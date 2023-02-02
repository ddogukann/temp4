from user.models import maas,bordro,calisan
from .models import hesaplama
from datetime import datetime,timedelta
import pandas as pd
def hesaplama1(ay,maasid,calisanid):
    maas1=maas.objects.get(id=maasid)

    bordro1=bordro.objects.get(maas_id=maas1)
    calisan1=calisan.objects.get(id=calisanid)

    data=hesaplama.objects.get(hesaplama_yili=2023)

    if(ay=="ocak"):
        aylikasgari=data.ocakasgari
        brutucret=maas1.maas_tutari1
        if maas1.para_birimi=="pick1":
            brutucret=brutucret*float(getdolar()[0][1])
        elif maas1.para_birimi=="pick2":
            brutucret=brutucret*float(geteuro()[0][1])
        gunsayisi=maas1.gunsayisi1
        argegun=maas1.argegun1
        oncekiaykumulatif=0
        oncekiaykumulatifasgariucret=0
    elif (ay=="subat"):
        aylikasgari=data.subatasgari
        brutucret=maas1.maas_tutari2
        gunsayisi=maas1.gunsayisi2
        argegun=maas1.argegun2
        oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="mart"):
        aylikasgari=data.martasgari
        brutucret=maas1.maas_tutari3
        gunsayisi=maas1.gunsayisi3
        argegun=maas1.argegun3
        oncekiaykumulatif=bordro1.subat_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="nisan"):
        aylikasgari=data.nisanasgari
        brutucret=maas1.maas_tutari4
        gunsayisi=maas1.gunsayisi4
        argegun=maas1.argegun4
        oncekiaykumulatif=bordro1.mart_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="mayis"):
        aylikasgari=data.mayisasgari
        brutucret=maas1.maas_tutari5
        gunsayisi=maas1.gunsayisi5
        argegun=maas1.argegun5
        oncekiaykumulatif=bordro1.nisan_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.nisan_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mart_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="haziran"):
        aylikasgari=data.haziranasgari
        brutucret=maas1.maas_tutari6
        gunsayisi=maas1.gunsayisi6
        argegun=maas1.argegun6
        oncekiaykumulatif=bordro1.mayis_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.mayis_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.nisan_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.nisan_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mart_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="temmuz"):
        aylikasgari=data.temmuzasgari
        brutucret=maas1.maas_tutari7
        gunsayisi=maas1.gunsayisi7
        argegun=maas1.argegun7
        oncekiaykumulatif=bordro1.haziran_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.haziran_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mayis_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mayis_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.nisan_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.nisan_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mart_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="agustos"):
        aylikasgari=data.agustosasgari
        brutucret=maas1.maas_tutari8
        gunsayisi=maas1.gunsayisi8
        argegun=maas1.argegun8
        oncekiaykumulatif=bordro1.temmuz_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.temmuz_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.haziran_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.haziran_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mayis_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mayis_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.nisan_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.nisan_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mart_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="eylul"):
        aylikasgari=data.eylulasgari
        brutucret=maas1.maas_tutari9
        gunsayisi=maas1.gunsayisi9
        argegun=maas1.argegun9
        oncekiaykumulatif=bordro1.agustos_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.agustos_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.temmuz_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.temmuz_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.haziran_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.haziran_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mayis_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mayis_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.nisan_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.nisan_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mart_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="ekim"):
        aylikasgari=data.ekimasgari
        brutucret=maas1.maas_tutari10
        gunsayisi=maas1.gunsayisi10
        argegun=maas1.argegun10
        oncekiaykumulatif=bordro1.eylul_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.eylul_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.agustos_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.agustos_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.temmuz_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.temmuz_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.haziran_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.haziran_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mayis_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mayis_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.nisan_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.nisan_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mart_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="kasim"):
        aylikasgari=data.kasimasgari
        brutucret=maas1.maas_tutari11
        gunsayisi=maas1.gunsayisi11
        argegun=maas1.argegun11
        oncekiaykumulatif=bordro1.ekim_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.ekim_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.eylul_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.eylul_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.agustos_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.agustos_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.temmuz_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.temmuz_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.haziran_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.haziran_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mayis_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mayis_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.nisan_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.nisan_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mart_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    elif (ay=="aralik"):
        aylikasgari=data.aralikasgari
        brutucret=maas1.maas_tutari12
        gunsayisi=maas1.gunsayisi12
        argegun=maas1.argegun12
        oncekiaykumulatif=bordro1.kasim_kumulatif_vergi
        oncekiaykumulatifasgariucret=bordro1.kasim_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ekim_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ekim_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.eylul_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.eylul_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.agustos_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.agustos_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.temmuz_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.temmuz_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.haziran_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.haziran_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mayis_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mayis_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.nisan_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.nisan_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.mart_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.mart_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.subat_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.subat_kumulatif_asgari_ucret
        if oncekiaykumulatif==0:
            oncekiaykumulatif=bordro1.ocak_kumulatif_vergi
            oncekiaykumulatifasgariucret=bordro1.ocak_kumulatif_asgari_ucret
    indirim=calisan1.calisan_indirim
    egitimdurumu="pick1"
    emeklicalisan=calisan1.calisan_emekli
    calisanturu=calisan1.calisan_tesvik
    engelli=calisan1.calisan_engelli
    asgaritavanorani=data.asgaritavanorani
    sgkkesintiorani1=data.sgkkesintiorani1
    emeklisgkorani=data.emeklisgkorani
    issizlikkesintiorani=data.issizlikkesintiorani
    birinciderece=data.birinciderece
    ikinciderece=data.ikinciderece
    ucuncuderece=data.ucuncuderece
    otuzbesvergidilimi=data.otuzbesvergidilimi
    yirmiyedivergidilimi=data.yirmiyedivergidilimi
    yirmivergidilimi=data.yirmivergidilimi
    onbesvergidilimi=data.onbesvergidilimi
    asgarimatrahorani=data.asgarimatrahorani
    damgavergiorani=data.damgavergiorani
    issizlikisverenoran=data.issizlikisverenoran
    sgkistisnasioran=data.sgkkesintiorani
    gelirvergioran1=data.gelirvergioran1
    gelirvergioran2=data.gelirvergioran2
    gelirvergioran3=data.gelirvergioran3
    gelirvergioran4=data.gelirvergioran4
    egitim1geliroran=data.egitim1geliroran
    egitim2geliroran=data.egitim2geliroran
    egitim3geliroran=data.egitim3geliroran
    sgkkesintiorani=data.sgkkesintiorani
    if maas1.ucrettipi=="pick1":
        brutucret=get_nettenbrute(brutucret,gunsayisi,aylikasgari,asgaritavanorani,sgkkesintiorani1,emeklicalisan,emeklisgkorani,calisanturu,sgkkesintiorani,issizlikkesintiorani,issizlikisverenoran,engelli,birinciderece,ikinciderece,ucuncuderece,damgavergiorani,oncekiaykumulatif,otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,asgarimatrahorani,oncekiaykumulatifasgariucret)
    bordroyaesas=get_bordroyaesasbrut(brutucret,gunsayisi)
    sgkmatrah=get_sgkmatrahi(brutucret,gunsayisi,aylikasgari,asgaritavanorani)
    sgkkesinti=get_sgkkesintisi(sgkkesintiorani1,emeklicalisan,emeklisgkorani,calisanturu,sgkmatrah)
    issizlikkesinti=get_issizlikkesintisi(issizlikkesintiorani,emeklicalisan,calisanturu,sgkmatrah)
    vergimatrahi=get_vergimatrahi(engelli,birinciderece,ikinciderece,ucuncuderece,bordroyaesas,sgkkesinti,issizlikkesinti)
    kumulatifvergimatrahi=get_kumulatifvergimatrahi(oncekiaykumulatif,vergimatrahi)
    istisnaoncesigelirvergisi=get_istisnaoncesigelirvergisi(oncekiaykumulatif,otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,kumulatifvergimatrahi)
    asgariucretvergimatrahi=get_asgariucretvergimatrahi(aylikasgari,asgarimatrahorani)
    kumulatifasgariucret=get_kumulatifasgariucret(oncekiaykumulatifasgariucret,asgariucretvergimatrahi)
    asgarigelirvergisiistisnasi=get_asgarigelirvergisiistisnasi(otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,kumulatifasgariucret,oncekiaykumulatifasgariucret,istisnaoncesigelirvergisi)
    damgavergisi=get_damgavergisi(bordroyaesas,aylikasgari,damgavergiorani)
    gelirvergisiodemesi=get_gelirvergisiasgaridusulmus(bordroyaesas,asgariucretvergimatrahi,istisnaoncesigelirvergisi,asgarigelirvergisiistisnasi)
    netucret=get_netucret(bordroyaesas,sgkkesinti,issizlikkesinti,damgavergisi,gelirvergisiodemesi)
    sgkisveren=get_sgkisveren(calisanturu,sgkmatrah,sgkkesintiorani,emeklicalisan)
    issizlikkesintisiisveren=get_issizlikkesintisiisveren(sgkmatrah,issizlikisverenoran,calisanturu,emeklicalisan)
    toplamsgkkesintisi=get_toplamsgkkesintisi(sgkisveren,issizlikkesintisiisveren,sgkkesinti,issizlikkesinti)
    sgkistisnasi=get_sgkistisnasi(sgkmatrah,sgkisveren,toplamsgkkesintisi,sgkistisnasioran,emeklicalisan,calisanturu,indirim,aylikasgari,gunsayisi,argegun)
    odeneceksgk=get_odeneceksgk(sgkistisnasi,toplamsgkkesintisi)
    gelirvergisi=get_gelirvergisiodemesi(brutucret,asgariucretvergimatrahi,istisnaoncesigelirvergisi,asgarigelirvergisiistisnasi)
    gelirverigsi1=get_gelirvergisi(gelirvergisi,argegun,gunsayisi,calisanturu,egitimdurumu,egitim1geliroran,egitim2geliroran,egitim3geliroran)
    damgaodemesi=get_damgavergisiodemesi(calisanturu,damgavergisi,argegun,gunsayisi)
    indirimsizdamga=get_indirimsizdamgavergisi(bordroyaesas,damgavergiorani)
    damgaistisnasi=get_damgaistisnasi(damgavergisi,indirimsizdamga)
    toplammaliyet=get_toplammaliyet1(netucret,odeneceksgk,gelirverigsi1,damgaodemesi)
    geliroran=get_gelirvergisioran(kumulatifvergimatrahi,gelirvergioran1,gelirvergioran2,gelirvergioran3,gelirvergioran4)
    asgaridensonragelirvergisi=get_asgaridensonragelirvergisiistisnasi(calisanturu,gelirvergisi,gunsayisi,argegun,egitim1geliroran,egitim2geliroran,egitim3geliroran,egitimdurumu)
    asgaridensonradamgavergisi=get_asgaridensonradamgavergisiistisnasi(calisanturu,argegun,gunsayisi,damgavergisi)

    bordro2=[]
    bordro2.append(("{:.2f}".format(brutucret)))
    bordro2.append(gunsayisi)
    bordro2.append(argegun)
    bordro2.append(("{:.2f}".format(bordroyaesas)))
    bordro2.append(("{:.2f}".format(sgkmatrah)))
    bordro2.append(("{:.2f}".format(sgkkesinti)))
    bordro2.append(("{:.2f}".format(issizlikkesinti)))
    bordro2.append(("{:.2f}".format(vergimatrahi)))
    bordro2.append(("{:.2f}".format(kumulatifvergimatrahi)))
    bordro2.append(("{:.2f}".format(istisnaoncesigelirvergisi)))
    bordro2.append(("{:.2f}".format(kumulatifasgariucret)))
    bordro2.append(("{:.2f}".format(asgarigelirvergisiistisnasi)))
    bordro2.append(("{:.2f}".format(damgavergisi)))
    bordro2.append(("{:.2f}".format(gelirvergisiodemesi)))
    bordro2.append(("{:.2f}".format(netucret)))
    bordro2.append(("{:.2f}".format(sgkisveren)))
    bordro2.append(("{:.2f}".format(issizlikkesintisiisveren)))
    bordro2.append(("{:.2f}".format(toplamsgkkesintisi)))
    bordro2.append(("{:.2f}".format(sgkistisnasi)))
    bordro2.append(("{:.2f}".format(odeneceksgk)))
    bordro2.append(("{:.2f}".format(gelirvergisi)))
    bordro2.append(("{:.2f}".format(gelirverigsi1)))
    bordro2.append(("{:.2f}".format(damgaodemesi)))
    bordro2.append(("{:.2f}".format(indirimsizdamga)))
    bordro2.append(("{:.2f}".format(damgaistisnasi)))
    bordro2.append(("{:.2f}".format(toplammaliyet)))
    bordro2.append((geliroran))
    bordro2.append(("{:.2f}".format(asgaridensonragelirvergisi)))
    bordro2.append(("{:.2f}".format(asgaridensonradamgavergisi)))
    return bordro2
