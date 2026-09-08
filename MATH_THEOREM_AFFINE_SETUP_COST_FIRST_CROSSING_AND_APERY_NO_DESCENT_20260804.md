# Affine setup-cost clocks: an exact obstruction to first-crossing size descent

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem and counterexample to a
structural induction method.  It constructs, in every grid size, a
first-crossing endpoint-saturated table whose entire lower support is
indispensable but whose endpoint is inert.  Its Apéry recursion has smaller
displayed support but a subthreshold period, and first-crossing extension
returns the original grid size.  The theorem does **not** assert that these
clocks have nonpositive Bellman functional.

Put

\[
                         A={\sqrt\pi\over2},
\]

and let `K` be the Rayleigh signed-tail kernel.

## 1. Endpoint saturation has complementary-pair geometry

Let

\[
 0=c_0\le c_1\le\cdots\le c_n
\]

be internally superadditive.  Let `P_n` be the best value of a partition
of capacity `n` using only denominations smaller than `n`.

### Lemma 1.1

For every `n>=2`,

\[
 \boxed{
 P_n=\max_{1\le i\le n-1}(c_i+c_{n-i}).
 }
\tag{1.1}
\]

Consequently endpoint saturation is exactly

\[
 c_n'=\max\left\{A,\max_{1\le i\le n-1}(c_i+c_{n-i})\right\}.
\tag{1.2}
\]

#### Proof

Every displayed pair is an admissible lower-denomination partition of
`n`, proving one inequality.  Conversely, take any lower partition

\[
                         n=j_1+\cdots+j_t,qquad t\ge2.
\]

Repeated internal superadditivity gives

\[
 c_{j_2}+\cdots+c_{j_t}\le c_{n-j_1}.
\]

Thus its value is at most `c_{j_1}+c_{n-j_1}`, which is bounded by the
right side of (1.1).  This proves equality. \(\square\)

For `n=5`, (1.2) has the threshold face and two unordered inert faces.
For `n=6`, it has the threshold face and the three unordered inert faces

\[
 c_6=A,qquad c_6=c_1+c_5,qquad c_6=c_2+c_4,qquad c_6=2c_3.
\tag{1.3}
\]

The third complementary face is new at grid six.

## 2. The affine setup-cost family

Fix an integer `n>=3` and a parameter

\[
                         0<\beta<{A\over n-2}.
\tag{2.1}
\]

Set

\[
 \alpha={A+2\beta\over n},
\tag{2.2}
\]

and define

\[
 c_0=0,qquad
 c_j=\alpha j-\beta\quad(1\le j<n),qquad
 c_n=A=\alpha n-2\beta.
\tag{2.3}
\]

The value `beta` is a fixed setup cost paid by each lower part.  The
endpoint pays two setup costs, exactly matching every two-part
complementary partition.

### Theorem 2.1

The table (2.3) has all of the following properties.

1. It is strictly increasing and internally superadditive.
2. Its first displayed threshold crossing is exactly at slot `n`.
3. It is endpoint-saturated, with

   \[
   P_n=A,
   \]

   and every two-part complementary partition attains `P_n`.
4. Every denomination `j<n` is indispensable at its own capacity: after
   deleting it, the best exact fill of capacity `j` has value strictly
   smaller than `c_j`.
5. The endpoint denomination is Bellman-inert.
6. The unique maximum-density denomination is `h=n-1`.
7. The exact Bellman clock is

   \[
   \boxed{
   V_m=\alpha m-\beta\left\lceil{m\over n-1}\right\rceil
   \qquad(m\ge0).
   }
   \tag{2.4}
   \]

#### Proof

Condition (2.1) gives

\[
 c_1=\alpha-\beta={A-(n-2)\beta\over n}>0.
\tag{2.5}
\]

The lower entries increase by `alpha`, while

\[
 c_n-c_{n-1}=\alpha-\beta=c_1>0.
\]

Thus the table is strictly increasing.  If `i,j>=1` and `i+j<n`, then

\[
 c_{i+j}=c_i+c_j+\beta>c_i+c_j.
\tag{2.6}
\]

If `i+j=n`, then

\[
 c_n=\alpha n-2\beta=c_i+c_j.
\tag{2.7}
\]

These are all internal superadditivity inequalities.

Equation (2.5) also gives

\[
 c_{n-1}=A-c_1<A,
\]

so every lower displayed value is below `A`, while `c_n=A`.  This proves
the first-crossing assertion.

Any lower partition of `n` into `t>=2` parts has value

\[
                         \alpha n-t\beta\le\alpha n-2\beta=A,
\tag{2.8}
\]

with equality for every two-part partition.  Hence `P_n=A`, proving
saturation and endpoint inertness.

Similarly, a partition of `j<n` not using denomination `j` has at least
two parts and therefore has value at most

\[
 \alpha j-2\beta=c_j-\beta<c_j.
\tag{2.9}
\]

Thus every lower denomination is indispensable.

For `j<n`,

\[
 {c_j\over j}=\alpha-{\beta\over j}
\]

is strictly increasing in `j`.  Moreover

\[
 {c_{n-1}\over n-1}-{c_n\over n}
 ={\beta(n-2)\over n(n-1)}>0.
\tag{2.10}
\]

Thus `n-1` is the unique maximum-density denomination.

