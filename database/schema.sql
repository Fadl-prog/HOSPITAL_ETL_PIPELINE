create database if not exists hospital;
use hospital;


/* tables de dim pour le shema en etoile */


create table if not exists dim_patient(
    id_patient int primary key auto_increment,
    prenom_patient varchar(25) not null,
    nom_patient varchar(25) not null,
    age_patient int not null check(age_patient >= 0),
    sexe_patient enum('M','F','O') not null,
    num_dossier_patient varchar(20) not null unique ,
    ville_patient varchar(40)

)Engine=InnoDB;

create table if not exists dim_medecin(
    id_medecin int primary key auto_increment,
    prenom_medecin varchar(25) not null,
    nom_medecin varchar(25) not null,
    specialite_medecin varchar(50) not null,
    grade varchar(25) not null
)Engine=InnoDB;

create table if not exists dim_departement(
    id_departement int primary key auto_increment,
    nom_departement varchar(50) not null,
    batiment_departement varchar(20),
    etage_departement varchar(20)
)Engine=InnoDB;

create table if not exists dim_date(
    id_date int primary key auto_increment,
    date_complete date not null ,
    mois_date int not null check(mois_date<13 and mois_date>0),
    jour_sem_date int not null check(jour_sem_date>=0 and jour_sem_date<=6),
    annee_date int not null check(annee_date > 0) 
)Engine=InnoDB;

create table if not exists dim_medicament
(
    id_medicament int primary key auto_increment,
    nom_medicament varchar(25) not null,
    description_medicament varchar(200)
)Engine=InnoDB;


/* maintenant , les tables fact regroupant les tables de dim */

create table if not exists fact_admission(
    id_patient int not null,
    id_medecin int not null,
    id_departement int not null,
    id_date int not null,
    duree_sejour int not null check(duree_sejour > 0),
    cout_hebergement float not null check(cout_hebergement >= 0),
    cout_total float not null check(cout_total >=0),
    cout_par_jour float not null check(cout_par_jour >=0),
    cout_soins_infirmiers float not null check(cout_soins_infirmiers >=0),
    constraint fk_id_patient_adm foreign key(id_patient) references dim_patient(id_patient) on update cascade ,
    constraint fk_id_medecin_adm foreign key(id_medecin) references dim_medecin(id_medecin) on update cascade,
    constraint fk_id_departement_adm foreign key(id_departement) references dim_departement(id_departement) on update cascade,
    constraint fk_id_date_adm foreign key(id_date) references dim_date(id_date) on update cascade,
    constraint pk_admission primary key(id_patient,id_medecin,id_departement,id_date)
)Engine=InnoDB;

create table if not exists fact_ordonnance(
    id_patient int not null,
    id_medecin int not null,
    id_date int not null,
    id_medicament int not null,
    prix_medicament float not null check(prix_medicament >= 0),
    duree_ordonnace int not null check(duree_ordonnace > 0),
    constraint fk_id_patient_ord foreign key(id_patient) references dim_patient(id_patient) on update cascade,
    constraint fk_id_medecin_ord foreign key(id_medecin) references dim_medecin(id_medecin) on update cascade,
    constraint fk_id_date_ord foreign key(id_date) references dim_date(id_date) on update cascade,
    constraint fk_id_medicament_ord foreign key(id_medicament) references dim_medicament(id_medicament) on update cascade,
    constraint pk_ord primary key(id_patient,id_medecin,id_date,id_medicament)
)Engine=InnoDB;