def getdolar():
    startDate= ""
    endDate=""
    if int(datetime.now().hour)<15 and int(datetime.now().minute)<30:
        date_today = (datetime.today()-timedelta(days=1)).date().strftime("%d-%m-%Y")
        startDate=date_today
        endDate=date_today
        
    else:
        date_today = (datetime.today()).date().strftime("%d-%m-%Y")
        startDate=date_today
        endDate=date_today


    i=1
    while True:
        series ="TP.DK.USD.A.YTL"
        series_name="Dolar_Kuru"
        typee="csv"
        key="dJqoNMHhsC"
        aggregationTypes="avg"
        formulas="0"
        frequency = "2"
        url= 'https://evds2.tcmb.gov.tr/service/evds/series={}&startDate={}&endDate={}&type={}&key={}&aggregationTypes={}&formulas={}&frequency={}'.format(series,
        startDate,endDate,typee,key,aggregationTypes,formulas,frequency)
        try:
            dolar = pd.read_csv(url)
            break
        except:
            date_today = (datetime.today()-timedelta(days=i)).date().strftime("%d-%m-%Y")
            startDate= date_today
            endDate=date_today
            i+=1
            
    
        
        
   
    
    dolar1=dolar.values.tolist()

    
    return dolar1
def geteuro():
    startDate= ""
    endDate=""
    if int(datetime.now().hour)<15 and int(datetime.now().minute)<30:
        date_today = (datetime.today()-timedelta(days=1)).date().strftime("%d-%m-%Y")
        startDate=date_today
        endDate=date_today
    else:
        date_today = (datetime.today()).date().strftime("%d-%m-%Y")
        startDate=date_today
        endDate=date_today

    i=1
    while True:
        series ="TP.DK.EUR.A.YTL"
        series_name="Euro_Kuru"
        typee="csv"
        key="dJqoNMHhsC"
        aggregationTypes="avg"
        formulas="0"
        frequency = "2"
        url= 'https://evds2.tcmb.gov.tr/service/evds/series={}&startDate={}&endDate={}&type={}&key={}&aggregationTypes={}&formulas={}&frequency={}'.format(series,
        startDate,endDate,typee,key,aggregationTypes,formulas,frequency)
        try:
            euro = pd.read_csv(url)
            break
        except:
            date_today = (datetime.today()-timedelta(days=i)).date().strftime("%d-%m-%Y")
            startDate= date_today
            endDate=date_today
            i+=1

    euro1=euro.values.tolist()
    
    return euro1
