# Multi-order flags: exact fractional factor, protected rankwise marginals, and the chain-integrality gate

**Date:** 2026-08-01  
**Status:** unconditional selector-level theorems, superseded on the
unrestricted integrality row by
`MATH_THEOREM_SCD_EXACT_ALL_HIGH_ORDERED_CHAIN_SELECTOR_AND_PROTECTED_GATE_20260801.md`.
The all-high flag host has
an exact symmetric fractional named-target factor; a bounded protected root
bank can be frozen under an explicit sharp top-facet condition; and after
deleting any bounded protected bank, every high rank separately still has an
integral containment matching.  A matching exponential upper bound for a
global-order support menu is also proved.  This note did not prove the common
nested-chain selector; the later SCD theorem does.  Its matrix is nevertheless
non-TU at two suffix levels.  No
additive-constant upper bound is claimed.

## 0. Outcome

Write

\[
                         k=2m+1,
 \qquad {\cal R}=\binom{[k]}m,
 \qquad W=|{\cal R}|,
\]

and fix a depth \(d\ge2\).  An all-high flag at a root \(q\in{\cal
R}\) is determined by an ordered \((d-1)\)-tuple of distinct elements of
\(q\).  It supplies one nested suffix at every rank

\[
                         m-1,m-2,\ldots,m-d+1.                 \tag{0.1}
\]

The exact conclusions are as follows.

1. Choosing a local order uniformly at every root gives every fixed
   rank-\(t\) target total fractional availability

   \[
                    {W\over\binom kt}.                         \tag{0.2}
   \]

   Since this is at least one for \(t<m\), independent marking thins it
   to exact target load one.  Thus the complete all-high flag host has an
   explicit rational exact fractional named-target factor at all high ranks
   simultaneously.

2. If a protected root bank \({\cal P}\) is frozen and every unprotected
   root remains uniformly ordered, a target \(T\) of rank \(m-j\) has
   availability at least one whenever

   \[
       |\{p\in{\cal P}:T\subset p\}|
       \le \binom{m+j+1}j-\binom mj.                            \tag{0.3}
   \]

   For a bounded bank, the only asymptotically nonautomatic row is \(j=1\):
   no unmarked facet may lie in more than two protected roots.  In
   particular, two arbitrary protected flags can always be frozen, and any
   fixed bank with no triple common facet can be frozen.

3. Much more is true rankwise.  After deleting any \(h\) protected roots,
   the rank-\((m-j)\)-to-rank-\(m\) containment graph still has a matching
   saturating every rank-\((m-j)\) target whenever

   \[
                          h\le\binom{m+j+1}j-1.                 \tag{0.4}
   \]

   Hence every fixed protected bank is harmless at every high rank
   separately.

4. The exponential order-menu obstruction is sharp up to a polynomial
   factor.  The bottom rank forces

   \[
      |\Pi|\ge
      {\binom{2m+1}{d-1}\over\binom{m+d}{d-1}}
      =2^{d-1}\exp\!\left(-O(d^2/m)\right),                     \tag{0.5}
   \]

   while

   \[
      |\Pi|=O\!\left(m2^d\exp(O(d^2/m))\right)                 \tag{0.6}
   \]

   random global orders suffice simultaneously at every rank in (0.1).

5. These marginal results do not round to one-copy flags by TU.  With only
   the top two proper suffix ranks, the exact selector matrix contains the
   determinant-two minor

   \[
                \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix}. \tag{0.7}
   \]

The remaining object is therefore an **ordered-chain transversal**, not a
collection of independent containment matchings.

## 1. Local flags and their suffix chains

For a root \(q\in{\cal R}\), let

\[
             f=(q;z_1,z_2,\ldots,z_{d-1})                       \tag{1.1}
\]

be an ordered tuple of distinct elements of \(q\).  Define

\[
             T_j(f)=q-\{z_1,\ldots,z_j\},
             \qquad 1\le j\le d-1.                              \tag{1.2}
\]

Then \(|T_j(f)|=m-j\) and

\[
                   T_{d-1}(f)\subset\cdots\subset T_1(f)\subset q.
                                                                    \tag{1.3}
\]

Every such local flag is induced by some total order on \([k]\).  A global
order menu is more restrictive because the same total order must induce its
flags at every root.

### Lemma 1.1 (uniform local suffix law)

