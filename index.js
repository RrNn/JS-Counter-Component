class Counter extends HTMLElement {
	constructor() {
		super();
		//Increment button
		this.increaseButton = document.createElement('button');
		this.increaseButton.id = 'increase';
		this.increaseButton.innerText = 'Increase';
		//Reduction button
		this.decreaseButton = document.createElement('button');
		this.increaseButton.id = 'decrease';
		// The count
		this.counter = document.createElement('span');
		this.counter.className = 'the-counter'
		// Prompt input
		this.input = document.createElement('input');
		this.input.className = 'prompt-input';
		this.input.type = 'number';
		this.input.placeholder = 'Enter Number to Increase and Decrease by';
		// Prompt button
		this.promptButton = document.createElement('button');
		this.promptButton.className = 'prompt-button';
		this.promptButton.innerText = 'Continue';
		//Value to use for increament and decrement
		this.increaseDecrease = null;
		// Info on increase and decrease value
		this.info = document.createElement('p');



		//Counter

		this.counter.innerText = '0';
		this.decreaseButton.innerText = 'Decrease';

		this.appendChild(this.input);
		this.appendChild(this.promptButton);
		this.appendChild(document.createElement('br'));
		this.appendChild(this.decreaseButton);
		this.appendChild(this.counter);
		this.appendChild(this.increaseButton);


		this.promptButton.addEventListener('click', (e) => {
			this.input.value
				? (this.increaseDecrease = parseInt(this.input.value))
				: (this.increaseDecrease = 1);
			this.input.value = null;

			this.info.innerText =
				'Currently Increasing and Decresing by ' +
				this.increaseDecrease;
			this.appendChild(this.info);
		});

		this.decreaseButton.addEventListener('click', () => {
			this.increaseDecrease === null
			? (this.noIncreaseDecreaseFound())
			:
			  (this.counter.innerText =
				parseInt(this.counter.innerText) - this.increaseDecrease);
		});

		this.increaseButton.addEventListener('click', (e) => {
			this.increaseDecrease === null
			? (this.noIncreaseDecreaseFound())
			: (this.counter.innerText =
				parseInt(this.counter.innerText) + this.increaseDecrease);
		});

	}

	noIncreaseDecreaseFound(){
		this.info.innerText = `What's wrong with you? You did not provide any number to increment or decrement with,
		just click on the Continue button to increment and decrement by 1`
		this.appendChild(this.info)
	}

	counter() {}

	connectedCallback() {
		console.log('Custom counter element added to page.');
	}

}


customElements.define('counter-component', Counter);