def hesaplama2(brutucret,gunsayisi,aylikasgari,asgaritavanorani,sgkkesintiorani1,emeklicalisan,emeklisgkorani,calisanturu,sgkkesintiorani,issizlikkesintiorani,issizlikisverenoran,engelli,birinciderece,ikinciderece,ucuncuderece,damgavergiorani,oncekiaykumulatif,otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,asgarimatrahorani,oncekiaykumulatifasgariucret):
    bordroyaesas=get_bordroyaesasbrut(brutucret,gunsayisi)
    sgkmatrah=get_sgkmatrahi(brutucret,gunsayisi,aylikasgari,asgaritavanorani)
    sgkkesinti=get_sgkkesintisi(sgkkesintiorani1,emeklicalisan,emeklisgkorani,calisanturu,sgkmatrah)
    issizlikkesinti=get_issizlikkesintisi(issizlikkesintiorani,emeklicalisan,calisanturu,sgkmatrah)
    vergimatrahi=get_vergimatrahi(engelli,birinciderece,ikinciderece,ucuncuderece,bordroyaesas,sgkkesinti,issizlikkesinti)
    kumulatifvergimatrahi=get_kumulatifvergimatrahi(oncekiaykumulatif,vergimatrahi)
    istisnaoncesigelirvergisi=get_istisnaoncesigelirvergisi(oncekiaykumulatif,otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,kumulatifvergimatrahi)
    asgariucretvergimatrahi=get_asgariucretvergimatrahi(aylikasgari,asgarimatrahorani)
    kumulatifasgariucret=get_kumulatifasgariucret(oncekiaykumulatifasgariucret,asgariucretvergimatrahi)
    asgarigelirvergisiistisnasi=get_asgarigelirvergisiistisnasi(otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,kumulatifasgariucret,oncekiaykumulatifasgariucret,istisnaoncesigelirvergisi)
    damgavergisi=get_damgavergisi(bordroyaesas,aylikasgari,damgavergiorani)
    gelirvergisiodemesi=get_gelirvergisiasgaridusulmus(bordroyaesas,asgariucretvergimatrahi,istisnaoncesigelirvergisi,asgarigelirvergisiistisnasi)
    netucret=get_netucret(bordroyaesas,sgkkesinti,issizlikkesinti,damgavergisi,gelirvergisiodemesi)
    
    return netucret