Choose the order of a fixed root \(q\) uniformly.  For a fixed
\((m-j)\)-set \(T\subset q\),

\[
                         \Pr[T_j(f)=T]={1\over\binom mj}.        \tag{1.4}
\]

#### Proof

The first \(j\) positions of a uniform order form a uniform \(j\)-subset
of \(q\).  Equation (1.2) equals \(T\) precisely when that subset is
\(q-T\). \(\square\)

## 2. The smallest exact flag-selector LP

For each root \(q\) and local flag \(f\) at \(q\), introduce a flag variable
\(x_f\).  For each \(1\le j<d\), introduce a mark variable \(y_{f,j}\).
The selector-level fractional system is

\[
 \sum_{f:\operatorname{root}(f)=q}x_f=1
                    \qquad(q\in{\cal R}),                       \tag{2.1}
\]

\[
 0\le y_{f,j}\le x_f,                                           \tag{2.2}
\]

and

\[
 \sum_{f:T_j(f)=T}y_{f,j}=1
 \quad\left(T\in\binom{[k]}{m-j},\ 1\le j<d\right).            \tag{2.3}
\]

A protected flag \(f_p\) at root \(p\) is imposed by

\[
                          x_{f_p}=1.                             \tag{2.4}
\]

The integral system adds \(x_f,y_{f,j}\in\{0,1\}\).  It chooses one flag
per root and one occurrence of every named target.  The same chosen flag
must realize all selected ranks, which is the only cross-rank coupling in
(2.1)--(2.3).

There is no hidden constraint on which subsets of ranks may be marked on
one fractional flag.  Given any numbers \(0\le y_{f,j}\le x_f\), divide
the mass \(x_f\) among mark subsets by independent Bernoulli choices with
probabilities \(y_{f,j}/x_f\).  Thus (2.1)--(2.3) is exactly the projected
marked-flag polytope, not a relaxation caused by forgetting mark
correlations.

Physical successor turns, Euler balance, residence, and upper shadows are
additional constraints outside this selector-level system.

## 3. Exact symmetric fractional factor

Put

\[
        D_j=\binom{m+j+1}j,
        \qquad A_j={D_j\over\binom mj}.                           \tag{3.1}
\]

Here \(D_j\) is the number of rank-\(m\) roots containing a fixed
rank-\((m-j)\) target.

### Theorem 3.1 (uniform fractional all-high factor)

The system (2.1)--(2.3) has an explicit rational solution.  Choose the
local flag uniformly at every root.  If \(T_j(f)=T\), set

\[
                           y_{f,j}={x_f\over A_j}.                \tag{3.2}
\]

Then every target row has load exactly one.

#### Proof

By Lemma 1.1, a fixed target \(T\) has total available mass

\[
 {D_j\over\binom mj}=A_j.
\]

The binomial identity

\[
 {\binom{m+j+1}j\over\binom mj}
 = {\binom{2m+1}m\over\binom{2m+1}{m-j}}
 = {W\over\binom{k}{m-j}}                                      \tag{3.3}
\]

is the symmetric target marginal.  It is greater than one for \(j\ge1\),
so (3.2) is legal and gives target load one. \(\square\)

The theorem is simultaneous over all \(j\).  It is an exact finite rational
solution, obtained either from all local orders or by averaging all global
orders.  It removes every rank-count and symmetric fractional separator
from the multi-order flag problem.

## 4. Protected fractional flags

Let \({\cal P}\subset{\cal R}\) be a protected root bank.  Freeze an
arbitrary local flag at each root in \({\cal P}\), put zero marks on those
protected masses, and order every root outside \({\cal P}\) uniformly.
For a target \(T\in\binom{[k]}{m-j}\), put

\[
                  c_{\cal P}(T)=|\{p\in{\cal P}:T\subset p\}|.  \tag{4.1}
\]

Its remaining availability is

\[
              a_T={D_j-c_{\cal P}(T)\over\binom mj}.             \tag{4.2}
\]

### Theorem 4.1 (protected symmetric thinning)

If

\[
 c_{\cal P}(T)\le E_j:=D_j-\binom mj                            \tag{4.3}
\]

for every high target \(T\) of rank \(m-j\), then (2.1)--(2.4) has an
exact fractional solution.  Namely, on every unprotected flag with
\(T_j(f)=T\), set

