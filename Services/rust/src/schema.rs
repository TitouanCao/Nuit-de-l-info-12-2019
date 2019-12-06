table! {
    Survey (id) {
        id -> Integer,
        user_nickname -> Nullable<Varchar>,
        type_etudiant -> Nullable<Char>,
        handicap -> Nullable<Bool>,
        type_logement -> Nullable<Char>,
        ressource_bourses -> Nullable<Integer>,
        ressource_job_etudiant -> Nullable<Integer>,
        ressource_parents -> Nullable<Integer>,
    }
}

table! {
    UserAccount (pseudo) {
        pseudo -> Varchar,
        password -> Nullable<Varchar>,
        codepostal -> Nullable<Integer>,
        expertlevel -> Nullable<Integer>,
    }
}

allow_tables_to_appear_in_same_query!(
    Survey,
    UserAccount,
);