## Net Ücret Hesaplama Fonksiyonları
def get_bordroyaesasbrut(brutucret,gunsayisi):     
    return float(float(brutucret)/30*float(gunsayisi))

def get_sgkmatrahi(brutucret,gunsayisi,aylikasgari,asgaritavanorani):
    return float(min(float(brutucret),(aylikasgari*float(asgaritavanorani)))/30*float(gunsayisi))

def get_sgkkesintisi(sgkkesintiorani1,emeklicalisan,emeklisgkorani,calisanturu,sgkmatrah):

    if calisanturu=='pick7' or calisanturu=='pick8' or calisanturu=='pick9':
        return float(0)
    else:
        if emeklicalisan==False:
            return float(float(sgkmatrah)*float(sgkkesintiorani1))
        else:
            return float(float(sgkmatrah)*float(emeklisgkorani))
def get_issizlikkesintisi(issizlikkesintiorani,emeklicalisan,calisanturu,sgkmatrah):
    
    if calisanturu=='pick7' or calisanturu=='pick8' or calisanturu=='pick9' or emeklicalisan==True:
        return float(0)
    else:   
        return float(float(sgkmatrah)*float(issizlikkesintiorani))
   
def get_vergimatrahi(engelli,birinciderece,ikinciderece,ucuncuderece,bordroyaesasbrut,sgkkesintisi,issizlikkesintisi):
    
    if engelli=="pick0":
            return float(float(bordroyaesasbrut)-float(sgkkesintisi)-float(issizlikkesintisi))
    elif engelli=="pick1":
            return float(float(bordroyaesasbrut)-float(sgkkesintisi)-float(issizlikkesintisi)-float(birinciderece))
    elif engelli=="pick2":
            return float(float(bordroyaesasbrut)-float(sgkkesintisi)-float(issizlikkesintisi)-float(ikinciderece))
    elif engelli=="pick3":
            return float(float(bordroyaesasbrut)-float(sgkkesintisi)-float(issizlikkesintisi)-float(ucuncuderece))

def get_kumulatifvergimatrahi(oncekiaykumulatif,vergimatrahi):
    
    return float((float(oncekiaykumulatif)+float(vergimatrahi)))

def get_istisnaoncesigelirvergisi(oncekiaykumulatif,otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,kumulatif):

    return float((float(max(((float(kumulatif)-float(otuzbesvergidilimi))*5/100),0)+max((float(kumulatif)-float(yirmiyedivergidilimi))*8/100,0)+max((float(kumulatif)-float(yirmivergidilimi))*7/100,0)+max((float(kumulatif)-float(onbesvergidilimi))*5/100,0)+(float(kumulatif*15/100)))-(max((oncekiaykumulatif-float(otuzbesvergidilimi))*5/100,0)+max((oncekiaykumulatif-float(yirmiyedivergidilimi))*8/100,0)+max((float(oncekiaykumulatif)-float(yirmivergidilimi))*7/100,0)+max((float(oncekiaykumulatif)-float(onbesvergidilimi))*5/100,0)+(float(oncekiaykumulatif)*15/100))))

def get_asgariucretvergimatrahi(aylikasgari,asgarimatrahorani):
    return float(float(aylikasgari)*float(asgarimatrahorani))
    
def get_kumulatifasgariucret(asgarivergimatrahi,oncekikumulatifasgari):
    return ((float(float(oncekikumulatifasgari)+float(asgarivergimatrahi))))

