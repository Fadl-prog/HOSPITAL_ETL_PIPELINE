USE hospital;

/* le taux de la couverture commercial(combien de clients combien a visite par exemple)
/taux de realisation de lobjectif brut/net(vente brut ,resiliation brut , trouver le net)
/le taux de penetration du marche (ta part de marche par rapport aux concurrents)
/le taux de retention client (les clients quon a retenu de resilier)
/parc : le nombre de contrats actifs
/taux de concretisation de contrats
(Pour Maroc Telecom par exemple d'apres ma mere)*/ 

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

