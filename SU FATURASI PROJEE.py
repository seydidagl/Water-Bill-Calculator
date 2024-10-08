
while True:
        konut1_abone_say = 0
        konut2_abone_say = 0
        konut3_abone_say = 0
        konut_abone_say = konut1_abone_say + konut2_abone_say + konut3_abone_say
        isyeri_abone_say = 0
        resmi_abone_say = 0
        organize_abone_say = 0
        ilce1_tarımsal__abone_say = 0
        ilce2_tarımsal_abone_say = 0
        ilce3_tarımsal_abone_say = 0
        ilce_tarımsal_abone_say = 0
        toplam_abone_say = konut_abone_say + isyeri_abone_say + resmi_abone_say + organize_abone_say + ilce_tarımsal_abone_say
        yüz_veya_beşyüz = 0
        elli_ve_ilce = 0
        yüksek_resmi = 0
        yüksek_konut_olmayan = 0
        bornova_su_tuketim = 0
        konut1_tuketim = 0
        konut2_tuketim = 0
        konut3_tuketim = 0
        konut_tuketim = konut1_tuketim + konut2_tuketim + konut3_tuketim
        isyeri_tuketim = 0
        resmi_tuketim = 0
        organize_tuketim = 0
        ilce1_tuketim = 0
        ilce2_tuketim = 0
        ilce3_tuketim = 0
        ilce_tuketim = ilce1_tuketim + ilce2_tuketim + ilce3_tuketim
        konut_tuketim_ucret = 0
        isyeri_tuketim_ucret = 0
        resmi_tuketim_ucret = 0
        organize_tuketim_ucret = 0
        ilce_tuketim_ucret = 0
        abone_no=input("Abone numarasını giriniz:")
        abone_tipi_kodu=int(input("Abone tipi kodunu giriniz:[1,5]"))
        while abone_tipi_kodu>5 or abone_tipi_kodu<1:
                abone_tipi_kodu=int(input("Abone tipi kodunu tekrar giriniz:"))
                if 1<=abone_tipi_kodu<=5:
                    break
        onceki_sayac_degeri=int(input("Önceki sayaç değerini giriniz (0 ya da 0'dan büyük):"))
        while onceki_sayac_degeri<0:
             onceki_sayac_degeri=int(input("Önceki sayaç değerini tekrar giriniz:"))
             if 0<=onceki_sayac_degeri:
                 break
        simdiki_sayac_degeri=int(input("Şimdiki sayaç değerini giriniz(Öncekinden büyük ya da eşit):"))
        while simdiki_sayac_degeri<onceki_sayac_degeri:
            simdiki_sayac_degeri=int(input("Şimdiki sayaç değerini tekrar giriniz:"))
            if simdiki_sayac_degeri>=onceki_sayac_degeri:
                break
        su_tuketim =simdiki_sayac_degeri-onceki_sayac_degeri
        su_tuketim_ucret = 0
        atık_su_ucret = 0
        sayac_okuma_gün=int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısı: tamsayı (0’dan büyük) "))
        while sayac_okuma_gün<=0:
            sayac_okuma_gün=int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını tekrar giriniz"))
            if sayac_okuma_gün>0:
                break
        hane_sayısı = int(input("Hane sayısını giriniz(1 ya da 1'den büyük):"))
        while hane_sayısı < 1:
            hane_sayısı = int(input("Hane sayısını tekrar giriniz:"))
            if 1 <= hane_sayısı:
                break
        if abone_tipi_kodu==1:
            abone_tipi_adı="Konut"
            if  hane_sayısı==1:
                indirim_durumu = input("Şehit,Gazi,Sporcu veya Engelli olduğunu belirtiniz(SGS/E/Yok):")
                if 0<=su_tuketim<=(sayac_okuma_gün/30)*13:
                    konut1_abone_say+=1
                    konut1_tuketim += su_tuketim
                    if indirim_durumu=="SGS" or indirim_durumu=="E":
                        su_tuketim_ucret+=su_tuketim*2.89/2
                        atık_su_ucret+=su_tuketim*1.44/2
                    else:
                        su_tuketim_ucret+=su_tuketim * 2.89
                        atık_su_ucret+=su_tuketim * 1.44
                elif 14*(sayac_okuma_gün/30)<=su_tuketim<=(sayac_okuma_gün/30)*20:
                    konut2_abone_say+=1
                    konut2_tuketim+=su_tuketim
                    if  indirim_durumu=="SGS" or indirim_durumu=="E":
                             su_tuketim_ucret+=(sayac_okuma_gün/30)*13*2.89/2
                             su_tuketim_ucret+=(su_tuketim-((sayac_okuma_gün/30)*13))*3.13/2
                             atık_su_ucret+=(sayac_okuma_gün/30)*13*1.44/2
                             atık_su_ucret+=(su_tuketim-((sayac_okuma_gün/30)*13))*1.56/2
                    else:
                          su_tuketim_ucret += (sayac_okuma_gün / 30) * 13 * 2.89
                          su_tuketim_ucret += (su_tuketim - ((sayac_okuma_gün / 30) * 13)) * 3.13
                          atık_su_ucret += (sayac_okuma_gün / 30) * 13 * 1.44
                          atık_su_ucret += (su_tuketim - ((sayac_okuma_gün / 30) * 13)) * 1.56
                elif  21*(sayac_okuma_gün/30)<=su_tuketim :
                    konut3_abone_say+=1
                    konut3_tuketim+=su_tuketim
                    if indirim_durumu=="SGS":
                        su_tuketim_ucret += (sayac_okuma_gün / 30) * 13 * 2.89 / 2
                        su_tuketim_ucret+=(sayac_okuma_gün / 30) * 7 *3.13 /2
                        su_tuketim_ucret+=(su_tuketim-((sayac_okuma_gün/30)*20))*6.43 /2
                        atık_su_ucret += (sayac_okuma_gün / 30) * 13 * 1.44 / 2
                        atık_su_ucret+=(sayac_okuma_gün / 30) * 7 *1.56/2
                        atık_su_ucret+=(su_tuketim-((sayac_okuma_gün/30)*20))*3.22 /2
                    else:
                        su_tuketim_ucret += (sayac_okuma_gün / 30) * 13 * 2.89
                        su_tuketim_ucret += (sayac_okuma_gün / 30) * 7 * 3.13
                        su_tuketim_ucret+=(su_tuketim-((sayac_okuma_gün/30)*20))* 6.43
                        atık_su_ucret += (sayac_okuma_gün / 30) * 13 * 1.44
                        atık_su_ucret += (sayac_okuma_gün / 30) * 7 * 1.56
                        atık_su_ucret+=(su_tuketim-((sayac_okuma_gün/30)*20))* 3.22
            elif 1<hane_sayısı:
                sehit_gazi_sporcu_say = int(input("Şehit,gazi ve sporcu sayısını giriniz(ŞGS):"))
                while sehit_gazi_sporcu_say < 0 or hane_sayısı < sehit_gazi_sporcu_say:
                    sehit_gazi_sporcu_say = int(input("Şehit,gazi ve sporcu sayısını tekrar giriniz"))
                    if 0 < sehit_gazi_sporcu_say < hane_sayısı:
                        break
                engelli_say = int(input("Engelli sayısını giriniz:"))
                while engelli_say < 0 or hane_sayısı < engelli_say:
                    engelli_say = int(input("Engelli sayısını tekrar giriniz"))
                    if 0<engelli_say<hane_sayısı:
                        break
                while 0 <= (su_tuketim/hane_sayısı) <= (sayac_okuma_gün / 30) * 13:
                     konut1_abone_say+=hane_sayısı
                     konut1_tuketim+=su_tuketim
                     su_tuketim_ucret+=(sehit_gazi_sporcu_say+engelli_say)*2.89*(su_tuketim/hane_sayısı)/2
                     su_tuketim_ucret+=(hane_sayısı-(sehit_gazi_sporcu_say+engelli_say))*2.89*(su_tuketim/hane_sayısı)
                     atık_su_ucret+=(sehit_gazi_sporcu_say+engelli_say)*1.44*(su_tuketim/hane_sayısı)/2
                     atık_su_ucret+=(hane_sayısı-(sehit_gazi_sporcu_say+engelli_say))*1.44*(su_tuketim/hane_sayısı)
                while 14 * (sayac_okuma_gün / 30) <= (su_tuketim/hane_sayısı) <= (sayac_okuma_gün / 30) * 20:
                    konut2_abone_say+=hane_sayısı
                    konut2_tuketim+=su_tuketim
                    su_tuketim_ucret += (sehit_gazi_sporcu_say + engelli_say) *2.89* (sayac_okuma_gün / 30) * 13 / 2
                    su_tuketim_ucret += (hane_sayısı - (sehit_gazi_sporcu_say + engelli_say))*2.89 *(sayac_okuma_gün / 30) * 13
                    su_tuketim_ucret+=((su_tuketim / hane_sayısı)-((sayac_okuma_gün /30) * 13))*3.13*(sehit_gazi_sporcu_say+engelli_say)/2
                    su_tuketim_ucret+=((su_tuketim / hane_sayısı)-((sayac_okuma_gün /30) * 13))*3.13*(hane_sayısı-(sehit_gazi_sporcu_say+engelli_say))
                    atık_su_ucret += (sehit_gazi_sporcu_say + engelli_say) *1.44* (sayac_okuma_gün / 30) * 13 / 2
                    atık_su_ucret += (hane_sayısı - (sehit_gazi_sporcu_say + engelli_say)) *1.44* (sayac_okuma_gün / 30) * 13
                    atık_su_ucret+=((su_tuketim / hane_sayısı)-((sayac_okuma_gün /30) * 13))*1.56*(sehit_gazi_sporcu_say+engelli_say)/2
                    atık_su_ucret+=((su_tuketim / hane_sayısı)-((sayac_okuma_gün /30) * 13))*1.56*(hane_sayısı-(sehit_gazi_sporcu_say+engelli_say))
                while 21 * (sayac_okuma_gün / 30) <= (su_tuketim/hane_sayısı):
                    konut3_abone_say+=hane_sayısı
                    konut3_tuketim+=su_tuketim
                    su_tuketim_ucret += (sehit_gazi_sporcu_say + engelli_say) * (sayac_okuma_gün / 30) *2.89* 13 / 2
                    su_tuketim_ucret += (sehit_gazi_sporcu_say + engelli_say) *(sayac_okuma_gün / 30) *3.13* 7/2
                    su_tuketim_ucret += (hane_sayısı - (sehit_gazi_sporcu_say + engelli_say)) * (sayac_okuma_gün / 30) *2.89* 13
                    su_tuketim_ucret += (hane_sayısı - (sehit_gazi_sporcu_say + engelli_say)) * (sayac_okuma_gün / 30) *3.13* 7
                    su_tuketim_ucret+=((su_tuketim / hane_sayısı)-((sayac_okuma_gün / 30)*20))*6.43*(sehit_gazi_sporcu_say)/2
                    su_tuketim_ucret+=((su_tuketim / hane_sayısı)-((sayac_okuma_gün / 30) *20))*6.43*(hane_sayısı-(sehit_gazi_sporcu_say))
                    atık_su_ucret += (sehit_gazi_sporcu_say + engelli_say) * (sayac_okuma_gün / 30) *1.44* 13 / 2
                    atık_su_ucret += (sehit_gazi_sporcu_say + engelli_say) *(sayac_okuma_gün / 30) *1.56* 7/2
                    atık_su_ucret += (hane_sayısı - (sehit_gazi_sporcu_say + engelli_say)) * (sayac_okuma_gün / 30) *1.44* 13
                    atık_su_ucret += (hane_sayısı - (sehit_gazi_sporcu_say + engelli_say)) * (sayac_okuma_gün / 30) * 1.56*7
                    atık_su_ucret+=((su_tuketim / hane_sayısı)-((sayac_okuma_gün / 30)*20))*3.22*(sehit_gazi_sporcu_say)/2
                    atık_su_ucret+=((su_tuketim / hane_sayısı)-((sayac_okuma_gün / 30) *20))*3.22*(hane_sayısı-(sehit_gazi_sporcu_say))
            konut_tuketim_ucret += su_tuketim_ucret
        elif abone_tipi_kodu==2:
            abone_tipi_adı="İşyeri"
            isyeri_abone_say += 1
            isyeri_tuketim+=su_tuketim
            su_tuketim_ucret+=su_tuketim*7.38
            atık_su_ucret+=su_tuketim_ucret*3.68
            isyeri_tuketim_ucret+=su_tuketim_ucret

        elif abone_tipi_kodu==3:
            abone_tipi_adı="Resmi Daire"
            resmi_abone_say+=1
            resmi_tuketim+=su_tuketim
            su_tuketim_ucret+=su_tuketim*4.34
            atık_su_ucret+=su_tuketim*2.16
            resmi_tuketim_ucret+=su_tuketim_ucret
        elif abone_tipi_kodu==4:
            abone_tipi_adı="Organize Sanayi"
            organize_abone_say+=1
            organize_tuketim+=su_tuketim
            su_tuketim_ucret+=su_tuketim*5
            atık_su_ucret+=su_tuketim*2.5
            organize_tuketim_ucret+=su_tuketim_ucret
        else:
            abone_tipi_adı="İlçe Tarımsal ve Hayvan Sulama"
            ilce_tarımsal_abone_say+=1
            if 0<=su_tuketim<=(sayac_okuma_gün/30)*13:
                    ilce1_tarımsal__abone_say+=1
                    ilce1_tuketim+=su_tuketim
                    su_tuketim_ucret+=su_tuketim*1.45
                    atık_su_ucret+=su_tuketim*0.72
            elif 14*(sayac_okuma_gün/30)<=su_tuketim<=(sayac_okuma_gün / 30) * 20:
                    ilce2_tarımsal_abone_say+=1
                    ilce2_tuketim+=su_tuketim
                    su_tuketim_ucret += (sayac_okuma_gün / 30) * 13* 1.45
                    su_tuketim_ucret+=(su_tuketim-((sayac_okuma_gün/30)*13))*2.89
                    atık_su_ucret += (sayac_okuma_gün/30)*13* 0.72
                    atık_su_ucret+=(su_tuketim - ((sayac_okuma_gün / 30) * 13))*1.44
            elif 21*(sayac_okuma_gün/30)<=su_tuketim:
                    ilce3_tarımsal_abone_say+=1
                    ilce3_tuketim+=su_tuketim
                    su_tuketim_ucret += (sayac_okuma_gün / 30) * 13 * 1.45
                    su_tuketim_ucret += (sayac_okuma_gün / 30) * 7 * 2.89
                    su_tuketim_ucret+=(su_tuketim-((sayac_okuma_gün/30)*20))*6.43
                    atık_su_ucret += (sayac_okuma_gün / 30) * 13 * 0.72
                    atık_su_ucret += (sayac_okuma_gün / 30) * 7 * 1.44
                    atık_su_ucret+=(su_tuketim - ((sayac_okuma_gün / 30) * 20)) *3.22
            ilce_tuketim_ucret+=su_tuketim_ucret
        toplam_abone_say = konut_abone_say + isyeri_abone_say + resmi_abone_say + organize_abone_say + ilce_tarımsal_abone_say
        if (su_tuketim*(30/sayac_okuma_gün))>100 and (su_tuketim_ucret*(30/sayac_okuma_gün)):
            yüz_veya_beşyüz+=1
        toplam_fatura=(su_tuketim_ucret+atık_su_ucret+(hane_sayısı*13)+(hane_sayısı*2.54))*108/100+(0.39*su_tuketim)
        kdv_tutar=(su_tuketim_ucret+atık_su_ucret+(hane_sayısı*13)+(hane_sayısı*2.54))*8/100
        print("Abone no:",abone_no)
        print("Abone tipi adı:",abone_tipi_adı)
        print("Dönemlik su tüketim miktarı:",su_tuketim)
        print("Dönemlik su tüketim ücreti:",su_tuketim_ucret)
        print("Dönemlik atık su ücreti",atık_su_ucret)
        print("Dönemlik toplam su tüketim ve atık su ücreti:",atık_su_ucret+su_tuketim_ucret)
        print("Dönemlik ÇTV tutarı:",0.39*su_tuketim)
        print("Dönemlik katı atık toplama ücreti:",hane_sayısı*13)
        print("Dönemlik katı atık bertaraf ücreti:",hane_sayısı*2.54)
        print("Dönemlik toplam fatura tutarı:",toplam_fatura)
        print("Dönemlik devlete aktarılacak KDV tutarı (%8):",kdv_tutar)
        print("Dönemlik ilçe belediyesine aktarılacak tutar:",(0.39*su_tuketim)+(hane_sayısı*13))
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar:",hane_sayısı*2.54)
        print("Dönemlik İZSU payı:",atık_su_ucret+su_tuketim_ucret)
        diger_abone=input("Başka abone var mı?:(E/e/H/h)")
        if diger_abone=="H" or diger_abone=="h":
            break