def get_asgarigelirvergisiistisnasi(otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,kumulatifasgari,oncekiaykumulatifasgari,istisnaoncesigelirvergisi):
    
    temp=((max(((float(kumulatifasgari)-float(otuzbesvergidilimi))*5/100),0)+max((float(kumulatifasgari)-float(yirmiyedivergidilimi))*8/100,0)+max((float(kumulatifasgari)-float(yirmivergidilimi))*7/100,0)+max((float(kumulatifasgari)-float(onbesvergidilimi))*5/100,0)+(float(kumulatifasgari)*15/100))-(max((float(oncekiaykumulatifasgari)-float(otuzbesvergidilimi))*5/100,0)+max((float(oncekiaykumulatifasgari)-float(yirmiyedivergidilimi))*8/100,0)+max((float(oncekiaykumulatifasgari)-float(yirmivergidilimi))*7/100,0)+max((float(oncekiaykumulatifasgari)-float(onbesvergidilimi))*5/100,0)+(float(oncekiaykumulatifasgari)*15/100)))
    return (min(temp,istisnaoncesigelirvergisi))

def get_damgavergisi(bordroyaesasbrut,aylikasgari,damgavergiorani):
    
    if aylikasgari>float(bordroyaesasbrut):
        return (float((0)))
    else:
        return (((float(bordroyaesasbrut)-aylikasgari)*float(damgavergiorani)))

def get_gelirvergisiasgaridusulmus(bordroyaesasbrut,asgarivergimatrahi,istisnaoncesigelirvergisi,asgarigelirvergisiistisnasi):

    if float(bordroyaesasbrut)<float(asgarivergimatrahi):
        return (float((0)))
    else:
        return (abs(float((float(istisnaoncesigelirvergisi)-float(asgarigelirvergisiistisnasi)))))
    
def get_netucret(bordroyaesasbrut,issizlikkesintisi,sgkkesintisi,damgavergisi,gelirvergisiodemesi):     
    return (float((float(bordroyaesasbrut)-float(damgavergisi)-float(gelirvergisiodemesi)- float(issizlikkesintisi)- float(sgkkesintisi))))

def get_damgavergisiodemesi(damgavergisi,argegun,gunsayisi,calisanturu):
    if calisanturu=='pick1':
            return (float(damgavergisi))
    elif calisanturu=='pick2':
        if argegun==gunsayisi:
            return (float(0))
        else:
            return ((float(damgavergisi)-float(damgavergisi)*float(argegun)/float(gunsayisi)))
    elif calisanturu=='pick3':
        if argegun==gunsayisi:
            return (float(0))
        else:
            return ((float(damgavergisi)-float(damgavergisi)*float(argegun)/float(gunsayisi))) 
    elif calisanturu=='pick4':
            return (float(damgavergisi))
    elif calisanturu=='pick5':
            return (float(damgavergisi))
    elif calisanturu=='pick6':
             return (float(damgavergisi))
    elif calisanturu=='pick7':
            return (float(damgavergisi))
    elif calisanturu=='pick8':
        if argegun==gunsayisi:
            return (float(0))
        else:
            return ((float(damgavergisi)-float(damgavergisi)*float(argegun)/float(gunsayisi)))
    elif calisanturu=='pick9':
        if argegun==gunsayisi:
            return (float(0))
        else:
            return ((float(damgavergisi)-float(damgavergisi)*float(argegun)/float(gunsayisi)))

def get_sgkistisnasi(gunsayisi,argegun,calisanturu,aylikasgari,sgkmatrahi,sgkisveren,sgkistisnasi,toplamsgk,emeklicalisan,indirimm):

    if emeklicalisan==True:
            return (float(0))
    elif calisanturu=='pick1':
        if indirimm==False:
            return (float(0))
        else:
            return (float(sgkmatrahi)*0.05)
    elif calisanturu=='pick2':

        if indirimm==False:
                #sgkistisnasi.append((float(sgk[i])*float(sgkkesintiorani[0])*0.5*float(argegun[i])/float(gunsayisi1[i])))eski fonksiyon
            return (float(sgkmatrahi)*0)+((float(sgkmatrahi)*0.0775)*(float(argegun)/float(gunsayisi)))
        else:
                #sgkistisnasi.append((float(sgk[i])*0.5*(float(sgkkesintiorani[0])-float(indirimorani5510[0]))*float(argegun[i])/float(gunsayisi1[i])))eski fonksiyon
            return ((float(sgkmatrahi)*0.05)+((float(sgkmatrahi)*0.0775)*(float(argegun)/float(gunsayisi))))
    elif calisanturu=='pick3':
        if indirimm==False:
                #sgkistisnasi.append((float(sgk[i])*float(sgkkesintiorani[0])*0.5*float(argegun[i])/float(gunsayisi1[i])))
            return (float(sgkmatrahi)*0)+((float(sgkmatrahi)*0.0775)*(float(argegun)/float(gunsayisi)))## arge günü 0 durumu eklenecek
        else:
                #sgkistisnasi.append((float(sgk[i])*0.5*(float(sgkkesintiorani[0])-float(indirimorani5510[0]))*float(argegun[i])/float(gunsayisi1[i])))
            return ((float(sgkmatrahi)*0.05)+((float(sgkmatrahi)*0.0775)*float(argegun)/float(gunsayisi)))

    elif calisanturu=='pick4':
        return ((float(sgkisveren)))
    elif calisanturu[0]=='pick5':
            #sgkistisnasi.append((float(aylikasgari[i]*0.375)))
        istisna=float(float(aylikasgari)*float(gunsayisi)/30)*0.375
        istisna=min(istisna,toplamsgk)
        return (istisna)
           
    elif calisanturu=='pick6':
             #istisna=float(brutucret1[i])*0.375
        istisna=float(float(aylikasgari)/0.375*float(gunsayisi)/30)*0.375
        istisna=min(istisna,toplamsgk)
        return (istisna)
            #  if istisna<aylikasgari[i]:
            #      sgkistisnasi.append(float(istisna)*gunsayisi1[i]/30)
            #  else:
            #      sgkistisnasi.append(sgk[i])
            #sgkistisnasi.append((float(aylikasgari[i]/30*float(gunsayisi1[i]))))
           
    elif  calisanturu=='pick7' or calisanturu=='pick8' or calisanturu=='pick9':
        return (float(0))

