/**
 * InputGroup is a group of inputs, that controls
 * amount of questions in themes
 */
class InputGroup {
	
	/**
	 * input is a input element, which stores amount of questions
	 * by pressing on dec_btn and inc_btn user can change amount of questions
	 * a value in the input should be in range (min_value, max_value)
	 */
	constructor(input, dec_btn, inc_btn, value, min_value, max_value) {
		
		this._input = input;
		this._decrement_button = dec_btn;
		this._increment_button = inc_btn;
		this._value = value;
		this._min_value = min_value;
		this._max_value = max_value;
		
		this.setHandlers();

	}

	/**
	 * This method handles decrement actions
	 */
	decrementHandler() {
		if (this._value > this._min_value) {
			if (this._increment_button.disabled === true) {
				this._increment_button.removeAttribute("disabled");
			}
			this._value--;
			this._input.value = this._value;
			if (this._value === this._min_value) {
				this._decrement_button.setAttribute("disabled", true);
			}
		}
	}

	/**
	 * This method handles increment actions
	 */
	incrementHandler() {
		if (this._value < this._max_value) {
			if (this._decrement_button.disabled === true) {
				this._decrement_button.removeAttribute("disabled");
			}
			this._value++;
			this._input.value = this._value;
			if (this._value === this._max_value) {
				this._increment_button.setAttribute("disabled", true);
			}
		}
	}

	/**
	 * This method sets handlers to decrement and increment buttons
	 */
	setHandlers() {
		this._decrement_button.addEventListener("click", this.decrementHandler.bind(this));
		this._increment_button.addEventListener("click", this.incrementHandler.bind(this));
	}

	/**
	 * This function returns value of the input
	 */
	getValue() {
		return this._value;
	}

	/**
	 * This method inits all input groups on the page and returns them
	 */
	static initInputGroups() {

		// empty array for members of InputGroup class
		let data = [];
		
		// get all input groups on the page
		const InputGroups = [...document.getElementsByClassName("input-group")];
		
		InputGroups.forEach((inputGroup) => {
			
			// get buttons
			const [dec_btn, inc_btn] = [...inputGroup.getElementsByTagName("button")];

			// get input
			const input = inputGroup.getElementsByClassName("form-control")[0];
			
			// get attributes of input element
			const value = parseInt(input.value);
			const min_value = parseInt(input.min);
			const max_value = parseInt(input.max);

			data.push(new InputGroup(input, dec_btn, inc_btn, value, min_value, max_value));

		});

		return data;

	}

	/**
	 * This function returns 
	 */
	static getAllValues(inputGroups) {
		return inputGroups.map(inputGroup => inputGroup.getValue())
	}

}

export default InputGroup;