if abone_tipi_kodu==1 and indirim_durumu=="SGS":
     sehit_gazi_sporcu_say+=1
elif abone_tipi_kodu==1 and indirim_durumu=="E":
     engelli_say+=1



if 0<konut_abone_say:
    print("Konut",konut_abone_say,konut_abone_say*100/toplam_abone_say,konut_tuketim*(30/sayac_okuma_gün))
    print(konut1_abone_say, konut2_abone_say, konut3_abone_say)
    print(konut1_abone_say * 100 / toplam_abone_say, konut2_abone_say * 100 / toplam_abone_say,konut3_abone_say * 100 / toplam_abone_say)
    print((konut1_tuketim / konut1_abone_say) * (30 / sayac_okuma_gün))
    print((konut2_tuketim / konut2_abone_say) * (30 / sayac_okuma_gün))
    print((konut3_tuketim / konut3_abone_say) * (30 / sayac_okuma_gün))
    print("Konut", konut_tuketim * (30 / sayac_okuma_gün))
    print("Konut", konut_tuketim / su_tuketim)
    print("Konut", konut_tuketim_ucret * (30 / sayac_okuma_gün))
    print(sehit_gazi_sporcu_say + engelli_say, (sehit_gazi_sporcu_say + engelli_say) * 100 / konut_abone_say)
