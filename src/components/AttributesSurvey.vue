<template>
  <div class="container">
    <div class="h5">1=never  2=sometimes  3=often  4=almost always  5=always</div>
    <attribute
      v-for="attribute in attributes"
      :key="attribute.name"
      v-bind:attribute="attribute"
    ></attribute>
  </div>
</template>
<script>
import SurveyQuestion from "./SurveyQuestion";
import Attribute from "./Attribute";

export default {
  name: "AttributesSurvey",
  components: {Attribute},
  data() {
    return {
      attributes: [
        {
          name: "Faith",
          survey: [
            {
              id: 1,
              question: "I believe in Christ and accept Him as my Savior.",
              scriptureHeader: "2 Nephi 25:29",
              scripture: [
                {
                  "verse": "29",
                  "text": "And now behold, I say unto you that the right way is to believe in Christ, and deny him not; and Christ is the Holy One of Israel; wherefore ye must bow down before him, and worship him with all your might, mind, and strength, and your whole soul; and if ye do this ye shall in nowise be cast out."
                }
              ],
            },
            {
              id: 2,
              question: "I feel confident that God loves me.",
              scriptureHeader: "1 Nephi 11:17",
              scripture: [
                {
                  "verse": "17",
                  "text": "And I said unto him: I know that he loveth his children; nevertheless, I do not know the meaning of all things."
                }
              ],
            },
            {
              id: 3,
              question:
                "I trust the Savior enough to accept His will and do whatever He asks.",
              scriptureHeader: "1 Nephi 3:7",
              scripture: [
                {
                  "verse": "7",
                  "text": "And it came to pass that I, Nephi, said unto my father: I will go and do the things which the Lord hath commanded, for I know that the Lord giveth no commandments unto the children of men, save he shall prepare a way for them that they may accomplish the thing which he commandeth them."
                }
              ],
            },
            {
              id: 4,
              question:
                "I firmly believe that through the Atonement of Jesus Christ I can be forgiven of all my sins.",
              scriptureHeader: "Enos 1:5-8",
              scripture: [
                {
                  "verse": "5",
                  "text": "And there came a voice unto me, saying: Enos, thy sins are forgiven thee, and thou shalt be blessed."
                }, {
                  "verse": "6",
                  "text": "And I, Enos, knew that God could not lie; wherefore, my guilt was swept away."
                }, {
                  "verse": "7",
                  "text": "And I said: Lord, how is it done?"
                }, {
                  "verse": "8",
                  "text": "And he said unto me: Because of thy faith in Christ, whom thou hast never before heard nor seen. And many years pass away before he shall manifest himself in the flesh; wherefore, go to, thy faith hath made thee whole."
                }
              ],
            },
            {
              id: 5,
              question:
                "I have enough faith in Christ to obtain answers to my prayers.",
              scriptureHeader: "Mosiah 27:14",
              scripture: [
                {
                  "verse": "14",
                  "text": "And again, the angel said: Behold, the Lord hath heard the prayers of his people, and also the prayers of his servant, Alma, who is thy father; for he has prayed with much faith concerning thee that thou mightest be brought to the knowledge of the truth; therefore, for this purpose have I come to convince thee of the power and authority of God, that the prayers of his servants might be answered according to their faith."
                }
              ],
            },
            {
              id: 6,
              question:
                "I think about the Savior during the day and remember what He has done for me.",
              scriptureHeader: "D&C 20:77,79",
              scripture: [
                {
                  "verse": "77",
                  "text": "O God, the Eternal Father, we ask thee in the name of thy Son, Jesus Christ, to bless and sanctify this bread to the souls of all those who partake of it, that they may eat in remembrance of the body of thy Son, and witness unto thee, O God, the Eternal Father, that they are willing to take upon them the name of thy Son, and always remember him and keep his commandments which he has given them; that they may always have his Spirit to be with them. Amen."
                }, {
                  "verse": "79",
                  "text": "O God, the Eternal Father, we ask thee in the name of thy Son, Jesus Christ, to bless and sanctify this wine to the souls of all those who drink of it, that they may do it in remembrance of the blood of thy Son, which was shed for them; that they may witness unto thee, O God, the Eternal Father, that they do always remember him, that they may have his Spirit to be with them. Amen."
                }
              ],
            },
            {
              id: 7,
              question:
                "I have the faith necessary to help make good things happen in my life or the lives of others.",
              scriptureHeader: "Ether 12:12",
              scripture: [
                {
                  "verse": "12",
                  "text": "For if there be no faith among the children of men God can do no miracle among them; wherefore, he showed not himself until after their faith."
                }
              ],
            },
            {
              id: 8,
              question:
                "I know by the power of the Holy Ghost that the Book of Mormon is true.",
              scriptureHeader: "Moroni 10:3-5",
              scripture: [
                {
                  "verse": "3",
                  "text": "Behold, I would exhort you that when ye shall read these things, if it be wisdom in God that ye should read them, that ye would remember how merciful the Lord hath been unto the children of men, from the creation of Adam even down until the time that ye shall receive these things, and ponder it in your hearts."
                }, {
                  "verse": "4",
                  "text": "And when ye shall receive these things, I would exhort you that ye would ask God, the Eternal Father, in the name of Christ, if these things are not true; and if ye shall ask with a sincere heart, with real intent, having faith in Christ, he will manifest the truth of it unto you, by the power of the Holy Ghost."
                }, {
                  "verse": "5",
                  "text": "And by the power of the Holy Ghost ye may know the truth of all things."
                }
              ],
            },
            {
              id: 9,
              question:
                "I have enough faith in Christ to accomplish anything He wants me to do—even miracles, if necessary.",
              scriptureHeader: "Moroni 7:33",
              scripture: [
                {
                  "verse": "33",
                  "text": "And Christ hath said: If ye will have faith in me ye shall have power to do whatsoever thing is expedient in me."
                }
              ],
            },
          ],
        },
        {
          name: "Hope",
          survey: [
            {
              id: 1,
              question:
                "One of my greatest desires is to inherit eternal life in the celestial kingdom of God.",
              scriptureHeader: "Moroni 7:41",
              scripture: [
                {
                  "verse": "41",
                  "text": "And what is it that ye shall hope for? Behold I say unto you that ye shall have hope through the atonement of Christ and the power of his resurrection, to be raised unto life eternal, and this because of your faith in him according to the promise."
                }
              ],
            },
            {
              id: 2,
              question:
                "I am confident that I will have a happy and successful mission.",
              scriptureHeader: "D&C 31:3-5",
              scripture: [
                {
                  "verse": "3",
                  "text": "Lift up your heart and rejoice, for the hour of your mission is come; and your tongue shall be loosed, and you shall declare glad tidings of great joy unto this generation."
                }, {
                  "verse": "4",
                  "text": "You shall declare the things which have been revealed to my servant, Joseph Smith, Jun. You shall begin to preach from this time forth, yea, to reap in the field which is white already to be burned."
                }, {
                  "verse": "5",
                  "text": "Therefore, thrust in your sickle with all your soul, and your sins are forgiven you, and you shall be laden with sheaves upon your back, for the laborer is worthy of his hire. Wherefore, your family shall live."
                }
              ],
            },
            {
              id: 3,
              question: "I feel peaceful and optimistic about the future.",
              scriptureHeader: "D&C 59:23",
              scripture: [
                {
                  "verse": "23",
                  "text": "But learn that he who doeth the works of righteousness shall receive his reward, even peace in this world, and eternal life in the world to come."
                }
              ],
            },
            {
              id: 4,
              question:
                "I firmly believe that someday I will dwell with God and become like Him.",
              scriptureHeader: "Ether 12:4",
              scripture: [
                {
                  "verse": "4",
                  "text": "Wherefore, whoso believeth in God might with surety hope for a better world, yea, even a place at the right hand of God, which hope cometh of faith, maketh an anchor to the souls of men, which would make them sure and steadfast, always abounding in good works, being led to glorify God."
                }
              ],
            },
          ],
        },
        {
          name: "Charity and Love",
          survey: [
            {
              id: 1,
              question:
                "I feel a sincere desire for the eternal welfare and happiness of other people.",
              scriptureHeader: "Mosiah 28:3",
              scripture: [{
                "verse": "3",
                "text": "Now they were desirous that salvation should be declared to every creature, for they could not bear that any human soul should perish; yea, even the very thoughts that any soul should endure endless torment did cause them to quake and tremble."
              }],
            },
            {
              id: 2,
              question:
                "When I pray, I ask for charity—the pure love of Christ.",
              scriptureHeader: "Moroni 7:47-48",
              scripture: [{
                "verse": "47",
                "text": "But charity is the pure love of Christ, and it endureth forever; and whoso is found possessed of it at the last day, it shall be well with him."
              }, {
                "verse": "48",
                "text": "Wherefore, my beloved brethren, pray unto the Father with all the energy of heart, that ye may be filled with this love, which he hath bestowed upon all who are true followers of his Son, Jesus Christ; that ye may become the sons of God; that when he shall appear we shall be like him, for we shall see him as he is; that we may have this hope; that we may be purified even as he is pure. Amen."
              }],
            },
            {
              id: 3,
              question:
                "I try to understand others’ feelings and see their point of view.",
              scriptureHeader: "Jude 1:22",
              scripture: [{
                "verse": "22",
                "text": "And of some have compassion, making a difference:"
              }],
            },
            {
              id: 4,
              question: "I forgive others who have offended or wronged me.",
              scriptureHeader: "Ephesians 4:32",
              scripture: [{
                "verse": "32",
                "text": "And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ\u00e2\u0080\u0099s sake hath forgiven you."
              }],
            },
            {
              id: 5,
              question:
                "I try to help others when they are struggling or discouraged.",
              scriptureHeader: "Mosiah 18:9",
              scripture: [{
                "verse": "9",
                "text": "Yea, and are willing to mourn with those that mourn; yea, and comfort those that stand in need of comfort, and to stand as witnesses of God at all times and in all things, and in all places that ye may be in, even until death, that ye may be redeemed of God, and be numbered with those of the first resurrection, that ye may have eternal life\u00e2\u0080\u0094"
              }],
            },
            {
              id: 6,
              question:
                "When appropriate, I tell others that I love them and care about them.",
              scriptureHeader: "Luke 7:12-15",
              scripture: [{
                "verse": "12",
                "text": "Now when he came nigh to the gate of the city, behold, there was a dead man carried out, the only son of his mother, and she was a widow: and much people of the city was with her."
              }, {
                "verse": "13",
                "text": "And when the Lord saw her, he had compassion on her, and said unto her, Weep not."
              }, {
                "verse": "14",
                "text": "And he came and touched the bier: and they that bare him stood still. And he said, Young man, I say unto thee, Arise."
              }, {
                "verse": "15",
                "text": "And he that was dead sat up, and began to speak. And he delivered him to his mother."
              }],
            },
            {
              id: 7,
              question: "I look for opportunities to serve other people.",
              scriptureHeader: "Mosiah 2:17",
              scripture: [{
                "verse": "17",
                "text": "And behold, I tell you these things that ye may learn wisdom; that ye may learn that when ye are in the service of your fellow beings ye are only in the service of your God."
              }],
            },
            {
              id: 8, question: "I say positive things about others.",
              scriptureHeader: "D&C 42:27",
              scripture: [{
                "verse": "27",
                "text": "Thou shalt not speak evil of thy neighbor, nor do him any harm."
              }]
            },
            {
              id: 9,
              question:
                "I am kind and patient with others, even when they are hard to get along with.",
              scriptureHeader: "Moroni 7:45",
              scripture: [{
                "verse": "45",
                "text": "And charity suffereth long, and is kind, and envieth not, and is not puffed up, seeketh not her own, is not easily provoked, thinketh no evil, and rejoiceth not in iniquity but rejoiceth in the truth, beareth all things, believeth all things, hopeth all things, endureth all things."
              }],
            },
            {
              id: 10, question: "I find joy in others’ achievements.",
              scriptureHeader: "Alma 17:2-4",
              scripture: [
                {
                  "verse": "2",
                  "text": "Now these sons of Mosiah were with Alma at the time the angel first appeared unto him; therefore Alma did rejoice exceedingly to see his brethren; and what added more to his joy, they were still his brethren in the Lord; yea, and they had waxed strong in the knowledge of the truth; for they were men of a sound understanding and they had searched the scriptures diligently, that they might know the word of God."
                }, {
                  "verse": "3",
                  "text": "But this is not all; they had given themselves to much prayer, and fasting; therefore they had the spirit of prophecy, and the spirit of revelation, and when they taught, they taught with power and authority of God."
                }, {
                  "verse": "4",
                  "text": "And they had been teaching the word of God for the space of fourteen years among the Lamanites, having had much success in bringing many to the knowledge of the truth; yea, by the power of their words many were brought before the altar of God, to call on his name and confess their sins before him."
                }
              ],
            },
          ],
        },
        {
          name: "Virtue",
          survey: [
            {
              id: 1,
              question: "I am clean and pure in heart.",
              scriptureHeader: "Psalms 24:3-4",
              scripture: [{
                "verse": "3",
                "text": "Who shall ascend into the hill of the Lord? or who shall stand in his holy place?"
              }, {
                "verse": "4",
                "text": "He that hath clean hands, and a pure heart; who hath not lifted up his soul unto vanity, nor sworn deceitfully."
              }],
            },
            {
              id: 2,
              question: "I have no desire to do evil but to do good.",
              scriptureHeader: "Mosiah 5:2",
              scripture: [{
                "verse": "2",
                "text": "And they all cried with one voice, saying: Yea, we believe all the words which thou hast spoken unto us; and also, we know of their surety and truth, because of the Spirit of the Lord Omnipotent, which has wrought a mighty change in us, or in our hearts, that we have no more disposition to do evil, but to do good continually."
              }],
            },
            {
              id: 3,
              question: "I am dependable—I do what I say I will do.",
              scriptureHeader: "Alma 53:20",
              scripture: [
                {
                  "verse": "20",
                  "text": "And they were all young men, and they were exceedingly valiant for courage, and also for strength and activity; but behold, this was not all\u00e2\u0080\u0094they were men who were true at all times in whatsoever thing they were entrusted."
                }
              ],
            },
            {
              id: 4,
              question:
                "I focus on righteous, uplifting thoughts and put unwholesome thoughts out of my mind.",
              scriptureHeader: "D&C 121:45",
              scripture: [
                {
                  "verse": "45",
                  "text": "Let thy bowels also be full of charity towards all men, and to the household of faith, and let virtue garnish thy thoughts unceasingly; then shall thy confidence wax strong in the presence of God; and the doctrine of the priesthood shall distil upon thy soul as the dews from heaven."
                }
              ],
            },
            {
              id: 5,
              question:
                "I repent of my sins and strive to overcome my weaknesses.",
              scriptureHeader: "D&C 49:26-28",
              scripture: [{
                "verse": "26",
                "text": "Behold, I say unto you, go forth as I have commanded you; repent of all your sins; ask and ye shall receive; knock and it shall be opened unto you."
              }, {
                "verse": "27",
                "text": "Behold, I will go before you and be your rearward; and I will be in your midst, and you shall not be confounded."
              }, {
                "verse": "28",
                "text": "Behold, I am Jesus Christ, and I come quickly. Even so. Amen."
              }],
            },
            {
              id: 6,
              question: "I feel the influence of the Holy Ghost in my life.",
              scriptureHeader: "D&C 11:12-13",
              scripture: [{
                "verse": "12",
                "text": "And now, verily, verily, I say unto thee, put your trust in that Spirit which leadeth to do good\u00e2\u0080\u0094yea, to do justly, to walk humbly, to judge righteously; and this is my Spirit."
              }, {
                "verse": "13",
                "text": "Verily, verily, I say unto you, I will impart unto you of my Spirit, which shall enlighten your mind, which shall fill your soul with joy;"
              }],
            },
          ],
        },
        {
          name: "Knowledge",
          survey: [
            {
              id: 1,
              question:
                "I feel confident in my understanding of gospel doctrine and principles.",
              scriptureHeader: "Ether 3:19-20",
              scripture: [{
                "verse": "19",
                "text": "And because of the knowledge of this man he could not be kept from beholding within the veil; and he saw the finger of Jesus, which, when he saw, he fell with fear; for he knew that it was the finger of the Lord; and he had faith no longer, for he knew, nothing doubting."
              }, {
                "verse": "20",
                "text": "Wherefore, having this perfect knowledge of God, he could not be kept from within the veil; therefore he saw Jesus; and he did minister unto him."
              }],
            },
            {
              id: 2,
              question: "I study the scriptures daily.",
              scriptureHeader: "John 5:39",
              scripture: [{
                "verse": "39",
                "text": "\u00c2\u00b6 Search the scriptures; for in them ye think ye have eternal life: and they are they which testify of me."
              }],
            },
            {
              id: 3,
              question:
                "I earnestly seek to understand the truth and find answers to my questions.",
              scriptureHeader: "D&C 6:7",
              scripture: [{
                "verse": "7",
                "text": "Seek not for riches but for wisdom, and behold, the mysteries of God shall be unfolded unto you, and then shall you be made rich. Behold, he that hath eternal life is rich."
              }],
            },
            {
              id: 4,
              question: "I receive knowledge and guidance through the Spirit.",
              scriptureHeader: "1 Nephi 4:6",
              scripture: [{
                "verse": "6",
                "text": "And I was led by the Spirit, not knowing beforehand the things which I should do."
              }],
            },
            {
              id: 5,
              question:
                "I love and cherish the doctrine and principles of the gospel.",
              scriptureHeader: "2 Nephi 4:15",
              scripture: [{
                "verse": "15",
                "text": "And upon these I write the things of my soul, and many of the scriptures which are engraven upon the plates of brass. For my soul delighteth in the scriptures, and my heart pondereth them, and writeth them for the learning and the profit of my children."
              }],
            },
          ],
        },
        {
          name: "Patience",
          survey: [
            {
              id: 1,
              question:
                "I wait patiently for the blessings and promises of the Lord to be fulfilled.",
              scriptureHeader: "2 Nephi 10:17",
              scripture: [{
                "verse": "17",
                "text": "For I will fulfil my promises which I have made unto the children of men, that I will do unto them while they are in the flesh\u00e2\u0080\u0094"
              }],
            },
            {
              id: 2,
              question:
                "I am able to wait for things without getting upset or frustrated.",
              scriptureHeader: "Romans 8:25",
              scripture: [{
                "verse": "25",
                "text": "But if we hope for that we see not, then do we with patience wait for it."
              }],
            },
            {
              id: 3,
              question:
                "I am patient and long-suffering with the challenges of being a missionary.",
              scriptureHeader: "Alma 17:11",
              scripture: [{
                "verse": "11",
                "text": "And the Lord said unto them also: Go forth among the Lamanites, thy brethren, and establish my word; yet ye shall be patient in long-suffering and afflictions, that ye may show forth good examples unto them in me, and I will make an instrument of thee in my hands unto the salvation of many souls."
              }],
            },
            {
              id: 4,
              question:
                "I am patient with the faults and weaknesses of others.",
              scriptureHeader: "Romans 15:1",
              scripture: [{
                "verse": "1",
                "text": "We then that are strong ought to bear the infirmities of the weak, and not to please ourselves."
              }],
            },
            {
              id: 5,
              question:
                "I am patient with myself and rely on the Lord as I work to overcome my weaknesses.",
              scriptureHeader: "Ether 12:27",
              scripture: [{
                "verse": "27",
                "text": "And if men come unto me I will show unto them their weakness. I give unto men weakness that they may be humble; and my grace is sufficient for all men that humble themselves before me; for if they humble themselves before me, and have faith in me, then will I make weak things become strong unto them."
              }],
            },
            {
              id: 6,
              question:
                "I face adversity and afflictions calmly and hopefully.",
              scriptureHeader: "Alma 34:40-41",
              scripture: [{
                "verse": "40",
                "text": "And now my beloved brethren, I would exhort you to have patience, and that ye bear with all manner of afflictions; that ye do not revile against those who do cast you out because of your exceeding poverty, lest ye become sinners like unto them;"
              }, {
                "verse": "41",
                "text": "But that ye have patience, and bear with those afflictions, with a firm hope that ye shall one day rest from all your afflictions."
              }],
            },
          ],
        },
        {
          name: "Humility",
          survey: [
            {
              id: 1,
              question: "I am meek and lowly in heart.",
              scriptureHeader: "Matthew 11:29",
              scripture: [{
                "verse": "29",
                "text": "Take my yoke upon you, and learn of me; for I am meek and lowly in heart: and ye shall find rest unto your souls."
              }],
            },
            {
              id: 2,
              question: "I rely on the Lord for help.",
              scriptureHeader: "Alma 26:12",
              scripture: [{
                "verse": "12",
                "text": "Yea, I know that I am nothing; as to my strength I am weak; therefore I will not boast of myself, but I will boast of my God, for in his strength I can do all things; yea, behold, many mighty miracles we have wrought in this land, for which we will praise his name forever."
              }],
            },
            {
              id: 3,
              question:
                "I am sincerely grateful for the blessings I have received from the Lord.",
              scriptureHeader: "Alma 7:23",
              scripture: [{
                "verse": "23",
                "text": "And now I would that ye should be humble, and be submissive and gentle; easy to be entreated; full of patience and long-suffering; being temperate in all things; being diligent in keeping the commandments of God at all times; asking for whatsoever things ye stand in need, both spiritual and temporal; always returning thanks unto God for whatsoever things ye do receive."
              }],
            },
            {
              id: 4,
              question: "My prayers are earnest and sincere.",
              scriptureHeader: "Enos 1:4",
              scripture: [{
                "verse": "4",
                "text": "4 And my soul hungered; and I kneeled down before my Maker, and I cried unto him in mighty prayer and supplication for mine own soul; and all the day long did I cry unto him; yea, and when the night came I did still raise my voice high that it reached the heavens."
              }],
            },
            {
              id: 5,
              question: "I appreciate direction from my leaders or teachers.",
              scriptureHeader: "2 Nephi 9:28",
              scripture: [{
                "verse": "28",
                "text": "O that cunning plan of the evil one! O the vainness, and the frailties, and the foolishness of men! When they are learned they think they are wise, and they hearken not unto the counsel of God, for they set it aside, supposing they know of themselves, wherefore, their wisdom is foolishness and it profiteth them not. And they shall perish."
              }],
            },
            {
              id: 6,
              question:
                "I strive to be submissive to the Lord’s will, whatever it may be.",
              scriptureHeader: "Mosiah 24:15",
              scripture: [{
                "verse": "15",
                "text": "And now it came to pass that the burdens which were laid upon Alma and his brethren were made light; yea, the Lord did strengthen them that they could bear up their burdens with ease, and they did submit cheerfully and with patience to all the will of the Lord."
              }],
            },
          ],
        },
        {
          name: "Diligence",
          survey: [
            {
              id: 1,
              question:
                "I work effectively, even when I’m not under pressure or close supervision.",
              scriptureHeader: "D&C 58:26-27",
              scripture: [{
                "verse": "26",
                "text": "For behold, it is not meet that I should command in all things; for he that is compelled in all things, the same is a slothful and not a wise servant; wherefore he receiveth no reward."
              }, {
                "verse": "27",
                "text": "Verily I say, men should be anxiously engaged in a good cause, and do many things of their own free will, and bring to pass much righteousness;"
              }],
            },
            {
              id: 2,
              question: "I focus my efforts on the most important things.",
              scriptureHeader: "Matthew 23:23",
              scripture: [{
                "verse": "23",
                "text": "Woe unto you, scribes and Pharisees, hypocrites! for ye pay tithe of mint and anise and cummin, and have omitted the weightier matters of the law, judgment, mercy, and faith: these ought ye to have done, and not to leave the other undone."
              }],
            },
            {
              id: 3,
              question: "I have a personal prayer at least twice a day.",
              scriptureHeader: "Alma 34:18-27",
              scripture: [
                {
                  "verse": "18",
                  "text": "Yea, cry unto him for mercy; for he is mighty to save."
                }, {
                  "verse": "19",
                  "text": "Yea, humble yourselves, and continue in prayer unto him."
                }, {
                  "verse": "20",
                  "text": "Cry unto him when ye are in your fields, yea, over all your flocks."
                }, {
                  "verse": "21",
                  "text": "Cry unto him in your houses, yea, over all your household, both morning, mid-day, and evening."
                }, {
                  "verse": "22",
                  "text": "Yea, cry unto him against the power of your enemies."
                }, {
                  "verse": "23",
                  "text": "Yea, cry unto him against the devil, who is an enemy to all righteousness."
                }, {
                  "verse": "24",
                  "text": "Cry unto him over the crops of your fields, that ye may prosper in them."
                }, {
                  "verse": "25",
                  "text": "Cry over the flocks of your fields, that they may increase."
                }, {
                  "verse": "26",
                  "text": "But this is not all; ye must pour out your souls in your closets, and your secret places, and in your wilderness."
                }, {
                  "verse": "27",
                  "text": "Yea, and when you do not cry unto the Lord, let your hearts be full, drawn out in prayer unto him continually for your welfare, and also for the welfare of those who are around you."
                }],
            },
            {
              id: 4,
              question: "I focus my thoughts on my calling as a missionary.",
              scriptureHeader: "D&C 4:2,5",
              scripture: [{
                "verse": "2",
                "text": "Therefore, O ye that embark in the service of God, see that ye serve him with all your heart, might, mind and strength, that ye may stand blameless before God at the last day."
              }, {
                "verse": "5",
                "text": "And faith, hope, charity and love, with an eye single to the glory of God, qualify him for the work."
              }],
            },
            {
              id: 5,
              question: "I set goals and plan regularly.",
              scriptureHeader: "D&C 88:119",
              scripture: [{
                "verse": "119",
                "text": "Organize yourselves; prepare every needful thing; and establish a house, even a house of prayer, a house of fasting, a house of faith, a house of learning, a house of glory, a house of order, a house of God;"
              }],
            },
            {
              id: 6,
              question: "I work hard until the job is completed successfully.",
              scriptureHeader: "D&C 10:4",
              scripture: [{
                "verse": "4",
                "text": "Do not run faster or labor more than you have strength and means provided to enable you to translate; but be diligent unto the end."
              }],
            },
            {
              id: 7,
              question: "I find joy and satisfaction in my work.",
              scriptureHeader: "Alma 36:24-25",
              scripture: [{
                "verse": "24",
                "text": "Yea, and from that time even until now, I have labored without ceasing, that I might bring souls unto repentance; that I might bring them to taste of the exceeding joy of which I did taste; that they might also be born of God, and be filled with the Holy Ghost."
              }, {
                "verse": "25",
                "text": "Yea, and now behold, O my son, the Lord doth give me exceedingly great joy in the fruit of my labors;"
              }],
            },
          ],
        },
        {
          name: "Obedience",
          survey: [
            {
              id: 1,
              question:
                "When I pray, I ask for strength to resist temptation and to do what is right.",
              scriptureHeader: "3 Nephi 18:15",
              scripture: [{
                "verse": "15",
                "text": "Verily, verily, I say unto you, ye must watch and pray always, lest ye be tempted by the devil, and ye be led away captive by him."
              }],
            },
            {
              id: 2,
              question:
                "I keep the required commandments to be worthy of a temple recommend.",
              scriptureHeader: "D&C 97:8",
              scripture: [{
                "verse": "8",
                "text": "Verily I say unto you, all among them who know their hearts are honest, and are broken, and their spirits contrite, and are willing to observe their covenants by sacrifice\u00e2\u0080\u0094yea, every sacrifice which I, the Lord, shall command\u00e2\u0080\u0094they are accepted of me."
              }],
            },
            {
              id: 3,
              question:
                "I willingly obey the mission rules and follow the counsel of my leaders.",
              scriptureHeader: "Hebrews 13:17",
              scripture: [{
                "verse": "17",
                "text": "Obey them that have the rule over you, and submit yourselves: for they watch for your souls, as they that must give account, that they may do it with joy, and not with grief: for that is unprofitable for you."
              }],
            },
            {
              id: 4,
              question:
                "I strive to live in accordance with the laws and principles of the gospel.",
              scriptureHeader: "D&C 41:5",
              scripture: [{
                "verse": "5",
                "text": "He that receiveth my law and doeth it, the same is my disciple; and he that saith he receiveth it and doeth it not, the same is not my disciple, and shall be cast out from among you;"
              }],
            },
          ],
        },
      ],
    };
  },
};
</script>
