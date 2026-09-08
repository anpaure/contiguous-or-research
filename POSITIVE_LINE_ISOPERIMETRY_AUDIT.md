# Independent audit of positive-line isoperimetry and the paired broad seal

## Verdict

**PASS, with narrow scope.**  The sharp line-energy inequality, the absorbed
mass bound, the saving calculation, and the common-weight dual algebra are
correct.  They eliminate every arbitrary partial actual-line absorption of
the one explicit nested alternating-pair broad ledger.  They do not eliminate
all mixed profiles and do not prove the local three-box lemma or the original
contiguous-OR conjecture.

## Checks

For three measures `nu_i<=dt` on `[0,1]`, the energy

\[
E=\sum_i\int t\,d\nu_i+
\sum_{i<j}\iint_{t+u\le1}d\nu_i(t)d\nu_j(u)
\]

has the sharp lower envelope

\[
F(A)=
\begin{cases}
A^2/2,&A\le1,\\
A-1/2,&1\le A\le2,\\
A^2/2-A+3/2,&2\le A\le3.
\end{cases}
\]

The Ferrers compression proof is valid.  The complement duality

\[
E(dt-\nu_1,dt-\nu_2,dt-\nu_3)=E(\nu)+3-2A
\]

independently checks the first and third branches.  The middle branch is
flat after one colour is filled, giving `E=A-1/2`.

In the paired broad limit, the physical absorbed-line inequality gives
`E<=1`; hence the middle branch forces `A<=3/2`.  The saving density
`b(t)=2+t-t^2` is symmetric and decreasing away from `1/2`.  Under total
density at most two and mass `A<=3/2`, the bathtub optimizer is density two
on `[1/8,7/8]`, yielding

\[
B\le423/128.
\]

The remaining arithmetic is

\[
2\int_0^1b(t)dt=13/3,
\qquad
5-(13/3-423/128)=1525/384=4-11/384.
\]

All limiting boundaries are harmless: domination by `dt` makes
`t+u=1` product-null; the nonreflected block and contracted gap moment
vanish; the strict `11/384` margin survives a diagonal choice of one small
fixed threshold.

Finally, with

\[
G_{w,q}=\int\min\{w\phi,q(p-1)\}\,d\rho,
\qquad
R_A=2f-\ell-\tau_A-\iota_A,
\]

the common-weight envelope follows directly from the seamwise dichotomy
`w phi` (nonabsorbed) versus `q t>=q(p-1)` (absorbed), followed by exact
substitution of the absorbed-line slack.  No independently optimized
threshold coupling is introduced.

## Exact boundary of the result

The proof rules out the displayed paired coupling, including every partial
choice of absorbed seams and directions.  It leaves open arbitrary mixed
length couplings, positive gap mass, and the integrated control of

\[
\int q(c)(\iota_A(c)+R_A(c))dc
\]

along one common physical edge-lifetime process.
