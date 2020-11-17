<template>
  <div class="container">
    <div>1=never 5= always</div>
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
  components: { Attribute },
  data() {
    return {
      attributes: [
        {
          name: "Faith",
          survey: [
            {
              id: 1,
              question: "I believe in Christ and accept Him as my Savior.",
            },
            { 
              id: 2, 
              question: "I feel confident that God loves me.",
            },
            {
              id: 3,
              question: "I trust the Savior enough to accept His will and do whatever He asks.",
            },
            {
              id: 4,
              question: "I firmly believe that through the Atonement of Jesus Christ I can be forgiven of all my sins.",
            },
            {
              id: 5,
              question:
                "I have enough faith in Christ to obtain answers to my prayers.",
            },
            {
              id: 6,
              question:
                "I think about the Savior during the day and remember what He has done for me.",
            },
            {
              id: 7,
              question:
                "I have the faith necessary to help make good things happen in my life or the lives of others.",
            },
            {
              id: 8,
              question:
                "I know by the power of the Holy Ghost that the Book of Mormon is true.",
            },
            {
              id: 9,
              question:
                "I have enough faith in Christ to accomplish anything He wants me to do—even miracles, if necessary.",
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
            },
            {
              id: 2,
              question:
                "I am confident that I will have a happy and successful mission.",
            },
            {
              id: 3,
              question: "I feel peaceful and optimistic about the future.",
            },
            {
              id: 4,
              question:
                "I firmly believe that someday I will dwell with God and become like Him.",
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
            },
            {
              id: 2,
              question: "When I pray, I ask for charity—the pure love of Christ.",
            },
            {
              id: 3,
              question:
                "I try to understand others’ feelings and see their point of view.",
            },
            {
              id: 4,
              question: "I forgive others who have offended or wronged me.",
            },
            {
              id: 5,
              question:
                "I try to help others when they are struggling or discouraged.",
            },
            {
              id: 6,
              question:
                "When appropriate, I tell others that I love them and care about them.",
            },
            { id: 7, question: "I look for opportunities to serve other people." },
            { id: 8, question: "I say positive things about others." },
            {
              id: 9,
              question:
                "I am kind and patient with others, even when they are hard to get along with.",
            },
            { id: 10, question: "I find joy in others’ achievements." },
          ],
        },
        {
          name: "Virtue",
          survey: [
            { id: 1, question: "I am clean and pure in heart." },
            { id: 2, question: "I have no desire to do evil but to do good." },
            { id: 3, question: "I am dependable—I do what I say I will do." },
            {
              id: 4,
              question:
                "I focus on righteous, uplifting thoughts and put unwholesome thoughts out of my mind.",
            },
            {
              id: 5,
              question:
                "I repent of my sins and strive to overcome my weaknesses.",
            },
            {
              id: 6,
              question: "I feel the influence of the Holy Ghost in my life.",
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
            },
            { id: 2, question: "I study the scriptures daily." },
            {
              id: 3,
              question:
                "I earnestly seek to understand the truth and find answers to my questions.",
            },
            {
              id: 4,
              question: "I receive knowledge and guidance through the Spirit.",
            },
            {
              id: 5,
              question:
                "I love and cherish the doctrine and principles of the gospel.",
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
            },
            {
              id: 2,
              question:
                "I am able to wait for things without getting upset or frustrated.",
            },
            {
              id: 3,
              question:
                "I am patient and long-suffering with the challenges of being a missionary.",
            },
            {
              id: 4,
              question: "I am patient with the faults and weaknesses of others.",
            },
            {
              id: 5,
              question:
                "I am patient with myself and rely on the Lord as I work to overcome my weaknesses.",
            },
            {
              id: 6,
              question: "I face adversity and afflictions calmly and hopefully.",
            },
          ],
        },
        {
          name: "Humility",
          survey: [
            { id: 1, question: "I am meek and lowly in heart." },
            { id: 2, question: "I rely on the Lord for help." },
            {
              id: 3,
              question:
                "I am sincerely grateful for the blessings I have received from the Lord.",
            },
            { id: 4, question: "My prayers are earnest and sincere." },
            {
              id: 5,
              question: "I appreciate direction from my leaders or teachers.",
            },
            {
              id: 6,
              question:
                "I strive to be submissive to the Lord’s will, whatever it may be.",
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
            },
            {
              id: 2,
              question: "I focus my efforts on the most important things.",
            },
            { id: 3, question: "I have a personal prayer at least twice a day." },
            {
              id: 4,
              question: "I focus my thoughts on my calling as a missionary.",
            },
            { id: 5, question: "I set goals and plan regularly." },
            {
              id: 6,
              question: "I work hard until the job is completed successfully.",
            },
            { id: 7, question: "I find joy and satisfaction in my work." },
          ],
        },
        {
          name: "Obedience",
          survey: [
            {
              id: 1,
              question:
                "When I pray, I ask for strength to resist temptation and to do what is right.",
            },
            {
              id: 2,
              question:
                "I keep the required commandments to be worthy of a temple recommend.",
            },
            {
              id: 3,
              question:
                "I willingly obey the mission rules and follow the counsel of my leaders.",
            },
            {
              id: 4,
              question:
                "I strive to live in accordance with the laws and principles of the gospel.",
            },
          ],
        },
      ],
    };
  },
};
</script>