def get_gelirvergisioran(kumulatifvergimatrahi,gelirvergioran1,gelirvergioran2,gelirvergioran3,gelirvergioran4):

    gelirvergideneme1=[]
    kumulatif=kumulatifvergimatrahi
    j=0
    k=0
    t=0
    y=0


    if kumulatif<=0:
        return ("%0")
            
    elif kumulatif>0 and kumulatif<gelirvergioran1:
        return  ("%15")
            
    elif kumulatif>=gelirvergioran1 and kumulatif<gelirvergioran2:
        if j ==0:
            j+=1
            return ("%15-20")
            
        else:
            gelirvergideneme1.append("%20")
           
    elif kumulatif>=gelirvergioran2 and kumulatif<gelirvergioran3:
        if k ==0:
            if j==0:
                return ("%15-20-27")
                k+=1
            else:
                return ("%20-27")
                k+=1
        else:
            return ("%27")
            
    elif kumulatif>=gelirvergioran3 and kumulatif<gelirvergioran4:
        if t ==0:
            if k==0:
                if j==0:
                    return ("%15-20-27-35")
                    t+=1
                else:
                    return ("%20-27-35")
                    t+=1
            else:
                return ("%27-35")
                t+=1
        else:
            return ("%35")
           
    elif kumulatif>=gelirvergioran4:
        if y ==0:
            if t==0:
                if k==0:
                    if j==0:
                        return ("%15-20-27-35-40")
                        y+=1
                    else:
                        return ("%20-27-35-40")
                        y+=1
                else:
                    return ("%27-35-40")
                    y+=1
            else:
                return ("%35-40")
                y+=1
        else:
            return ("%40")
            
def get_nettenbrute(netucret,gunsayisi,aylikasgari,asgaritavanorani,sgkkesintiorani1,emeklicalisan,emeklisgkorani,calisanturu,sgkkesintiorani,issizlikkesintiorani,issizlikisverenoran,engelli,birinciderece,ikinciderece,ucuncuderece,damgavergiorani,oncekiaykumulatif,otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,asgarimatrahorani,oncekiaykumulatifasgariucret):    
    enteredamount=0
    for i in range(12):
        enteredamount= float(netucret)*(float(gunsayisi)/30)
        left = enteredamount/30
        right = 30* enteredamount
        middle= (left+right)/2
        k=0
        while abs(left-right)>0.0001 and k<100:
            if float(hesaplama2(middle,gunsayisi,aylikasgari,asgaritavanorani,sgkkesintiorani1,emeklicalisan,emeklisgkorani,calisanturu,sgkkesintiorani,issizlikkesintiorani,issizlikisverenoran,engelli,birinciderece,ikinciderece,ucuncuderece,damgavergiorani,oncekiaykumulatif,otuzbesvergidilimi,yirmiyedivergidilimi,yirmivergidilimi,onbesvergidilimi,asgarimatrahorani,oncekiaykumulatifasgariucret))>enteredamount:
                right=middle             
            else:
                left=middle
            middle=(left+right)/2
            k=k+1

    return middle
    
##Net Ücret hesaplama fonksiyonu

def get_sgkisveren(calisanturu,sgkmatrahi,sgkkesintiorani,emeklicalisan):
    matrah=sgkmatrahi
    if calisanturu=='pick7' or calisanturu=='pick8' or calisanturu=='pick9':
        return float((0))
    else:
        if emeklicalisan==False:
                    
            return ((float(matrah)*float(sgkkesintiorani)))
        else:
            return ((float(matrah)*0.225))

def get_issizlikkesintisiisveren(sgkmatrahi,issizlikisverenoran,calisanturu,emeklicalisan,):
    matrah=sgkmatrahi
    if calisanturu=='pick7' or calisanturu=='pick8' or calisanturu=='pick9' or emeklicalisan==True:
        return float((0))
    else:
        return ((float(matrah)*float(issizlikisverenoran)))

def get_toplamsgkkesintisi(sgkisveren,issizlikkesintisiisveren,sgkisci,issizlikkesintisi):

    return ((float(sgkisveren)+float(issizlikkesintisiisveren)+float(sgkisci)+float(issizlikkesintisi)))