\[
                         y_{f,j}={x_f\over a_T}.                 \tag{4.4}
\]

#### Proof

Condition (4.3) is exactly \(a_T\ge1\).  Hence (4.4) respects (2.2), and
the sum over all occurrences of \(T\) is one.  The root equations are
unchanged. \(\square\)

The top value is sharp:

\[
                             E_1=2.                              \tag{4.5}
\]

Moreover

\[
 E_2=3m+3,
 \qquad E_{j+1}>E_j\quad(j\ge1),                                \tag{4.6}
\]

because

\[
 E_{j+1}-E_j
 =\binom{m+j+1}{j+1}-\binom m{j+1}+\binom mj>0.                 \tag{4.7}
\]

Therefore:

* any two arbitrary protected flags may be frozen;
* any fixed protected bank for which no rank-\((m-1)\) target lies in
  three protected roots may be frozen for all sufficiently large \(m\);
* for a general bounded bank, the naive ``deterministic protected plus
  uniform unprotected'' solution can fail only at the top facet row.

The last bullet is a statement about this explicit symmetric conditioning,
not a no-go for a nonuniform protected solution.

## 5. Every protected rank projection is integrally feasible

The preceding conditioning theorem is fractional and keeps one common flag
distribution.  If the ranks are separated, one can say more.

### Lemma 5.1 (strict shadow surplus)

Let \(r=m+1\), \(1\le j\le m\), and
\({\cal F}\subseteq\binom{[2m+1]}{r+j}\) be nonempty.  Its \(j\)-step
lower shadow satisfies

\[
 |\partial_j^-{\cal F}|
 \ge |{\cal F}|+\binom{r+j}j-1.                                 \tag{5.1}
\]

#### Proof

Write \(|{\cal F}|=\binom{x}{r+j}\) with real \(x\ge r+j\).  The Lovasz
form of Kruskal--Katona gives

\[
                    |\partial_j^-{\cal F}|\ge\binom xr.         \tag{5.2}
\]

It remains to minimize

\[
 g_j(x)=\binom xr-\binom{x}{r+j}
       =\sum_{a=r}^{r+j-1}\left(\binom xa-\binom{x}{a+1}\right) \tag{5.3}
\]

on \(r+j\le x\le2r-1\).  Each summand is

\[
 \binom xa{2a+1-x\over a+1}.                                   \tag{5.4}
\]

Its logarithmic derivative is

\[
 \sum_{i=0}^{a-1}{1\over x-i}-{1\over2a+1-x}
 \ >\ {a\over x}-{1\over2}\ >0,                               \tag{5.5}
\]

because \(a\ge r\) and \(x\le2r-1\).  Thus \(g_j\) is increasing, and
at \(x=r+j\) it equals \(\binom{r+j}j-1\).  Equations (5.2)--(5.5) prove
(5.1). \(\square\)

### Theorem 5.2 (protected rankwise containment matching)

Fix \(j\ge1\), and delete any \(h\) rank-\(m\) roots.  If

\[
                          h\le D_j-1,                            \tag{5.6}
\]

then every rank-\((m-j)\) target can be matched injectively to a remaining
rank-\(m\) root containing it.

#### Proof

Complementation sends a family \({\cal X}\) of rank-\((m-j)\) targets
to a family of rank-\((m+1+j)\) sets, and its root neighbourhood to the
\(j\)-step lower shadow.  Lemma 5.1 gives

\[
                         |N({\cal X})|\ge|{\cal X}|+D_j-1.       \tag{5.7}
\]

After deleting \(h\) roots, at least \(|{\cal X}|\) neighbours remain.
Hall's theorem proves the claim. \(\square\)

Since \(D_1=m+2\), any fixed protected bank is harmless at every high rank
separately.  Applying Theorem 5.2 for all \(j\) gives exact integral
rankwise matchings.  It does **not** order the matched targets at one root
into one nested flag.  That correlation is the remaining selector gate.

## 6. Global-order menu size is now sharp up to a polynomial

The bottom-suffix theorem already proves the lower bound (0.5).  There is a
matching probabilistic upper bound which works at all high ranks at once.

### Theorem 6.1 (simultaneous random-order cover)

There is a family \(\Pi\) of

