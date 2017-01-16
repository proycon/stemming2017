FAKE_SEATS_PER_PARTY = {'vnl': 2, 'gl': 11, 'vvd': 32, 'cu': 3, 'cda': 6, 'pvdd': 1, 'pvda': 22, 'denk': 17, '50plus': 3, 'sp': 7,
             'pvv': 31, 'd66': 12, 'ppnl': 0, 'sgp': 3}

FAKE_HISTORY_OF_PARTY_MENTIONS_PERCENTAGES = {'20161218': {'vnl': 0.7916402786573781, 'gl': 22.67257758074731, 'vvd': 12.713742875237491,
                      'cu': 1.0449651678277392, 'cda': 2.6124129195693477, 'pvdd': 0.506649778340722,
                      'pvda': 11.510449651678277, 'denk': 6.918936035465484, '50plus': 1.1399620012666245,
                      'sp': 6.016466117796074, 'pvv': 19.300189993666876, 'd66': 14.075364154528183,
                      'ppnl': 0.04749841671944269, 'sgp': 0.64914502849905},
         '20161207': {'vnl': 1.5661491963181755, 'gl': 7.3224344003297155, 'vvd': 21.80244539085039,
                      'cu': 2.1706278334936115, 'cda': 4.327517516142327, 'pvdd': 1.5661491963181755,
                      'pvda': 17.48866602555296, 'denk': 8.778678389888722, '50plus': 2.5965105096853964,
                      'sp': 4.121445253468883, 'pvv': 16.884187388377523, 'd66': 9.795301552411045,
                      'ppnl': 0.05495260337958511, 'sgp': 1.5249347437834868},
         '20161203': {'vnl': 5.218525766470972, 'gl': 7.8277886497064575, 'vvd': 13.470319634703197,
                      'cu': 2.0221787345075017, 'cda': 2.756033920417482, 'pvdd': 1.304631441617743,
                      'pvda': 18.88454011741683, 'denk': 7.811480756686236, '50plus': 1.2557077625570776,
                      'sp': 4.158512720156556, 'pvv': 27.511415525114156, 'd66': 7.02870189171559,
                      'ppnl': 0.08153946510110893, 'sgp': 0.6686236138290933},
         '20161205': {'vnl': 3.6947929197456606, 'gl': 6.255370338546142, 'vvd': 16.0336827633614,
                      'cu': 1.5810276679841897, 'cda': 2.835538752362949, 'pvdd': 1.1857707509881423,
                      'pvda': 18.766111015638426, 'denk': 9.709572091424644, '50plus': 1.890359168241966,
                      'sp': 5.344560921120467, 'pvv': 23.268602852723834, 'd66': 8.248840006874033,
                      'ppnl': 0.10311050008592541, 'sgp': 1.082660250902217},
         '20161229': {'vnl': 0.9694619486185168, 'gl': 6.7135239941832285, 'vvd': 13.354338342220068,
                      'cu': 1.793504604944256, 'cda': 4.0475036354823075, 'pvdd': 0.9209888511875909,
                      'pvda': 10.033931168201647, 'denk': 18.54095976732913, '50plus': 1.2845370819195348,
                      'sp': 5.06543868153175, 'pvv': 29.035385361124575, 'd66': 6.834706737760543,
                      'ppnl': 0.290838584585555, 'sgp': 1.1148812409112943},
         '20161219': {'vnl': 2.3714094856379426, 'gl': 16.182364729458918, 'vvd': 11.239144956579826,
                      'cu': 1.7535070140280562, 'cda': 3.9746158984635938, 'pvdd': 0.501002004008016,
                      'pvda': 12.040748162992651, 'denk': 9.802939211756847, '50plus': 3.4402137608550434,
                      'sp': 3.9746158984635938, 'pvv': 18.37007348029392, 'd66': 15.464261857047429,
                      'ppnl': 0.050100200400801605, 'sgp': 0.8350033400133601},
         '20161226': {'vnl': 1.3198944084473243, 'gl': 5.567554595632349, 'vvd': 31.005519558435324,
                      'cu': 2.567794576433885, 'cda': 3.2157427405807537, 'pvdd': 0.9599232061435086,
                      'pvda': 12.239020878329734, 'denk': 10.943124550035996, '50plus': 1.3678905687544995,
                      'sp': 3.8636909047276218, 'pvv': 19.678425725941924, 'd66': 5.759539236861051,
                      'ppnl': 0.023998080153587713, 'sgp': 1.4878809695224382},
         '20161216': {'vnl': 1.8257956448911223, 'gl': 7.403685092127303, 'vvd': 20.65326633165829,
                      'cu': 2.3283082077051924, 'cda': 7.671691792294808, 'pvdd': 0.6365159128978225,
                      'pvda': 14.90787269681742, 'denk': 8.006700167504187, '50plus': 1.0217755443886096,
                      'sp': 4.924623115577889, 'pvv': 16.381909547738694, 'd66': 12.73031825795645,
                      'ppnl': 0.23450586264656617, 'sgp': 1.273031825795645},
         '20161204': {'vnl': 2.9183483390251475, 'gl': 12.791058677429369, 'vvd': 11.0835144365104,
                      'cu': 1.3660353927351754, 'cda': 2.545793231915554, 'pvdd': 1.7696367587705681,
                      'pvda': 15.864638311083514, 'denk': 7.932319155541757, '50plus': 5.324433405774604,
                      'sp': 4.641415709407016, 'pvv': 25.02328469419435, 'd66': 7.947842285004657,
                      'ppnl': 0.09313877677739832, 'sgp': 0.6985408258304874},
         '20161212': {'vnl': 1.161680458306811, 'gl': 6.1903246339910885, 'vvd': 17.05919796308084,
                      'cu': 1.893698281349459, 'cda': 5.569700827498409, 'pvdd': 1.0184595798854232,
                      'pvda': 26.11394016549968, 'denk': 7.558879694462126, '50plus': 3.0872056015276894,
                      'sp': 5.315085932527053, 'pvv': 17.886696371737745, 'd66': 5.665181413112667,
                      'ppnl': 0.11139401654996817, 'sgp': 1.3685550604710375},
         '20161206': {'vnl': 2.297200287150036, 'gl': 6.819813352476669, 'vvd': 15.68557071069634,
                      'cu': 2.4527398899258195, 'cda': 6.185690356544628, 'pvdd': 1.1246709739172052,
                      'pvda': 16.846135439100262, 'denk': 9.176836563771237, '50plus': 8.566642737497009,
                      'sp': 5.587461115099306, 'pvv': 16.870064608758074, 'd66': 6.903565446279014,
                      'ppnl': 0.059822924144532184, 'sgp': 1.423785594639866},
         '20161209': {'vnl': 0.7407407407407407, 'gl': 4.0, 'vvd': 8.962962962962964, 'cu': 0.9537037037037037,
                      'cda': 2.4166666666666665, 'pvdd': 0.5462962962962963, 'pvda': 38.49074074074074,
                      'denk': 5.666666666666667, '50plus': 0.6666666666666666, 'sp': 3.3333333333333335,
                      'pvv': 25.99074074074074, 'd66': 7.435185185185185, 'ppnl': 0.027777777777777776,
                      'sgp': 0.7685185185185185},
         '20161227': {'vnl': 1.3269904857285928, 'gl': 5.332999499248873, 'vvd': 18.5778668002003,
                      'cu': 2.3535302954431647, 'cda': 3.4051076614922384, 'pvdd': 0.901352028042063,
                      'pvda': 20.68102153229845, 'denk': 13.495242864296445, '50plus': 1.101652478718077,
                      'sp': 5.533299949924888, 'pvv': 19.42914371557336, 'd66': 6.584877315973961,
                      'ppnl': 0.0500751126690035, 'sgp': 1.226840260390586},
         '20161208': {'vnl': 1.1610598392378684, 'gl': 7.3682643643941645, 'vvd': 19.17237272997916,
                      'cu': 2.5900565644537066, 'cda': 5.730872283417684, 'pvdd': 0.967549866031557,
                      'pvda': 17.490324501339686, 'denk': 9.080083358142303, '50plus': 1.0568621613575468,
                      'sp': 5.269425424233403, 'pvv': 19.767788032152428, 'd66': 8.559094968740697,
                      'ppnl': 0.1637392080976481, 'sgp': 1.6225066984221495},
         '20161213': {'vnl': 0.8783297336213103, 'gl': 7.501799856011519, 'vvd': 18.833693304535636,
                      'cu': 1.4974802015838733, 'cda': 6.897048236141108, 'pvdd': 2.275017998560115,
                      'pvda': 20.187185025197984, 'denk': 7.012239020878329, '50plus': 1.42548596112311,
                      'sp': 5.385169186465083, 'pvv': 18.94888408927286, 'd66': 7.717782577393809,
                      'ppnl': 0.18718502519798416, 'sgp': 1.2526997840172787},
         '20161202': {'vnl': 1.108748481166464, 'gl': 7.351154313487242, 'vvd': 13.699878493317133,
                      'cu': 2.5668286755771565, 'cda': 3.44775212636695, 'pvdd': 1.3669501822600243,
                      'pvda': 23.769744835965977, 'denk': 8.945929526123937, '50plus': 0.9264884568651276,
                      'sp': 4.389428918590522, 'pvv': 21.74969623329283, 'd66': 9.492709599027947,
                      'ppnl': 0.106318347509113, 'sgp': 1.0783718104495748},
         '20161215': {'vnl': 1.4729761076316399, 'gl': 12.816051960102065, 'vvd': 23.2776617954071,
                      'cu': 2.632799814428207, 'cda': 8.75666898631408, 'pvdd': 0.6147065646021804,
                      'pvda': 10.183252145673858, 'denk': 6.726977499420088, '50plus': 0.9626536766411505,
                      'sp': 5.787520296914869, 'pvv': 16.109951287404314, 'd66': 9.382973787984227,
                      'ppnl': 0.1507770818835537, 'sgp': 1.12502899559267},
         '20161230': {'vnl': 1.3826043237807943, 'gl': 7.290095525389643, 'vvd': 13.59979889391654,
                      'cu': 2.890899949723479, 'cda': 4.047259929612871, 'pvdd': 1.4328808446455505,
                      'pvda': 13.926596279537456, 'denk': 17.747611865258925, '50plus': 1.583710407239819,
                      'sp': 5.304172951231775, 'pvv': 21.367521367521366, 'd66': 7.46606334841629,
                      'ppnl': 0.10055304172951232, 'sgp': 1.860231271995978},
         '20161214': {'vnl': 0.8882907133243607, 'gl': 4.939434724091521, 'vvd': 15.235531628532975,
                      'cu': 1.911170928667564, 'cda': 5.006729475100942, 'pvdd': 1.1036339165545088,
                      'pvda': 15.88156123822342, 'denk': 5.841184387617766, '50plus': 1.117092866756393,
                      'sp': 22.005383580080753, 'pvv': 16.985195154777927, 'd66': 7.806191117092867,
                      'ppnl': 0.1480484522207268, 'sgp': 1.1305518169582773},
         '20161222': {'vnl': 1.0299166257969592, 'gl': 6.016020925290175, 'vvd': 11.819519372241295,
                      'cu': 2.713748569560242, 'cda': 4.69184240640837, 'pvdd': 1.177047572339382,
                      'pvda': 33.05541932319765, 'denk': 7.6835049861043, '50plus': 0.7683504986104299,
                      'sp': 4.185058034984469, 'pvv': 16.838319437632826, 'd66': 8.321072421121464,
                      'ppnl': 0.0980872976949485, 'sgp': 1.6020925290174923},
         '20161201': {'vnl': 1.5625, 'gl': 7.630813953488372, 'vvd': 18.011143410852714, 'cu': 3.5973837209302326,
                      'cda': 3.137112403100775, 'pvdd': 2.0954457364341086, 'pvda': 24.76986434108527,
                      'denk': 8.357558139534884, '50plus': 0.7873062015503876, 'sp': 3.6458333333333335,
                      'pvv': 15.95203488372093, 'd66': 9.314437984496124, 'ppnl': 0.060562015503875966,
                      'sgp': 1.0780038759689923},
         '20161231': {'vnl': 1.8468871015787907, 'gl': 6.523681858802502, 'vvd': 12.272862675007447,
                      'cu': 2.621388144176348, 'cda': 3.3363121834971703, 'pvdd': 0.7447125409591897,
                      'pvda': 20.196604110813226, 'denk': 17.515638963360143, '50plus': 1.0425975573428656,
                      'sp': 4.915102770330653, 'pvv': 19.273160560023832, 'd66': 7.447125409591898, 'ppnl': 0.0,
                      'sgp': 2.2639261245159368},
         '20161223': {'vnl': 0.9993482511405605, 'gl': 7.51683684553552, 'vvd': 23.484683901803173,
                      'cu': 2.368020855963502, 'cda': 4.149467738431458, 'pvdd': 0.6082989354768629,
                      'pvda': 19.03106669563328, 'denk': 8.08168585704975, '50plus': 1.06452313708451,
                      'sp': 4.714316749945688, 'pvv': 18.37931783619379, 'd66': 8.0165109711058,
                      'ppnl': 0.15207473386921572, 'sgp': 1.4338474907668912},
         '20161224': {'vnl': 0.9042613315248107, 'gl': 3.809200859048265, 'vvd': 8.884367582231265,
                      'cu': 2.1702271956595456, 'cda': 1.6389736633887193, 'pvdd': 0.508646998982706,
                      'pvda': 7.3697298519272065, 'denk': 59.398666214536, '50plus': 0.6894992652876681,
                      'sp': 1.7407030631852605, 'pvv': 9.121736181756528, 'd66': 2.938849327455635,
                      'ppnl': 0.011303266644060133, 'sgp': 0.8138351983723296},
         '20161211': {'vnl': 3.1491635034443974, 'gl': 6.565443554055954, 'vvd': 13.201180936313792,
                      'cu': 1.0965837199493884, 'cda': 3.1351047378040207, 'pvdd': 0.7591733445803458,
                      'pvda': 19.991564740615775, 'denk': 7.690144805286096, '50plus': 3.8380430198228597,
                      'sp': 5.750035146914101, 'pvv': 26.10712779417967, 'd66': 7.296499367355546,
                      'ppnl': 0.07029382820188387, 'sgp': 1.3496415014761705},
         '20170103': {'vnl': 0.8970886932972241, 'gl': 5.26404874746107, 'vvd': 36.47596479350034,
                      'cu': 1.6418415707515233, 'cda': 3.3683141503046716, 'pvdd': 0.7786052809749492,
                      'pvda': 11.408259986459038, 'denk': 6.838185511171293, '50plus': 2.064996614759648,
                      'sp': 3.3513879485443465, 'pvv': 16.130670277589708, 'd66': 9.055517941773866,
                      'ppnl': 0.05077860528097495, 'sgp': 2.6743398781313474},
         '20170102': {'vnl': 1.0909935004642526, 'gl': 7.404828226555246, 'vvd': 16.759517177344474,
                      'cu': 1.6945218198700094, 'cda': 6.7780872794800375, 'pvdd': 1.0677808727948004,
                      'pvda': 18.175487465181057, 'denk': 8.681522748375116, '50plus': 3.806870937790158,
                      'sp': 5.617455896007428, 'pvv': 19.382544103992572, 'd66': 7.938718662952646,
                      'ppnl': 0.04642525533890436, 'sgp': 1.5552460538532962},
         '20170105': {'vnl': 2.595573440643863, 'gl': 7.10261569416499, 'vvd': 22.3943661971831,
                      'cu': 2.5754527162977867, 'cda': 4.527162977867203, 'pvdd': 0.8048289738430584,
                      'pvda': 16.599597585513077, 'denk': 7.766599597585513, '50plus': 2.9979879275653922,
                      'sp': 3.7022132796780682, 'pvv': 18.390342052313883, 'd66': 8.06841046277666, 'ppnl': 0.0,
                      'sgp': 2.4748490945674044},
         '20170101': {'vnl': 1.0526315789473684, 'gl': 12.81733746130031, 'vvd': 13.157894736842104,
                      'cu': 1.08359133126935, 'cda': 2.1052631578947367, 'pvdd': 0.7120743034055728,
                      'pvda': 14.303405572755418, 'denk': 12.136222910216718, '50plus': 7.863777089783282,
                      'sp': 5.7894736842105265, 'pvv': 18.390092879256965, 'd66': 9.969040247678018,
                      'ppnl': 0.030959752321981424, 'sgp': 0.5882352941176471},
         '20161220': {'vnl': 1.1545623836126628, 'gl': 10.279329608938548, 'vvd': 11.831160769708255,
                      'cu': 8.45437616387337, 'cda': 7.49844816883923, 'pvdd': 0.9931719428926132,
                      'pvda': 13.320918684047175, 'denk': 5.661080074487896, '50plus': 2.2346368715083798,
                      'sp': 4.419615145872129, 'pvv': 19.428926132836747, 'd66': 12.625698324022347,
                      'ppnl': 0.04965859714463067, 'sgp': 2.0484171322160147},
         '20161210': {'vnl': 1.061084026383711, 'gl': 5.291081158589045, 'vvd': 12.675652423286493,
                      'cu': 1.1901347863492975, 'cda': 2.6383710926297677, 'pvdd': 0.6595927731574419,
                      'pvda': 24.82076283338113, 'denk': 7.513622024663034, '50plus': 7.8004014912532265,
                      'sp': 3.398336679093777, 'pvv': 23.501577287066247, 'd66': 7.8004014912532265,
                      'ppnl': 0.11471178663607685, 'sgp': 1.534270146257528},
         '20161225': {'vnl': 1.1405959031657356, 'gl': 4.934823091247672, 'vvd': 29.376163873370576,
                      'cu': 1.3500931098696463, 'cda': 2.164804469273743, 'pvdd': 0.5121042830540037,
                      'pvda': 9.986033519553073, 'denk': 15.363128491620111, '50plus': 0.861266294227188,
                      'sp': 2.723463687150838, 'pvv': 25.349162011173185, 'd66': 5.0512104283054, 'ppnl': 0.0,
                      'sgp': 1.187150837988827},
         '20161217': {'vnl': 0.9909820632246557, 'gl': 37.89515409771083, 'vvd': 15.241304132395204,
                      'cu': 1.3477356059855317, 'cda': 3.0224952928352, 'pvdd': 0.6144088791992864,
                      'pvda': 13.477356059855317, 'denk': 3.91437914973739, '50plus': 0.7729660093152314,
                      'sp': 3.0720443959964325, 'pvv': 14.498067584976711, 'd66': 4.330591616291745,
                      'ppnl': 0.11891784758695867, 'sgp': 0.7035972648895055},
         '20161228': {'vnl': 1.6040329972502292, 'gl': 7.126489459211732, 'vvd': 14.848762603116407,
                      'cu': 1.6040329972502292, 'cda': 3.758020164986251, 'pvdd': 0.7103574702108157,
                      'pvda': 13.496791934005499, 'denk': 11.228230980751604, '50plus': 2.5664527956003664,
                      'sp': 4.674610449129239, 'pvv': 29.537121906507792, 'd66': 7.401466544454629,
                      'ppnl': 0.1604032997250229, 'sgp': 1.2832263978001832},
         '20170104': {'vnl': 1.2767368595589454, 'gl': 7.776488144586304, 'vvd': 33.11225335765213,
                      'cu': 1.65809981760902, 'cda': 5.836511357983751, 'pvdd': 1.7078428121372906,
                      'pvda': 11.988061681313216, 'denk': 6.085226330625104, '50plus': 0.7129829215718786,
                      'sp': 2.885093682639695, 'pvv': 17.36030509036644, 'd66': 6.930857237605704,
                      'ppnl': 0.0497429945282706, 'sgp': 2.6197977118222515},
         '20161221': {'vnl': 1.8054672600127146, 'gl': 6.687857596948506, 'vvd': 14.939605848696758,
                      'cu': 3.4710743801652892, 'cda': 8.150031786395422, 'pvdd': 0.775588048315321,
                      'pvda': 22.28862047043865, 'denk': 5.657978385251113, '50plus': 1.042593769866497,
                      'sp': 4.589955499046408, 'pvv': 20.228862047043865, 'd66': 9.141767323585505,
                      'ppnl': 0.0508582326764145, 'sgp': 1.1697393515575334}}