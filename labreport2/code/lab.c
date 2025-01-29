#include <stdio.h>
#include <math.h>

#define THRESHOLD 0.0001  // Define the threshold for stopping

// Function to generate v * exp(-x)
double generate_value(double v, double x) {
    return v * exp(-x);
}

// Function to update v1 based on the previous value and input x
double update_v1(double prev_v1, double x) {
    double temp = generate_value(prev_v1, x);  // First application
    double final_value = generate_value(temp, x);  // Second application
    return 5 * (1 - 1 / exp(x)) + final_value;
}

int main(void) {
    double x;  
    printf("Enter the value of x for exponent calculation: ");
    scanf("%lf", &x);

    double v1 = 5 * (1 - 1 / exp(x)); // Initial V1
    double prev_v1, v2;
    int iterations = 0;

    do {
        prev_v1 = v1;  // Store previous V1
        v1 = update_v1(prev_v1, x);  // Update V1
        v2 = generate_value(v1, x);  // Compute V2 from new V1

        iterations++;
        printf("Iteration %d: V1 = %lf, V2 = %lf\n", iterations, v1, v2);
    } while (fabs(v1 - prev_v1) > THRESHOLD); // Stop when difference is small

    printf("Final V1 reached: %lf after %d iterations\n", v1, iterations);
    return 0;
}

