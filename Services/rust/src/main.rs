#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use] extern crate rocket;
#[macro_use] extern crate rocket_contrib;
#[macro_use] extern crate rocket_codegen;

use dotenv::dotenv;
use std::env;
use rocket::request::Form;
use surkek::models::*;
use diesel::query_dsl::*;
#[macro_use] extern crate serde_derive;
use rocket_contrib::json::*;
use rocket::request::FromForm;
use diesel::prelude::*;

#[get("/get")]
fn get(connection: surkek::db::Connection) -> JsonValue {
    use surkek::schema::Survey::dsl::*;
    json!(Survey.load::<SurveyAnswer>(&*connection).unwrap())
}

#[get("/get?<survey_id>")]
fn getOne(connection: surkek::db::Connection, survey_id: i32) -> JsonValue {
    use surkek::schema::Survey::dsl::*;
    json!(Survey.filter(id.eq(&survey_id)).limit(1).load::<SurveyAnswer>(&*connection).unwrap())
}

#[post("/update?<survey_id>", data = "<form>")]
fn update(connection: surkek::db::Connection, form: Form<SurveyAnswer>, survey_id: i32) -> JsonValue {
    use surkek::schema::Survey::dsl::*;
    diesel::delete(Survey.filter(id.eq(&survey_id))).execute(&*connection);
    diesel::insert_into(Survey).values(form.0).execute(&*connection);
    json!(true)
}

#[post("/add", data = "<form>")]
fn add(connection: surkek::db::Connection, form: Form<NewSurveyAnswer> ) -> JsonValue {
    use surkek::schema::Survey::dsl::*;
    diesel::insert_into(Survey).values(form.0).execute(&*connection);
    json!(true)
}

fn main() {
    rocket::ignite()
        .manage(surkek::db::connect())
        .mount("/", routes![get,add,getOne,update])
        .launch();
}