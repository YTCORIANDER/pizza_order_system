# Pizza Order System
Welcome to the Pizza Order System! 🍕 This Python program allows users to place pizza orders with customizable toppings and sizes, ensuring a delightful pizza ordering experience.

## About
Pizza Order System simplifies the process of ordering pizzas by providing a user-friendly interface to select pizza sizes and toppings. It calculates the total cost of the order and generates a detailed receipt for the customer.

## Features
- **Customizable Orders**: Users can select from a variety of pizza sizes and toppings to customize their orders according to their preferences.
- **Automatic Price Calculation**: The system automatically calculates the total cost of the order based on the selected size and toppings, ensuring accuracy and convenience.
- **Detailed Receipt Generation**: Upon completion of the order, the system generates a comprehensive receipt containing itemized information and the total cost, providing transparency and clarity.

## Getting Started
To start using the Pizza Order System:

1. Clone this repository: `git clone https://github.com/YTCORIANDER/pizza_order_system.git`
2. Navigate to the project directory: `cd pizza-order-system`
3. Run the Python script: `python pizza_order.py`
4. Follow the prompts to place your pizza order, selecting the size and toppings of your choice.
5. Once your order is complete, the system will generate a receipt displaying the details of your order and the total cost.

## Usage
Here's an example of how to use the Pizza Order System:

```bash
$ python pizza_order.py
Welcome to Pizza Order System!

Choose a size: S, M, L, or XL:  S
Type in one of our toppings to add it to your pizza. To see the list of toppings, enter 'LIST'.
When you are done adding toppings, enter 'X': Pepperoni
Added Pepperoni to your pizza
Type in one of our toppings to add it to your pizza. To see the list of toppings, enter 'LIST'.
When you are done adding toppings, enter 'X': Mushrooms
Added Mushrooms to your pizza
Type in one of our toppings to add it to your pizza. To see the list of toppings, enter 'LIST'.
When you are done adding toppings, enter 'X': X
Your order:
Pizza 1:  S             7.99
- Pepperoni
- Mushrooms
Tax: 1.04
Total: 9.03
```
## Modify and Customize
Certainly! To enable users to easily locate the file where they can modify toppings and provide options for adding or deleting toppings, you can include the following section in the README.md:

---

## Modify Toppings
The toppings for pizzas in the Pizza Order System are defined in a dedicated file, making it simple for you to add, delete, or modify toppings according to your preferences. You can find the toppings file at:
- **File**: `toppings.py`

### Adding Toppings
To add new toppings to the system:

1. Open the `toppings.py` file in your preferred code editor.
2. Locate the list of toppings within the file.
3. Simply add the name of the new topping to the list, following the existing format.

```python
# toppings.py

toppings = [
    "Pepperoni",
    "Mushrooms",
    "Onions",
    # Add your new topping here
]
```

4. Save the file after adding the new topping.

### Deleting Toppings
To delete toppings from the system:
1. Open the `toppings.py` file in your preferred code editor.
2. Locate the list of toppings within the file.
3. Remove the desired topping from the list.
```python
# toppings.py

toppings = [
    "Pepperoni",
    "Mushrooms",
    # "Onions",  # Delete the topping by commenting it out or removing it
]
```
4. Save the file after removing the topping.

### Testing Your Changes
Testing is an essential aspect of software development to ensure that the Pizza Order System functions correctly and meets the desired requirements. Here's how you can conduct testing for the Pizza Order System:

#### Automated Testing
1. **Run Automated Tests**: Utilize the provided `runTest` function to run automated tests for different scenarios. This function executes the Pizza Order System with predefined input and compares the output against expected results.

2. **Interpret Test Results**: After running automated tests, interpret the results to determine if the Pizza Order System behaves as expected. Tests may pass or fail based on whether the actual output matches the expected output.

#### Manual Testing
1. **Interactive Testing**: Manually interact with the Pizza Order System by running it directly from the command line. Enter various input combinations to simulate different user scenarios and observe the system's responses.

2. **Edge Cases**: Test edge cases and boundary conditions to validate the system's robustness and handling of exceptional scenarios. For example, try ordering pizzas with the maximum number of toppings or selecting uncommon pizza sizes.

#### Functional Testing
1. **Functional Coverage**: Ensure functional coverage by testing all features and functionalities of the Pizza Order System. Verify that users can place orders, customize pizzas, calculate prices accurately, and generate receipts correctly.

2. **User Experience**: Evaluate the user experience by assessing the clarity of prompts, intuitiveness of interactions, and overall usability of the Pizza Order System. Solicit feedback from users to identify areas for improvement.

#### Integration Testing
1. **Integration with Other Systems**: If the Pizza Order System integrates with external services or APIs (e.g., payment gateways), perform integration testing to validate seamless communication and data exchange between systems.

2. **Compatibility Testing**: Test the Pizza Order System across different platforms, browsers, and devices to ensure compatibility and consistent behavior across diverse environments.

#### Performance Testing
1. **Performance Metrics**: Measure the performance of the Pizza Order System in terms of response times, resource utilization, and scalability. Identify potential bottlenecks and optimize performance for optimal user experience.

2. **Load Testing**: Simulate high loads and concurrent user interactions to assess how the Pizza Order System handles increased traffic and maintains responsiveness under stress conditions.

#### Regression Testing
1. **Regression Test Suites**: Maintain regression test suites to verify that recent code changes or enhancements do not introduce new defects or regressions in existing functionality.

2. **Automate Regression Testing**: Automate regression testing wherever possible to streamline the process and ensure consistent validation of system integrity across different iterations.

## Contribute
Contributions to the Pizza Order System project are welcome! Whether you're adding new features, optimizing existing code, or fixing bugs, your contributions are appreciated. Please refer to the [contribution guidelines](CONTRIBUTING.md) for more information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions regarding the Pizza Order System, feel free to reach out.

Enjoy delicious and customizable pizzas with the Pizza Order System! 🍕🛒
