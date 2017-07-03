ReadWeatherFile <- function (filename){
  
  # ******************************************************************************
  # *   This function reads a (unique) weather file P4503501                     *
  # *   It puts the data in tabular form                                         *
  #                                                                              *
  # *   It returns a DataFrame                                                   *
  # *                                                                            *
  # *  ATTENTION: This script is provided to participants as help                *
  # *               But WITHOUT ANY WARRANTY                                     *
  # *                                                                            *
  # ******************************************************************************
  
  texte.ligne <- readLines(filename)


  # ******************************************************************************
  # Translations (by Wojciech):                                                
  # - validite = validity
  # - 
  # - 
  # ******************************************************************************

  date.fabrication.fichier        <- texte.ligne[1]
  entete.temperature              <- texte.ligne[2]
  texte.couples.dates             <- texte.ligne[3:80]
  
  couples.dates <- read.fwf (textConnection(texte.couples.dates), 
                             widths=c(10,10),col.names=c("date.base","date.validite"),
                             header=FALSE)
  # Initializing an empty data.frame
  rs <- data.frame()
  
  # Boucle sur l'ensemble des 35 stations
  # Remarque : Utilisation d'une boucle for et "modèle de l'objet croissant" ("growing object") 
  # Cette méthode est en général peu performante en 'R, mais elle est suffisante ici (très peu d'itérations).
  # Elle a l'avantage d'être plus lisible que d'autres méthodes plus perfomantes (apply et/ou utilisation de packages plus spécialisés : data.table, dplyr, etc.).
  # A noter également que ce script ne fait aucune vérification de format (il suppose que tous les fichiers sont correctement formattés) et ne traite pas d'exceptions.
  
  for(s in 0:34){
    
    # Temperature
    
    # 10 lignes de données de température (à partir de la ligne 81)
    ts.1  <-  texte.ligne[80+1+s*10]
    ts.2  <-  texte.ligne[80+2+s*10]
    ts.3  <-  texte.ligne[80+3+s*10]
    ts.4  <-  texte.ligne[80+4+s*10]
    ts.5  <-  texte.ligne[80+5+s*10]
    ts.6  <-  texte.ligne[80+6+s*10]
    ts.7  <-  texte.ligne[80+7+s*10]
    ts.8  <-  texte.ligne[80+8+s*10]
    ts.9  <-  texte.ligne[80+9+s*10]
    ts.10 <-  texte.ligne[80+10+s*10]
    
    # Traitement individualisé de chacune de ces 10 lignes
    ti.1 <- strsplit(ts.1, split =' ')[[1]]
    ti.1 <- ti.1[ti.1!=""]
    station <- ti.1[1]
    ti.1 <- ti.1[-1]
    
    ti.2 <- strsplit(ts.2, split =' ')[[1]]
    ti.2 <- ti.2[ti.2!=""]
    
    ti.3 <- strsplit(ts.3, split =' ')[[1]]
    ti.3 <- ti.3[ti.3!=""]
    
    ti.4 <- strsplit(ts.4, split =' ')[[1]]
    ti.4 <- ti.4[ti.4!=""]
    
    ti.5 <- strsplit(ts.5, split =' ')[[1]]
    ti.5 <- ti.5[ti.5!=""]
    
    ti.6 <- strsplit(ts.6, split =' ')[[1]]
    ti.6 <- ti.6[ti.6!=""]
    
    ti.7 <- strsplit(ts.7, split =' ')[[1]]
    ti.7 <- ti.7[ti.7!=""]
    
    ti.8 <- strsplit(ts.8, split =' ')[[1]]
    ti.8 <- ti.8[ti.8!=""]
    
    ti.9 <- strsplit(ts.9, split =' ')[[1]]
    ti.9 <- ti.9[ti.9!=""]
    
    ti.10 <- strsplit(ts.10, split =' ')[[1]]
    ti.10 <- ti.10[ti.10!=""]
    
    # Constitution d'une matrice (78 lignes x 2 colonnes) de données de température
    # A ce stade les données sont encore des chaines de caractères
    tv <- c(ti.1, ti.2, ti.3, ti.4, ti.5, ti.6, ti.7, ti.8, ti.9, ti.10)
    tm <- matrix(data = tv, ncol = 2, byrow = TRUE )
    
    # Extraction des valeurs/précisions/origines/qualités
    tm.valeur    <- tm[,1]
    tm.precision <- substr(tm[, 2], 1, nchar(tm[, 2])-2)
    tm.origine   <- substr(tm[, 2], nchar(tm[, 2])-1, nchar(tm[, 2])-1)
    tm.qualite   <- substr(tm[, 2], nchar(tm[, 2]), nchar(tm[, 2]))
    

    # Nebulosités
    
    # 4 lignes de donnees de nebulosité (à partir de la ligne 510)
    ns.1  <-  texte.ligne[509+1+s*4]
    ns.2  <-  texte.ligne[509+2+s*4]
    ns.3  <-  texte.ligne[509+3+s*4]
    ns.4  <-  texte.ligne[509+4+s*4]
    
    # Traitement individualisé de chacune de ces 4 lignes
    ni.1 <- strsplit(ns.1, split ='')[[1]]
    ni.1 <- ni.1[-c(1,2,3)] # station = ni.1[1,2 et 3] ignorée
    ni.2 <- strsplit(ns.2, split ='')[[1]]
    ni.3 <- strsplit(ns.3, split ='')[[1]]
    ni.4 <- strsplit(ns.4, split ='')[[1]]
    
    # Constitution d'une matrice (78 lignes x 4 colonnes) de données de nébulosité
    # A ce stade les données sont encore des chaines de caractères
    nv <- c(ni.1, ni.2, ni.3, ni.4)
    nm <- matrix(data = nv,ncol=4,byrow = TRUE)
    
    
    # Extraction des precisions/origines/qualités
    nm.valeur    <- nm[, 1]
    nm.precision <- nm[, 2]
    nm.origine   <- nm[, 3]
    nm.qualite   <- nm[, 4]
    

    # Traitements des valeurs manquantes (NA) (température = -999 : NA  / Nébulosité = 9 : NA)
    tm.valeur    <- ifelse(tm.valeur =="-999",    NA, tm.valeur)
    tm.precision <- ifelse(tm.precision =="-999", NA, tm.precision)
    
    nm.valeur    <- ifelse(nm.valeur == "9",    NA, nm.valeur)
    nm.precision <- ifelse(nm.precision == "9", NA, nm.precision)
    
    
    # Constitution d'un data.frame regroupant les les données de la station
    fm           <- as.data.frame(cbind(tm.valeur,tm.precision, tm.origine, tm.qualite,nm.valeur,nm.precision, nm.origine, nm.qualite), stringsAsFactors = FALSE)
    fm           <- cbind(station,date.fabrication.fichier,couples.dates, fm)
    
    # Contribution au résultat total (ensemble des stations)
    rs <- rbind(rs, fm)
  }
  
  # Nom définitif des colonnes
  colnames(rs) <- c("station", "date.fabrication.fichier", "date.base", "date.validite",
                    "temperature", "temp.precision", "temp.origine", "temp.qualite",
                    "nebulosite", "neb.precision", "neb.origine", "neb.qualite"
                    )
  
  # Traitements complémentaires : types, unités et facteurs
  rs$station        <- as.factor(rs$station)
  
  rs$date.fabrication.fichier   <- strptime(rs$date.fabrication.fichier, format = "%Y%m%d%H%M%S", tz="UTC")
  rs$date.base                  <- strptime(rs$date.base, format = "%Y%m%d%H", tz="UTC")
  rs$date.validite              <- strptime(rs$date.validite, format = "%Y%m%d%H", tz="UTC")
  
  
  rs$temperature     <- as.numeric(rs$temperature)/10    # Conversion numerique (en °C) des températures 
  rs$temp.precision  <- as.numeric(rs$temp.precision)/10 # Conversion numerique (en °C) des précisions 
  rs$temp.origine    <- as.factor(rs$temp.origine)
  rs$temp.qualite    <- as.factor(rs$temp.qualite)
  
  rs$nebulosite     <- as.numeric(rs$nebulosite)         # Conversion numerique (en octa) des nébulosités
  rs$neb.precision  <- as.numeric(rs$neb.precision)      # Conversion numerique (en octa) des précisions
  rs$neb.origine    <- as.factor(rs$neb.origine)
  rs$neb.qualite    <- as.factor(rs$neb.qualite)
  
  full_filename = paste(filename, '.csv')
  #full_filename = paste('./preprocessed/', full_filename)
  write.csv(rs, full_filename) 
}

file_names <- list.files('./P4503501/2014/', full.names = TRUE)

for(i in 1:length(file_names)){
  ReadWeatherFile(file_names[i])
  iteration = paste('Iteration ', i)
  print(iteration)
  text = paste('File ', file_names[i], 'has been successfully tranformed into .csv!')
  print(text)
  
}


