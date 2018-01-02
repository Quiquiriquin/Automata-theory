This automaton has 3 states and 1 final state. When you enter a different letter of i, you'll be in the same initial state. 
When the automaton gets and 'i' (state 1), the next letter that it can receive is 'n' or 'i'. If we got and 'i', it will stay 
at state 1. In the case that we got an 'n' the automaton is going to pass to the state 2. If we are in the state 2 and we get 
a different character of 'g', we'll have 2 options, if is 'i', it will go back to the state 1, if is different of 'i', it will 
go back to the initial state. The process will end when the string has empty and the automata be on the third state.

It works in automatic form and manual form. Automatic consist in read a file, so if you choose manual yo are going to type
the text that you want to analyze.

The automaton give 2 ways to see the results. In the shell window and if you prefer in the file with the name "SalidaIng.txt" 
