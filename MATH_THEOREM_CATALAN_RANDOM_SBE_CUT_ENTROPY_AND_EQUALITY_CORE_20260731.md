# Random SBE orientation: exact Rademacher cuts, conditional entropy theorem, and the min-cut-counting obstruction

Date: 2026-07-31  
Status: exact all-parameter random-slack identity; rigorous union-bound and
lopsided-LLL sufficient theorems; exact authenticated cut audit through
parameter seven.  No unconditional all-parameter SBE-orientation theorem is
claimed.

## 0. Verdict

Independent random orientation is a useful final rounding step only after a
deterministic small-slack core has been controlled.  It is not, by itself, a
proof of simultaneous upper/lower SBE.

For every closed SBE cut `A`, its random slack has the exact form

\[
             L_A(X)=m(A)+{C\over2}
                    \sum_{i\in J(A)}\epsilon_i(A)X_i,            \tag{0.1}
\]

where the `X_i` are independent signs, `J(A)` is the set of path endpoint
pairs split by the cut, and `m(A)>=0` is precisely the half-endpoint
(midpoint) slack.  Thus the relevant scale is

\[
                 {2m(A)\over C\sqrt{|J(A)|}},                    \tag{0.2}
\]

not merely whether the midpoint min-cut is feasible.

This distinction is load-bearing.  On the authenticated parameter-three
seed, the midpoint is feasible but no one of the eight orientations is SBE.
The contradictory cuts have positive mean slack smaller than one endpoint
step.  Even the separate literal fixture with
`eta^-=eta^+=3` has exactly **one** successful orientation out of `32`.
Therefore neither midpoint feasibility nor facet slack three implies a
high-probability random rounding.

There is, however, a clean conditional theorem.  After fixing every
zero/small-slack row that needs deterministic treatment, independent random
orientation of the remaining paths succeeds whenever the exact sum of the
binomial cut tails is below one.  A cut-entropy bound or an asymmetric
lopsided local lemma gives usable sufficient forms below.

Ordinary Karger cut counting cannot supply the missing entropy estimate for
free.  The SBE oracle is a directed `s-t` closure network, and even an
undirected `s-t` network can have `2^K` minimum cuts.  Benczur--Karger
concentration concerns independent edge sampling, whereas one endpoint bit
moves a full amount `C` between a paired pair of sink arcs.  A positive
all-parameter theorem must prove a special low-entropy/small-dependency
property of the recursively supplied occurrence cuts.

## 1. Exact random-slack identity

Fix one strict shore and its middle ground set `X`.  Let the nontrivial path
endpoint blocks be

\[
                         E_i=\{u_i,v_i\},qquad i=1,\ldots,K_1, \tag{1.1}
\]

and let `I` be the isolated child vertices.  Choose independent Rademacher
variables `X_i in {-1,+1}`.  The sign convention is arbitrary on one shore;
on the opposite shore the selected endpoint is complementary, so all signs
are reversed after the appropriate endpoint relabelling.

For a middle set `A subseteq X`, put