\[
                 O\!\left(m2^d\exp(O(d^2/m))\right)             \tag{6.1}
\]

total orders such that every target of every rank
\(m-1,\ldots,m-d+1\) occurs as the corresponding terminal suffix under at
least one order-induced flag.  Any fixed prepared total order may be added
to the family.

#### Proof

Fix \(j\in\{1,\ldots,d-1\}\) and
\(T\in\binom{[2m+1]}{m-j}\).  It is realizable under a global order if the
first \(j\) coordinates avoid \(T\).  For a uniform random total order this
has probability

\[
 p_j={\binom{m+j+1}j\over\binom{2m+1}j}
    =2^{-j}\exp(O(j^2/m)).                                      \tag{6.2}
\]

Uniformly for \(j<d=o(m)\),

\[
 p_j\ge2^{-j}\exp(-O(j^2/m)).                                  \tag{6.3}
\]

With \(L\) independent orders the probability that a fixed pair \((j,T)\)
is missed is at most \(e^{-Lp_j}\).  There are at most
\(d2^{2m+1}\) such pairs.  Taking

\[
 L=O\!\left(m2^d\exp(O(d^2/m))\right)                          \tag{6.4}
\]

makes the union bound smaller than one. \(\square\)

For \(d=\Theta(\sqrt m)\), (0.5) and (6.1) differ only by a polynomial
factor in \(m\).  The support problem is therefore quantitatively settled.
Multiplicity balance inside one restricted global-order menu is not settled
here.  Unrestricted one-copy chain correlation is settled by the later SCD
theorem.

## 7. The first cross-rank minor is not TU

Assume \(d\ge3\).  Choose

\[
 S\in\binom{[k]}{m-2},\qquad b\notin S,\qquad
 T=S\cup\{b\}.                                                  \tag{7.1}
\]

Choose \(a\notin T\), \(c\in S\), and \(x\notin T\cup\{a\}\).  Put

\[
 q=S\cup\{a,b\},\quad q'=T\cup\{x\},\quad
 S'=T-\{c\},\quad T'=S\cup\{a\}.                              \tag{7.2}
\]

There are three local flags:

* \(f_1\) at \(q'\), beginning with \(x,b\), whose two suffixes are
  \(T,S\);
* \(f_2\) at \(q\), beginning with \(a,c\), whose two suffixes are
  \(T,S'\);
* \(f_3\) at \(q\), beginning with \(b,a\), whose two suffixes are
  \(T',S\).

On the three constraint rows \(S,T,q\), their incidence columns are

\[
 \begin{array}{c|ccc}
       &f_1&f_2&f_3\\ \hline
 S     &1&0&1\\
 T     &1&1&0\\
 q     &0&1&1
 \end{array}                                                    \tag{7.3}
\]

and the determinant is two.

### Corollary 7.1

The ordered-chain selector matrix is not totally unimodular as soon as two
proper suffix ranks are coupled.  The subsystem (7.3) with all three row
requirements equal to one has the unique solution

\[
                         x_{f_1}=x_{f_2}=x_{f_3}=1/2,            \tag{7.4}
\]

and no integral solution if structural zeros isolate these columns.

This does not prove that the complete flag selector is infeasible.  It
proves that rankwise containment matching, Birkhoff decomposition, and a
bare TU argument cannot perform the required common rounding.

## 8. Corrected remaining theorem

The unrestricted ordered-chain transversal below is solved by the later SCD
theorem.  The remaining selector statement is its protected physical
strengthening:

> **Protected transition-compatible ordered-chain transversal.**  Start
> from an exact SCD flag factor, retain the prescribed flags on the bounded
> prepared bank, and modify it without changing named target multiplicities
> so that the selected literal flags admit the required balanced owner/turn
> circulation.

The preceding results remove four possible obstructions:

* the complete host has the exact symmetric fractional marginals;
* an explicit class of bounded prepared banks preserves those marginals;
* arbitrary bounded protected-root deletion is harmless in every rankwise
  containment projection;
* an order menu within a polynomial factor of the information-theoretic
  minimum supports all targets at all high ranks.

Unrestricted one-copy chain-correlated rounding is now solved.  The
unresolved statement is **protected physical correlation**, followed by the
turn/Euler and upper-shadow gates.  The determinant-two minor rules out a
bare TU proof but is not an existence obstruction in the complete host.