def get_sgkistisnasi(sgkmatrahi,sgkisveren,toplamsgk,sgkistisnasioran,emeklicalisan,calisanturu,indirim,aylikasgari,gunsayisi,argegun):
    sgkistisnasi=[]
    sgk=sgkmatrahi
    if emeklicalisan==True:
        return float((0))
    elif calisanturu=='pick1':
        if indirim==False:
            return float(0)
        else:                
            return (float(sgk)*0.05)
    elif calisanturu=='pick2':
        if float(argegun!=0):
            if indirim==False:
                return ((float(sgk)*0)+((float(sgk)*0.0775)*(float(argegun)/float(gunsayisi))))
            else:
                return ((float(sgk)*0.05)+((float(sgk)*0.0775)*(float(argegun)/float(gunsayisi))))
        else:
             return float(0)
    elif calisanturu=='pick3':
            if float(argegun!=0):
                if indirim==False:
                    return ((float(sgk)*0)+((float(sgk)*0.0775)*float(argegun)/float(gunsayisi)))
                else:
                    return ((float(sgk)*0.05)+((float(sgk)*0.0775)*float(argegun)/float(gunsayisi)))
            else:
                return float(0)

    elif calisanturu=='pick4':
            return ((float(sgkisveren)))
    elif calisanturu=='pick5':
            istisna=float(float(aylikasgari)*float(gunsayisi)/30)*0.375
            istisna=min(istisna,toplamsgk[i])
            return (istisna)
           
    elif calisanturu=='pick6':
             
            istisna=float(float(aylikasgari)/0.375*float(gunsayisi)/30)*0.375
            istisna=min(istisna,toplamsgk[i])
            return (istisna)

    elif  calisanturu=='pick7' or calisanturu=='pick8' or calisanturu=='pick9':
        return ((0))

def get_odeneceksgk(sgkistisnasi,toplamsgkkesintisi):

    return ((float(toplamsgkkesintisi)-float(sgkistisnasi)))

def get_gelirvergisiodemesi(brutucret,asgarivergimatrahi,istisnaoncesi,asgarigelirvergisi):
    if float(brutucret)<float(asgarivergimatrahi):
        return (float((0)))
    else:
        return (abs(float((float(istisnaoncesi)-float(asgarigelirvergisi)))))

def get_gelirvergisi(gelirvergisiodemesi,argegun,gunsayisi,calisanturu,egitimdurumu,egitim1geliroran,egitim2geliroran,egitim3geliroran):
    gelirvergisi=gelirvergisiodemesi
    if calisanturu=="pick1":
        return ((float(gelirvergisi)))
    if calisanturu=='pick2':
        if argegun==gunsayisi:
            return ((float(0)))
        else:
            return ((float(gelirvergisi)-(float(gelirvergisi)*float(argegun)/float(gunsayisi))))

    if calisanturu=="pick3":
        if egitimdurumu=="pick1":
            return ((float(gelirvergisi-float(gelirvergisi*float(egitim1geliroran)*float(argegun)/float(gunsayisi)))))

        elif egitimdurumu=="pick2":
            return ((float(gelirvergisi-float(gelirvergisi)*float(egitim2geliroran)*float(argegun)/float(gunsayisi))))

        elif egitimdurumu=="pick3":
            return ((float(gelirvergisi-float(gelirvergisi)*float(egitim3geliroran)*float(argegun)/float(gunsayisi))))
    if calisanturu=="pick4":
        return ((float(gelirvergisi)))
    if calisanturu=="pick5":
        return ((float(gelirvergisi)))
    if calisanturu=="pick6":
        return ((float(gelirvergisi)))
    if calisanturu=="pick7":
        return ((float(gelirvergisi[i])))
    if calisanturu=="pick8":
        if argegun<gunsayisi:
            return ((float(gelirvergisi)-(float(gelirvergisi)*float(argegun)/float(gunsayisi))))
        else:
            return float((0))
    if calisanturu=="pick9":
        if egitimdurumu=="pick1":
            return (((float(gelirvergisi-float(gelirvergisi*float(egitim1geliroran)*float(argegun)/float(gunsayisi))))))

        elif egitimdurumu=="pick2":
            return (((float(gelirvergisi)-float(gelirvergisi)*float(egitim2geliroran))*float(argegun)/float(gunsayisi)))

        elif egitimdurumu=="pick3":
            return (((float(gelirvergisi-float(gelirvergisi)*float(egitim3geliroran)*float(argegun)/float(gunsayisi)))))

def get_damgavergisiodemesi(calisanturu,damgavergisi,argegun,gunsayisi):

    if calisanturu=='pick1':
        return(float(damgavergisi))
    elif calisanturu=='pick2':
        if argegun==gunsayisi:
            return (float(0))
        else:
            return ((float(damgavergisi)-float(damgavergisi)*float(argegun)/float(gunsayisi)))
    elif calisanturu=='pick3':
        if argegun==gunsayisi:
            return (float(0))
        else:
            return ((float(damgavergisi)-float(damgavergisi)*float(argegun)/float(gunsayisi))) 
    elif calisanturu=='pick4':
        return (float(damgavergisi))
    elif calisanturu=='pick5':
        return (float(damgavergisi))
    elif calisanturu=='pick6':
        return (float(damgavergisi))
    elif calisanturu=='pick7':
        return (float(damgavergisi))
    elif calisanturu=='pick8':
        if argegun==gunsayisi:
            return (float(0))
        else:
            return ((float(damgavergisi)-float(damgavergisi)*float(argegun)/float(gunsayisi)))
    elif calisanturu=='pick9':
        if argegun==gunsayisi:
            return(float(0))
        else:
            return ((float(damgavergisi)-float(damgavergisi)*float(argegun)/float(gunsayisi)))