\[
\begin{aligned}
 a(A)&=|I\cap A|+|\{i:E_i\subseteq A\}|,\\
 J(A)&=\{i:|E_i\cap A|=1\},\qquad b(A)=|J(A)|.         \tag{1.2}
\end{aligned}

For `i in J(A)`, choose `epsilon_i(A) in {-1,+1}` so that the indicator that
the selected terminal lies in `A` is

\[
                    {1+\epsilon_i(A)X_i\over2}.                  \tag{1.3}
\]

Recall the closed-neighbourhood demand

\[
       g^\sigma(A)=N|O^\sigma(A)|-R|A|.                         \tag{1.4}
\]

### Theorem 1.1 (Rademacher representation)

The scaled SBE slack of `A` is exactly

\[
\begin{aligned}
 L_A^\sigma(X)
 &=C|Z^\sigma(X)\cap A|-g^\sigma(A)\\
 &=m^\sigma(A)+{C\over2}
       \sum_{i\in J(A)}\epsilon_i^\sigma(A)X_i,                 \tag{1.5}\\
 m^\sigma(A)
 &=C\left(a(A)+{b(A)\over2}\right)-g^\sigma(A).                \tag{1.6}
\end{aligned}

The shore is SBE if and only if (1.5) is nonnegative for every `A`.  The
half-endpoint point is SBE if and only if `m^sigma(A)>=0` for every `A`.

#### Proof

Every isolated vertex and every block wholly contained in `A` contributes
one terminal.  Every split block contributes (1.3), and every disjoint block
contributes zero.  Summing these terms and subtracting (1.4) proves
(1.5)--(1.6).  The terminal-cover theorem identifies nonnegativity of all
these rows with SBE.  Taking expectations removes the signed sum, proving
the final assertion. `square`

The doubled midpoint slack

\[
                         s_2(A)=2m(A)                            \tag{1.7}

\]

is integral.  Reversing one split endpoint changes doubled slack by exactly
`2C`; equivalently its contribution to ordinary slack changes by `C` and
its deviation from the midpoint is `C/2`.

## 2. Equality, robust rows, and exact binomial tails

If `b(A)=0`, the row is deterministic.  Midpoint feasibility already proves
it for every orientation.  If `b(A)>0`, define

\[
 q(A)=\left\lceil {b(A)\over2}-{m(A)\over C}\right\rceil-1.     \tag{2.1}

### Proposition 2.1 (exact one-row failure probability)

Under independent uniform orientation,

\[
 p(A):=\Pr(L_A(X)<0)
 =2^{-b(A)}\sum_{j=0}^{\min\{b(A),q(A)\}}\binom{b(A)}j,          \tag{2.2}

\]

where the sum is zero when `q(A)<0`.  For `m(A)>0`,

\[
                      p(A)\le
       \exp\left(-{2m(A)^2\over C^2b(A)}\right).                \tag{2.3}

If `m(A)>=Cb(A)/2`, then `p(A)=0`: the row is valid for every orientation.

#### Proof

After changing signs, the number of positive selected literals is a
`Bin(b,1/2)` random variable `Y`.  Equation (1.5) fails precisely when

\[
                         Y<{b\over2}-{m\over C},                 \tag{2.4}

\]

which is (2.1)--(2.2).  Hoeffding's inequality gives (2.3), and the maximum
possible negative midpoint deviation is `Cb/2`. `square`

When `m=0` and `b>0`, the exact probability is approximately one half (and
is exactly `(1-P(Y=b/2))/2` for even `b`).  Such equality rows cannot be
buried inside a generic concentration estimate.  They must be satisfied by
a deterministic orientation core, or shown to have a jointly compatible
special structure.

## 3. Rigorous conditional existence theorems

Different middle sets may give the same signed boundary row.  Retain only
the strongest demand for each signed row on each shore; call the resulting
finite family `mathcal R`.  This compression changes no Boolean feasible
orientation.

### Theorem 3.1 (exact cut-tail union theorem)

If

\[
                         \sum_{A\in\mathcal R}p(A)<1,            \tag{3.1}

\]

with `p(A)` given by (2.2), then a simultaneous upper/lower SBE orientation
exists.  It is enough that

\[
 \sum_{A\in\mathcal R:m(A)>0}
     \exp\left(-{2m(A)^2\over C^2b(A)}\right)<1,                 \tag{3.2}

\]

provided every row with `b=0` is feasible and every row with `m=0,b>0` has
already been discharged deterministically.

#### Proof

The bad event for row `A` has probability (2.2).  The union bound makes the
probability of any failed row smaller than one under (3.1).  Equation (3.2)
uses (2.3). `square`

The theorem persists after a partial deterministic orientation.  Substitute
the fixed signs into (1.5), add their contribution to `m(A)`, delete them
from `J(A)`, and apply Theorem 3.1 to the remaining independent signs.

### Corollary 3.2 (cut-entropy/margin criterion)

Suppose the number `H_b` of retained rows of boundary width `b`, over both
shores together, satisfies

\[
                         H_b\le A e^{\eta b},                    \tag{3.3}

\]

and every such row has

\[
                         m(A)\ge\theta Cb.                       \tag{3.4}

\]

Put `a=2theta^2-eta`.  If `a>0` and

\[
                         {A e^{-a}\over1-e^{-a}}<1,              \tag{3.5}

\]

then a simultaneous SBE orientation exists.

#### Proof

Equations (2.3)--(3.4) bound the total contribution at width `b` by
`A exp(-(2theta^2-eta)b)`.  Sum the geometric series. `square`

This is the precise form a Karger-style argument would have to establish:
not merely polynomially many global near-mincuts, but an entropy bound on
the **signed endpoint-boundary rows** together with linear midpoint margin.

### Theorem 3.3 (lopsided dependency criterion)

Let two retained rows be adjacent when their remaining random boundary sets
intersect.  If numbers `x_A in (0,1)` exist with

\[
 p(A)\le x_A\prod_{B:\,J(A)\cap J(B)\ne\varnothing}(1-x_B)
                                                                  \tag{3.6}
\]

for every row, then a simultaneous SBE orientation exists.  In particular,
if all row probabilities are at most `p` and the dependency degree is at
most `Delta`, the sufficient condition

\[
                         e p(\Delta+1)\le1                       \tag{3.7}

\]

is valid.

#### Proof

Each row event is a function only of the independent signs indexed by its
boundary.  Events with disjoint boundaries are independent.  The asymmetric
Lovasz local lemma gives (3.6), and its symmetric form gives (3.7). `square`

Again, (3.6) is useful only after the zero/small-margin core has been
controlled.  A width-one row with `m<C/2` has failure probability `1/2` and
cannot tolerate a nontrivial dependency neighbourhood.

## 4. Why generic Karger/Benczur--Karger does not close the gate

Karger's polynomial near-mincut counting theorem concerns global undirected
cuts.  The SBE separation network is a directed closure network with fixed
source and sink.  Even the undirected `s-t` analogue has no polynomial
minimum-cut count.

Take `K` internally disjoint length-two paths

\[
                         s-u_i-t\qquad(i=1,\ldots,K),             \tag{4.1}

\]

with unit edges.  The minimum `s-t` cut has order `K`, and independently
choosing the first or second edge on every path gives exactly `2^K` distinct
minimum cuts.  This is the same combinatorial freedom as paired endpoint
arcs.

Benczur--Karger sampling also does not match (1.5).  It independently keeps
or rescales edges and preserves a cut in proportion to its total capacity.
Endpoint rounding instead transfers an indivisible capacity `C` between two
paired sink arcs.  A cut with midpoint margin below `C/2` can be destroyed by
one bit even when its total network cut has order `NP`.

Therefore any successful cut-counting proof must use additional Boolean
geometry of the recursively supplied occurrence graph—for example a bound
on the entropy of small-margin signed boundary rows.  Neither the ordinary
min-cut value nor `eta>=3` supplies that property.

## 5. Authenticated finite profile

The independent audit described in Section 6 gives the following exact
facts.

\[
\begin{array}{c|c|cc|cc|c}
\text{fixture}&K_1&
 \multicolumn{2}{c|}{\min s_2\text{ under a directed split}}&
 \multicolumn{2}{c|}{\#\text{ zero-slack split directions}}&
 \text{both-SBE orientations}\\
& & \text{upper}&\text{lower}&\text{upper}&\text{lower}&\\ \hline
\text{chain }n=3&3&2&6&0&0&0/8\\
\text{chain }n=4&10&42&42&0&0&475/1024\\
\text{chain }n=5&33&132&132&0&0&\text{not exhausted}\\
\text{chain }n=6&114&429&429&0&0&\text{not exhausted}\\
\text{chain }n=7&386&1430&1430&0&0&\text{not exhausted}\\
\eta^-=\eta^+=3, n=3&5&6&6&0&0&1/32.
\end{array}                                                     \tag{5.1}
\]

Here `s_2=2m` is doubled midpoint slack, and

\[
                  C=14,42,132,429,1430                           \tag{5.2}

\]

at chained parameters `3,...,7`.  Since every directed split was tested,
the zero columns in (5.1) prove that **every zero-midpoint-slack cut is
orientation-deterministic** on all six fixtures.  The dangerous rows have
small positive mean slack.

* On the chained `n=3` seed, the midpoint passes on both shores but all eight
  orientations fail.  Every directed endpoint split has a positive-slack
  minimum cut; the obstruction is therefore **small positive margin**, not a
  nondeterministic equality cut.
* On the chained `n=4` child, exactly `475/1024` orientations pass both
  shores, reproducing the earlier census.  The same audit continues the
  midpoint and forced-split profile through `n=5,6,7`.
* On the separate literal `eta^-=eta^+=3` five-path fixture, exactly `1/32`
  orientations passes both shores.  Facet margin three therefore does not
  imply random-orientation robustness.

The numerical violating-mincut spectra sharpen that warning.  At `n=4`, the
upper failed-orientation witnesses have boundary widths `2,...,9`; their
smallest observed Hoeffding exponent is `4/9`, below the forced-split minimum
`1/2`.  The lower witnesses have minimum exponent `4/3`.  On the `eta=3`
fixture both shores have minimum observed exponent `9/196` and eleven
distinct failed-orientation mincut witnesses.  These are exact finite
measurements, not an asymptotic law.  A forced split minimizes ordinary
midpoint slack subject to one endpoint direction; it need not minimize the
normalized risk `m/sqrt(b)`.  The `n=4` census explicitly shows why those
objectives must not be conflated.

## 6. Independent audit

The dependency-free script

```text
scratch/audit_catalan_sbe_random_cut_profile_n3_n7_20260731.py
```

authenticates the chained witness, reconstructs both occurrence graphs at
`n=3,...,7`, and for each shore:

1. verifies exact midpoint feasibility by doubled integral max flow;
2. represents the complete minimum-cut lattice by the residual SCC DAG;
3. tests every directed endpoint split for a zero-slack cut;
4. computes an exact minimum-midpoint-slack cut under every forced split;
5. records its boundary width, worst integral buffer, and Hoeffding exponent;
6. exhausts all orientations at `n=3,4`, independently separates every
   failed orientation, and records distinct violating cut witnesses; and
7. repeats the exact orientation census on the literal `eta=3` fixture.

The forced-split list is canonical but is not an enumeration of every member
of an exponentially large minimum-cut lattice.  All promoted existence and
nonexistence counts use exact min-cut separation, not only that list.

The final hashes are

```text
script   fd8d3bcd3d223499d9ad36f9cecbf468fd699f7d54dab0c8d3c4159d99276fe0
JSON     42eda26e1b53cb02a67e3074f7a761e45b67afffd4022d1de9e66fccf46c104c
payload  c6568419d26cf7c91ad0ce3b80dc2a5f069b17f258bbb8a3700045a054c203f6
```