elif 0<isyeri_abone_say:
    print("İşyeri", isyeri_abone_say, isyeri_abone_say * 100 / toplam_abone_say,isyeri_tuketim * (30 / sayac_okuma_gün))
    print("İşyeri", isyeri_tuketim * (30 / sayac_okuma_gün))
    print("İşyeri", isyeri_tuketim / su_tuketim)
    print("İşyeri", isyeri_tuketim_ucret * (30 / sayac_okuma_gün))
elif 0<resmi_abone_say:
    print("Resmi Daire", resmi_abone_say, resmi_abone_say * 100 / toplam_abone_say,resmi_tuketim * (30 / sayac_okuma_gün))
    print("Resmi Daire", resmi_tuketim * (30 / sayac_okuma_gün))
    print("Resmi Daire", resmi_tuketim / su_tuketim)
    print("Resmi Daire", resmi_tuketim_ucret* (30 / sayac_okuma_gün))
elif 0<organize_abone_say:
    print("Organize Sanayi", organize_abone_say * 100 / toplam_abone_say, organize_tuketim * (30 / sayac_okuma_gün))
    print("Organize Sanayi", organize_tuketim * (30 / sayac_okuma_gün))
    print("Organize Sanayi", organize_tuketim / su_tuketim)
    print("Organize Sanayi", organize_tuketim_ucret * (30 / sayac_okuma_gün))
