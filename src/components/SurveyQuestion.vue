<template>
  <div class="container">   
    <div class="row">
      <div class="col-8 ml-2 mt-1">
        {{ survey.question }}
          <b-icon icon="book" :id="attributeKey"></b-icon>
          <b-popover :target="attributeKey" triggers="hover" placement="right">
            <template #title>{{survey.scriptureHeader}}</template>
            <p
              v-for="scripture in survey.scripture"
              :key="scripture.verse"
            ><b>{{ scripture.verse }}</b> {{ scripture.text }}</p>
          </b-popover>          
      </div>
      <div class="col">
        <div
          class="btn-group btn-group-sm pb-1"
          role="group"
          aria-label="Attribute Self Assessment"
        >
          <button
            type="button"
            class="btn"
            :class="[answer[0] ? selected : notSelected]"
            @click="saveAssessment(1)"
          >
            1
          </button>
          <button
            type="button"
            class="btn"
            :class="[answer[1] ? selected : notSelected]"
            @click="saveAssessment(2)"
          >
            2
          </button>
          <button
            type="button"
            class="btn"
            :class="[answer[2] ? selected : notSelected]"
            @click="saveAssessment(3)"
          >
            3
          </button>
          <button
            type="button"
            class="btn"
            :class="[answer[3] ? selected : notSelected]"
            @click="saveAssessment(4)"
          >
            4
          </button>
          <button
            type="button"
            class="btn"
            :class="[answer[4] ? selected : notSelected]"
            @click="saveAssessment(5)"
          >
            5
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SurveyQuestion",
  data() {
    return {
      fillMask: [1, 1, 1, 1, 1],
      answer: [],
      selected: "btn-success",
      notSelected: "btn-secondary",
    };
  },
  props: {
    survey: {
      type: Object,
      required: true,
    },
    attributeKey: {
      type: String,
      required: true,
    }
  },
  methods: {
    saveAssessment: function (selfAssessment) {
      this.answer =
        selfAssessment == 5
          ? Array.from(this.fillMask)
          : Array.from(this.fillMask).fill(0, selfAssessment);
      this.$emit('increment-response', this.attributeKey + '_' + selfAssessment);
    },
  },
};
</script>