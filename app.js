if (window !== "undefined") {
  // browser code
var client;
init();
async function init() {
client =await window.app.initialized();
}
const questions = [
  "What is the age of Illayaraja",
  "How many songs did he compose?",
  "Who introduced him into indian cinema?",
  "For which actor he composed 1000 of songs from 1980-1987?",
  "How many awards did he get?",
];
console.log(questions)

const API_BASE_URL = "https://api.surveysparrow.com/v3/";
const headers = {
  options: {
    headers: {
      Authorization: `Bearer <%= iparams.surveysparrow_api_key %>`,
    },
  },
};
const button = document.getElementById("btn");
const message = document.getElementById("msg");

async function createSurvey(){
  try {
    button.innerHTML = "Your Survey is being created...";

    // Create the Survey
    const surveyId = await postSurvey();

    // Create questions for the Survey
    for (let question of questions) {
      await postQuestion(surveyId, question);
    }
      button.innerHTML = "Create";
    showNotificationMessage("Survey Created Successfully", { type: "success" });
  } catch (error) {
    button.innerHTML = "Create";
    console.log("Error while creating the Survey", error);
    showNotificationMessage("Error while Creating Survey", { type: "failure" });
}
}
async function postSurvey() {
  const response = await client.request.post(`${API_BASE_URL}surveys`, headers, {
    name: "My Marketplace Survey",
    survey_type: "ClassicForm",
  });
  return JSON.parse(response).body.data.id;
}
async function postQuestion(surveyId, question) {
  await client.request.post(`${API_BASE_URL}questions`, headers, {
    survey_id: surveyId,
    question: {
      type: "TextInput",
      text: question,
    },
  });
}
function showNotificationMessage(message, options){
  client.interface.alertMessage(message, options);
  if (options.type === "success") {
    message.innerHTML = "Please navigate to home screen to see newly created Survey.";
    setTimeout(() => {
      message.innerHTML = "";
    }, 3000);
  }
}
}
