# Independent audit of the local absorption counterexample

## Verdict

**PASS with the stated narrow scope.**  The construction is an exact
`c downarrow 1` single-threshold relaxation counterexample.  It is not an
actual full-line or all-threshold process, and the full selected-line gate
rejects it.

## Exact checks

The absorbed mass, total mass, request width, and edge moment are

\[
A={9\over5},\qquad f={11\over5},\qquad W={7\over25},
\qquad \ell=3.
\]

The identity `s(t)=p(1-t)` proves joint direction-length stationarity.  The
request intervals contain their assigned levels, the absorbed transitions
are off-diagonal, the line measures are dominated by Lebesgue measure, and
the zero-gap budget is saturated.

The absorbed-line penalty is

\[
E_A=\tau+I={261\over200}<{7\over5}=2f-\ell.
\]

The nonabsorbed block pays `121/250`, so

\[
U(1^+)={1029\over250}=4+{29\over250}.
\]

Thus the example genuinely defeats absorbed-line control alone.

## Refined dangerous band

For `C=2A-W`, the bounds

\[
C\le\min(2A,6-2f+A),\qquad F(A)\le2f-3
\]

give `C<=1+f` for `f<=2` and `f>=22/9`.  On the upper branch this is exactly

\[
\sqrt{4f-8}\le3(f-2),
\]

whose roots are `2` and `22/9`.  Hence `(2,22/9)` is the exact open band left
by these local inequalities, apart from endpoint equality analysis.

## Full-line rejection

For any level `v` of the added `z`-line, `|v|<=9/10`.  Against the selected
absorbed line sets `X=[0,9/10]` and `Y=[1/10,1]`, its incremental full penalty

\[
|v|+P_X(v)+P_Y(v)-T(v)
\]

is at least one.  Therefore beta mass `2/5` adds at least `2/5`, and

\[
{261\over200}+{2\over5}={341\over200}>{7\over5}.
\]

The full selected-line coarea gate already kills the example at one
threshold.  Common lifetimes are not needed for this particular rejection,
though they remain necessary in the general mixed-profile problem.
