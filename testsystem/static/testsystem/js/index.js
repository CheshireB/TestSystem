import InputGroup from "./input_group";


window.onload = () => {
	const inputGroups = InputGroup.initInputGroups();
	const generateButton = document.getElementById("generate-btn");
	generateButton.addEventListener("click", () => {
		generateVariant(InputGroup.getAllValues(inputGroups));
	});
};

function generateVariant(inputValues) {
	const parameters = inputValues.map(value => `id=${value}`);
	const queryParameters = parameters.join("&");
	const query = `get_temp_test/?${queryParameters}`;
	window.location.href = query;
}