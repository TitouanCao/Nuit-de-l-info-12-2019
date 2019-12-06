use super::schema::Survey;

#[derive(Queryable,Debug,Serialize,Deserialize,Insertable,FromForm)]
#[table_name="Survey"]
pub struct SurveyAnswer {
    pub id: i32,
    pub user_nickname: Option<String>,
    pub type_etudiant: Option<String>,
    pub handicap: Option<bool>,
    pub type_logement: Option<String>,
    pub ressource_bourses: Option<i32>,
    pub ressource_job_etudiant: Option<i32>,
    pub ressource_parents: Option<i32>
}


#[derive(Queryable,Debug,Serialize,Deserialize,Insertable,FromForm)]
#[table_name="Survey"]
pub struct NewSurveyAnswer {
    pub user_nickname: Option<String>,
    pub type_etudiant: Option<String>,
    pub handicap: Option<bool>,
    pub type_logement: Option<String>,
    pub ressource_bourses: Option<i32>,
    pub ressource_job_etudiant: Option<i32>,
    pub ressource_parents: Option<i32>
}