def get_indirimsizdamgavergisi(brut,damgavergiorani):
    return((float(brut)*float(damgavergiorani)))

def get_damgaistisnasi(damgavergisi,indirimsizdamgavergisi):
    indirimsiz=indirimsizdamgavergisi
    return ((float(indirimsiz)-float(damgavergisi)))

def get_toplammaliyet1(netucret,sgk,gelirvergisi,damgavergisi):
    return ((float(netucret)+float(sgk)+float(gelirvergisi)+float(damgavergisi)))

def get_asgaridensonragelirvergisiistisnasi(calisanturu,gelirvergisi,gunsayisi,argegun,egitim1geliroran,egitim2geliroran,egitim3geliroran,egitimdurumu):


    if calisanturu=="pick1":
        
            return((float(0)))
    if calisanturu=='pick2':
            
            if float(argegun)==float(gunsayisi):
                
                
                return ((float(gelirvergisi)))
               
            else:
                return (((float(gelirvergisi)*float(argegun)/float(gunsayisi))))
                
                

    if calisanturu=="pick3":
        if egitimdurumu=="pick1":
               if float(argegun)==0 :
                    return ((float(gelirvergisi)*float(egitim1geliroran)/float(gunsayisi)))
               else:
                     return ((float(gelirvergisi)*float(egitim1geliroran)*float(argegun)/float(gunsayisi)))

        elif egitimdurumu=="pick2":
                if float(argegun)==0 :
                     return ((float(gelirvergisi)*float(egitim1geliroran)/float(gunsayisi)))
                else:
                     return ((float(gelirvergisi)*float(egitim2geliroran)*float(argegun)/float(gunsayisi)))

        elif egitimdurumu=="pick3":
                if float(argegun)==0 :
                     return ((float(gelirvergisi)*float(egitim1geliroran)/float(gunsayisi)))
                else:
                     return ((float(gelirvergisi)*float(egitim3geliroran)*float(argegun)/float(gunsayisi)))
    if calisanturu=="pick4":
            return ((float(0)))
    if calisanturu=="pick5":
            return ((float(0)))
    if calisanturu=="pick6":
            return ((float(0)))
    if calisanturu=="pick7":
            return ((float(0)))
    if calisanturu=="pick8":
            if argegun<gunsayisi:
                if float(argegun)==0 :
                     return ((float(gelirvergisi)*float(egitim1geliroran)/float(gunsayisi)))
                else:
                
                    return (((float(gelirvergisi)*float(argegun)/float(gunsayisi))))
            else:
                
                    return ((gelirvergisi))
    if calisanturu=="pick9":
        if egitimdurumu=="pick1":
               if float(argegun)==0 :
                     return ((float(gelirvergisi)*float(egitim1geliroran)/float(gunsayisi)))
               else:
                     return (((float(gelirvergisi*float(egitim1geliroran)*float(argegun)/float(gunsayisi)))))

        elif egitimdurumu=="pick2":
                if float(argegun)==0 :
                    return ((float(gelirvergisi)*float(egitim1geliroran)/float(gunsayisi)))
                else:
                    return (((float(gelirvergisi)*float(egitim2geliroran))*float(argegun)/float(gunsayisi)))

        elif egitimdurumu=="pick3":
                if float(argegun)==0 :
                     return ((float(gelirvergisi)*float(egitim1geliroran)/float(gunsayisi)))
                else:
                     return (((float(gelirvergisi)*float(egitim3geliroran)*float(argegun)/float(gunsayisi))))

def get_asgaridensonradamgavergisiistisnasi(calisanturu,argegun,gunsayisi,damgavergisi):


    if calisanturu=='pick1':
            return (float(0))
    elif calisanturu=='pick2':
            if argegun==gunsayisi:
                return (float(damgavergisi))
            else:
                
                if float(argegun)==0:
                    
                    
                    return ((float(0)))
                else:
                    
                    return ((float(damgavergisi)*float(argegun)/float(gunsayisi)))
    elif calisanturu=='pick3':
            if argegun==gunsayisi:
                return (float(damgavergisi))
                
            else:

                if float(argegun)==0:
                    
                    return ((float(0)))
                else:
                    
                    return ((float(damgavergisi)*float(argegun)/float(gunsayisi))) 
    elif calisanturu=='pick4':
            return (float(0))
    elif calisanturu=='pick5':
            return (float(0))
    elif calisanturu=='pick6':
            return (float(0))
    elif calisanturu=='pick7':
            return (float(0))
    elif calisanturu=='pick8':
            if argegun==gunsayisi:
                return (float(damgavergisi))
            else:
                if argegun==0:
                    return ((float(0)))
                else:
                    return ((float(damgavergisi)*float(argegun)/float(gunsayisi)))
    elif calisanturu=='pick9':
            if argegun==gunsayisi:
                return (float(damgavergisi))
            else:
                if argegun==0:
                    return ((float(0)))
                else:
                    return ((float(damgavergisi)*float(argegun)/float(gunsayisi)))

    
  