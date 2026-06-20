USE hospital;



/* nombre total d'admission */

SELECT COUNT(*) AS nombre_total_dadmission FROM fact_admission;


/* duree moyenne de sejour*/
SELECT AVG(duree_sejour) AS moyenne_duree_sejour FROM fact_admission 

    
/*Volume d'admission par departement */
    SELECT d.nom_departement,COUNT(*) AS nombre_dadmission FROM fact_admission as a JOIN dim_departement as d ON d.id_departement = a.id_departement
    GROUP BY nom_departement ORDER BY nombre_dadmission DESC;


/*Revenu total genere lors des admissions(Cout de l'hebergement et des infirmiers)*/
    SELECT SUM(cout_total) AS total_genere FROM fact_admission;

/*Cout moyen d'une admission par departement*/
    SELECT d.nom_departement,AVG(a.cout_total) cout_moyen_departement FROM fact_admission AS a 
        JOIN dim_departement as d GROUP BY nom_departement ORDER BY cout_moyen_departement DESC;