elif 0<ilce_tarımsal_abone_say:
    print("İlçe Tarımsal ve Hayvan Sulama", ilce_tarımsal_abone_say * 100 / toplam_abone_say,ilce_tuketim * (30 / sayac_okuma_gün))
    print("İlçe Tarımsal ve Hayvan Sulama", ilce_tuketim * (30 / sayac_okuma_gün))
    print("İlçe Tarımsal ve Hayvan Sulama", ilce_tuketim / su_tuketim)
    print("İlçe Tarımsal ve Hayvan Sulama", ilce_tuketim_ucret * (30 / sayac_okuma_gün))



if (su_tuketim * (30 / sayac_okuma_gün)) > 50 and abone_tipi_kodu==5:
    elli_ve_ilce+=1
    print(elli_ve_ilce,elli_ve_ilce*100/ilce_tarımsal_abone_say)


if (su_tuketim * (30 / sayac_okuma_gün)) >100 or 500<(su_tuketim*(30/sayac_okuma_gün)):
    yüz_veya_beşyüz+=1
    print(yüz_veya_beşyüz)




print("Bornova’nın aylık toplam su tüketim miktarı:",su_tuketim*(30/sayac_okuma_gün))
print(su_tuketim_ucret*(30/sayac_okuma_gün))
print("Devlet gelir:",kdv_tutar)
print("İzsu gelir:",atık_su_ucret+su_tuketim_ucret)
print("İlçe belediyesi gelir:",(0.39*su_tuketim)+(hane_sayısı*13))
print("Büyükşehir belediyesi gelir:",hane_sayısı*2.54)




