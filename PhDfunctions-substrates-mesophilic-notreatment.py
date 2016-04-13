import matplotlib.pyplot as plt
from pylab import *
import numpy as np
twentyfive_sludge=0
fifty_sludge=0
seventyfive_sludge=0
raw_sludge=0
dict_substrates={}
dict_real_production={}
def theoretical_meso_biogas_substrates_notreatmentFM(raw_sludge, dict_substrates, dict_real_production):
    raw_sludge=5.90
    dict_substrates={'Slaughterhouse waste': 27.64, "Miscanthus Giganteus": 11.61, "Wheat Straw":16.32}
    dict_real_production={'Slaughterhouse waste': 23.81, "Miscanthus Giganteus": 11.83, "Wheat Straw":10.69}
    #It creates a list of theoretical biogas efficiencies from the production of the 
    #raw sludge and the production of the substrates without sludge, and compares it with the real production of the mixture
    #Everything in terms of Fresh Matter
    for i in dict_substrates:
        print " "
        print "THEORETICAL MESOPHILIC BIOGAS PRODUCTION OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF FRESH MATTER"
        print " "
        twentyfive_sludge=0.25*raw_sludge+0.75*dict_substrates[i]
        fifty_sludge=0.5*raw_sludge+0.5*dict_substrates[i]
        seventyfive_sludge=0.75*raw_sludge+0.25*dict_substrates[i]
        print "The production of 100% of sewage sludge is: " + str(raw_sludge) + "[m3/t f.m.]"
        print "|The theoretical production of 75% of sewage sludge and 25% of " + i + " is " + str(seventyfive_sludge) + "[m3/t f.m.]" + "|"      
        print "|The theoretical production of 50% of sewage sludge and 50% of " + i + " is " + str(fifty_sludge)+ "[m3/t f.m.]"+ "|" 
        print "|The theoretical production of 25% of sewage sludge and 75% of " + i + " is " + str(twentyfive_sludge)+ "[m3/t f.m.]"+ "|" 
        print "The production of 100% of " + i + " is " + str(dict_substrates[i])+ "[m3/t f.m.]"
        print "And the real production of 75% of sewage sludge and 25% of " + i + " was " + str(dict_real_production[i])+ "[m3/t f.m.]"
        sinergy=((dict_real_production[i]-seventyfive_sludge)/dict_real_production[i])*100
        print "The observed sinergy effect of mixing sewage sludge with " + i + " was: " + str(round (sinergy,2)) + "%"
        plt.figure("THEORETICAL MESOPHILIC BIOGAS PRODUCTION OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF FRESH MATTER")
        pos = arange(5)+ .5
        pos2 = arange(5)+.13
        plt.ylim([0,dict_substrates[i]+100])
        if dict_real_production[i] > seventyfive_sludge:
            pos2= arange(5)+.03
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
        else:
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
        xticks(pos, ("100%-0%", "75%-25%", "50%-50%", "25%-75%" , "0%-100%" ))
        xlabel("Amount of sewage sludge in the mixture % - Amount of "+i+" in the mixture %")
        ylabel("Fressh matter biogas production [m3/t f.m.]")
        title(" SEWAGE SLUDGE MIXED WITH " + i.upper() + ", FRESH MATTER")
        if dict_real_production[i] > seventyfive_sludge:
            plt.text(.95, dict_real_production[i] + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        else:
            plt.text(.95, seventyfive_sludge + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        plt.legend()
        grid(True)
        show()

def theoretical_meso_biogas_substrates_notreatmentODM(raw_sludge, dict_substrates, dict_real_production):
    raw_sludge=430.69
    dict_substrates={'Slaughterhouse waste': 1072.64, "Miscanthus Giganteus": 430.40, "Wheat Straw":592.37}
    dict_real_production={'Slaughterhouse waste': 943.11, "Miscanthus Giganteus": 396.24, "Wheat Straw":426.68}
    #It creates a list of theoretical biogas efficiencies from the production of the 
    #raw sludge and the production of the substrates without sludge, and compares it with the real production of the mixture
    #Everything in terms of Fresh Matter
    for i in dict_substrates:
        print " "
        print "THEORETICAL MESOPHILIC BIOGAS PRODUCTION OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF ORGANIC DRY MATTER"
        print " "
        twentyfive_sludge=0.25*raw_sludge+0.75*dict_substrates[i]
        fifty_sludge=0.5*raw_sludge+0.5*dict_substrates[i]
        seventyfive_sludge=0.75*raw_sludge+0.25*dict_substrates[i]
        print "The production of 100% of sewage sludge is: " + str(raw_sludge) + "[m3/t f.m.]"
        print "|The theoretical production of 75% of sewage sludge and 25% of " + i + " is " + str(seventyfive_sludge) + "[m3/t f.m.]" + "|"      
        print "|The theoretical production of 50% of sewage sludge and 50% of " + i + " is " + str(fifty_sludge)+ "[m3/t f.m.]"+ "|" 
        print "|The theoretical production of 25% of sewage sludge and 75% of " + i + " is " + str(twentyfive_sludge)+ "[m3/t f.m.]"+ "|" 
        print "The production of 100% of " + i + " is " + str(dict_substrates[i])+ "[m3/t f.m.]"
        print "And the real production of 75% of sewage sludge and 25% of " + i + " was " + str(dict_real_production[i])+ "[m3/t f.m.]"
        sinergy=((dict_real_production[i]-seventyfive_sludge)/dict_real_production[i])*100
        print "The observed sinergy effect of mixing sewage sludge with " + i + " was: " + str(round (sinergy,2)) + "%"
        plt.figure("THEORETICAL MESOPHILIC BIOGAS PRODUCTION OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF ORGANIC DRY MATTER")
        pos = arange(5)+ .5
        pos2 = arange(5)+.13
        plt.ylim([0,dict_substrates[i]+200])
        if dict_real_production[i] > seventyfive_sludge:
            pos2= arange(5)+.03
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
        else:
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
        
        xticks(pos, ("100%-0%", "75%-25%", "50%-50%", "25%-75%" , "0%-100%" ))
        xlabel("Amount of sewage sludge in the mixture % - Amount of "+i+" in the mixture %")
        ylabel("Organic dry matter biogas production [m3/t f.m.]")
        title(" SEWAGE SLUDGE MIXED WITH " + i.upper() + ", ORGANIC DRY MATTER")
        if dict_real_production[i] > seventyfive_sludge:
            plt.text(.95, dict_real_production[i] + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        else:
            plt.text(.95, seventyfive_sludge + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        plt.legend()
        grid(True)
        show()

def theoretical_meso_methane_substrates_notreatmentFM(raw_sludge, dict_substrates, dict_real_production):
    raw_sludge=3.49
    dict_substrates={'Slaughterhouse waste': 18.98, "Miscanthus Giganteus": 6.20, "Wheat Straw":8.45}
    dict_real_production={'Slaughterhouse waste': 16.28, "Miscanthus Giganteus": 6.46, "Wheat Straw":5.99}
    #It creates a list of theoretical biogas efficiencies from the production of the 
    #raw sludge and the production of the substrates without sludge, and compares it with the real production of the mixture
    #Everything in terms of Fresh Matter
    for i in dict_substrates:
        print " "
        print "THEORETICAL MESOPHILIC METHANE PRODUCTION OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF FRESH MATTER"
        print " "
        twentyfive_sludge=0.25*raw_sludge+0.75*dict_substrates[i]
        fifty_sludge=0.5*raw_sludge+0.5*dict_substrates[i]
        seventyfive_sludge=0.75*raw_sludge+0.25*dict_substrates[i]
        print "The production of 100% of sewage sludge is: " + str(raw_sludge) + "[m3/t f.m.]"
        print "|The theoretical production of 75% of sewage sludge and 25% of " + i + " is " + str(seventyfive_sludge) + "[m3/t f.m.]" + "|"      
        print "|The theoretical production of 50% of sewage sludge and 50% of " + i + " is " + str(fifty_sludge)+ "[m3/t f.m.]"+ "|" 
        print "|The theoretical production of 25% of sewage sludge and 75% of " + i + " is " + str(twentyfive_sludge)+ "[m3/t f.m.]"+ "|" 
        print "The production of 100% of " + i + " is " + str(dict_substrates[i])+ "[m3/t f.m.]"
        print "And the real production of 75% of sewage sludge and 25% of " + i + " was " + str(dict_real_production[i])+ "[m3/t f.m.]"
        sinergy=((dict_real_production[i]-seventyfive_sludge)/dict_real_production[i])*100
        print "The observed sinergy effect of mixing sewage sludge with " + i + " was: " + str(round (sinergy,2)) + "%"
        plt.figure("THEORETICAL MESOPHILIC METHANE PRODUCTION OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF FRESH MATTER")
        pos = arange(5)+ .5
        pos2 = arange(5)+.13
        plt.ylim([0,dict_substrates[i]+100])
        if dict_real_production[i] > seventyfive_sludge:
            pos2= arange(5)+.03
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
        else:
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
        
        xticks(pos, ("100%-0%", "75%-25%", "50%-50%", "25%-75%" , "0%-100%" ))
        xlabel("Amount of sewage sludge in the mixture % - Amount of "+i+" in the mixture %")
        ylabel("Fresh matter methane production [m3/t f.m.]")
        title(" SEWAGE SLUDGE MIXED WITH " + i.upper() + ", FRESH MATTER")
        if dict_real_production[i] > seventyfive_sludge:
            plt.text(.95, dict_real_production[i] + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        else:
            plt.text(.95, seventyfive_sludge + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        plt.legend()
        grid(True)
        show()       
        

def theoretical_meso_methane_substrates_notreatmentODM(raw_sludge, dict_substrates, dict_real_production):
    raw_sludge=255.04
    dict_substrates={'Slaughterhouse waste': 736.40, "Miscanthus Giganteus": 229.95, "Wheat Straw":317.77}
    dict_real_production={'Slaughterhouse waste': 644.80, "Miscanthus Giganteus": 216.62, "Wheat Straw":239.24}
    #It creates a list of theoretical biogas efficiencies from the production of the 
    #raw sludge and the production of the substrates without sludge, and compares it with the real production of the mixture
    #Everything in terms of Fresh Matter
    for i in dict_substrates:
        print " "
        print "THEORETICAL MESOPHILIC METHANE PRODUCTION OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF ORGANIC DRY MATTER"
        print " "
        twentyfive_sludge=0.25*raw_sludge+0.75*dict_substrates[i]
        fifty_sludge=0.5*raw_sludge+0.5*dict_substrates[i]
        seventyfive_sludge=0.75*raw_sludge+0.25*dict_substrates[i]
        print "The production of 100% of sewage sludge is: " + str(raw_sludge) + "[m3/t f.m.]"
        print "|The theoretical production of 75% of sewage sludge and 25% of " + i + " is " + str(seventyfive_sludge) + "[m3/t f.m.]" + "|"      
        print "|The theoretical production of 50% of sewage sludge and 50% of " + i + " is " + str(fifty_sludge)+ "[m3/t f.m.]"+ "|" 
        print "|The theoretical production of 25% of sewage sludge and 75% of " + i + " is " + str(twentyfive_sludge)+ "[m3/t f.m.]"+ "|" 
        print "The production of 100% of " + i + " is " + str(dict_substrates[i])+ "[m3/t f.m.]"
        print "And the real production of 75% of sewage sludge and 25% of " + i + " was " + str(dict_real_production[i])+ "[m3/t f.m.]"
        sinergy=((dict_real_production[i]-seventyfive_sludge)/dict_real_production[i])*100
        print "The observed sinergy effect of mixing sewage sludge with " + i + " was: " + str(round (sinergy,2)) + "%"
        plt.figure("THEORETICAL MESOPHILIC METHANE PRODUCTION OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF ORGANIC DRY MATTER")
        pos = arange(5)+ .5
        pos2 = arange(5)+.13
        width = 0.75
        plt.ylim([0,dict_substrates[i]+200])
        if dict_real_production[i] > seventyfive_sludge:
            pos2= arange(5)+.03
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), width, color="yellow", label = "Real production")
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), width,color="orange", align = "center", label="Theoretical production")
        else:
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), width,color="orange", align = "center", label="Theoretical production")
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), width,color="yellow", label = "Real production")
        
        xticks(pos, ("100%-0%", "75%-25%", "50%-50%", "25%-75%" , "0%-100%" ))
        xlabel("Amount of sewage sludge in the mixture % - Amount of "+i+" in the mixture %")
        ylabel("Organic dry matter methane production [m3/t f.m.]")
        title(" SEWAGE SLUDGE MIXED WITH " + i.upper() + ", ORGANIC DRY MATTER")
        if dict_real_production[i] > seventyfive_sludge:
            plt.text(.95, dict_real_production[i] + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        else:
            plt.text(.95, seventyfive_sludge + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        grid(True)
        plt.legend()
        
        show()        


if __name__=="__main__":
    theoretical_meso_biogas_substrates_notreatmentFM(raw_sludge, dict_substrates, dict_real_production)
    theoretical_meso_biogas_substrates_notreatmentODM(raw_sludge, dict_substrates, dict_real_production)
    theoretical_meso_methane_substrates_notreatmentFM(raw_sludge, dict_substrates, dict_real_production)
    theoretical_meso_methane_substrates_notreatmentODM(raw_sludge, dict_substrates, dict_real_production)
