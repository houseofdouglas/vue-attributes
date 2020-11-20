<template>
    <div>
      <div class="row">
        <div class="col-sm-8 pt-2 pl-2">
          <h3>{{ attribute.name }}</h3>
        </div>
        <div class="col-sm-4 pt-2 pl-4">
          <h3>{{score}}/{{numberOfSurveys}}</h3>
        </div>
      </div>
      <survey-question
        v-for="(survey, index) in attribute.survey"
        v-bind:key="index"
        v-bind:attributeKey="attribute.name + '_' + index"
        v-bind:survey="survey"
        v-on:increment-response="incrementResponse"
      ></survey-question>
    </div>
</template>
<script>
import SurveyQuestion from "./SurveyQuestion";
const reducer = (accumulator, currentValue) => accumulator + currentValue;
export default {  
  name: "Attribute",
  components: { SurveyQuestion },
  data() {
      return {
          response: [],
          score: 0
      }
  },
  props: {
    attribute: {
      type: Object,
      required: true,
    },
  },
  computed: {
      numberOfSurveys() {
          return this.attribute.survey.length*5
      },
      progressPercentage() {
          return (this.score/this.numberOfSurveys*100).toFixed(0);
      }
  },
  methods: {
      incrementResponse: function(response) {
          let element = response.split('_');
          this.response[element[1]] = parseInt(element[2]);
          this.score = this.response.reduce(reducer);
      }
  }
}
</script>