It remains to compute the clock.  Replace every endpoint part of size `n`
by any two complementary lower parts.  Capacity and value are unchanged,
so it is enough to optimize over parts of size at most `n-1`.  A partition
of capacity `m` into `t` such parts has value

\[
                         \alpha m-t\beta.
\]

Since `beta>0`, one minimizes `t`.  Writing

\[
                         m=q(n-1)+r,qquad0\le r<n-1,
\]

shows that the minimum number of parts is
`ceil(m/(n-1))`: use `q` parts of size `n-1`, and, when `r>0`, one part of
size `r`.  This proves (2.4). \(\square\)

## 3. Exact Apéry recursion and the no-descent cycle

Put

\[
 h=n-1,qquad P=c_h=\alpha h-\beta=A-c_1<A.
\tag{3.1}
\]

For `m=qh+r`, `0<=r<h`, formula (2.4) becomes

\[
 \boxed{
 V_{qh}=qP,qquad
 V_{qh+r}=qP+c_r\quad(1\le r<h).
 }
\tag{3.2}
\]

Thus there is no availability head at all.  The maximum-density Apéry
table is exactly

\[
                         (0,c_1,\ldots,c_{h-1},P),
\tag{3.3}
\]

which is the original lower prefix.  Its displayed endpoint is below the
Gaussian threshold, but its first carry crosses exactly at the next
capacity:

\[
                         P+c_1=A.
\tag{3.4}
\]

### Corollary 3.1 (no structural first-crossing descent)

For the family (2.3):

1. deleting dominated denominations removes only the inert endpoint;
2. the remaining `(n-1)`-denomination clock still first crosses `A` at
   capacity `n`;
3. adjoining that first crossing restores the original table exactly;
4. replacing the clock by its formal maximum-density Apéry table gives
   the same subthreshold prefix (3.3), and first-crossing extension again
   restores the original table.

Moreover, no internally superadditive first-crossing table of grid size at
most `n-1` and displayed endpoint at least `A` can have this Bellman clock.

#### Proof

The first four assertions follow from Theorem 2.1 and (3.1)--(3.4).  For
the last assertion, suppose a clock-equivalent first-crossing table had
grid size `m<=n-1`.  Internal superadditivity makes its Bellman value at
capacity `m` equal to its displayed endpoint, hence at least `A`.  But
the clock (2.4) satisfies

\[
                         V_m=c_m<A\qquad(m<n),
\]

a contradiction. \(\square\)

This proves that first-crossing deletion, endpoint saturation, inert
denomination deletion, and formal Apéry recursion do not by themselves
bound the grid size.  Any successful induction must add an analytic sign
principle for subthreshold Apéry periods or a genuinely non-clock-preserving
compression.

## 4. The first new grid: an exact five-coset carry gate at `n=6`

Take

\[
                         n=6,qquad
 \beta={A\over10},qquad \alpha={A\over5}.
\]

Then

\[
 \boxed{
 (c_0,\ldots,c_6)
 ={A\over10}(0,1,3,5,7,9,10).
 }
\tag{4.1}

The saturated endpoint lies simultaneously on all three inert faces:

\[
 c_1+c_5=c_2+c_4=2c_3=c_6=A.
\tag{4.2}

All five lower denominations are nevertheless indispensable.  Size five
is the unique maximum-density denomination, with the subthreshold period

\[
                         P=c_5={9A\over10}.
\tag{4.3}

The exact clock is

\[
 \boxed{
 V_m={A\over10}\left(2m-\left\lceil{m\over5}\right\rceil\right).
 }
\tag{4.4}

Consequently its functional is the explicit five-coset train

\[
\boxed{
\begin{aligned}
 \Phi_6=\sum_{q\ge0}\bigl(&K(9qA/10)+K((9q+1)A/10)\\
 &+K((9q+3)A/10)+K((9q+5)A/10)
 +K((9q+7)A/10)\bigr).
\end{aligned}}
\tag{4.5}

There is no finite transient to blame: the new geometry is entirely the
subthreshold period together with the carry `9A/10+A/10=A`.

More generally, in (2.3) choose

\[
 h=n-1,qquad
 \alpha={A\over h},qquad
 \beta={A\over2h}.
\tag{4.6}

Then, with `d=A/(2h)`,

\[
 V_m=d\left(2m-\left\lceil{m\over h}\right\rceil\right)
     =d\left\lfloor{(2h-1)m\over h}\right\rfloor.
\tag{4.7}

Thus the obstruction persists in every grid size as an exact rational
Beatty-type clock.

## 5. Exact missing lemma and scope

The already-proved positivity of first-crossing tables through grid five
cannot be applied to (4.5): its five-slot Apéry table has endpoint
`9A/10<A`, while first-crossing extension has grid six and returns (4.1).

Therefore any induction from the proved `n<=5` theorem must, at a minimum,
establish the new analytic inequality

\[
 \Phi_6>0
\tag{5.1}

for the train (4.5), or prove a broader **subthreshold Apéry carry lemma**
that contains it.  Finite-head estimates alone cannot supply that lemma,
because this family has an identically empty availability head.

This theorem is a rigorous obstruction to structural size descent, not a
counterexample to Bellman positivity.  It neither assigns a sign to
(4.5) nor proves that a minimal nonpositive table has this affine form.
It identifies the exact new grid-six phenomenon that a global induction
must control.
