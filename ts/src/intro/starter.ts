import {
  BedrockClient,
  ListFoundationModelsCommand,
} from "@aws-sdk/client-bedrock";

const client = new BedrockClient({
  region: "us-west-2",
});

async function listFoundationModels() {
  const response = await client.send(new ListFoundationModelsCommand({}));
  console.log(response);
}

listFoundationModels();
