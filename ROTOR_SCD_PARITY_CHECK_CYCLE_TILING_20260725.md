# Parity-check tilings by long-residence rotor cycles

Date: 2026-07-25

This note concerns the exact rotor--SCD route to coefficient one.  It gives
one positive integral construction and one sharp obstruction to using that
construction with a bounded library of coordinate orders.

## 1. Exact tiling of an orientation cube

Let \(\ell=2^h\), and write \(Q_\ell=\mathbb F_2^\ell\).  For a permutation
\(\pi\) of the coordinates, let \(C_\pi\) be the \(2\ell\)-cycle whose
transition word is

\[
 \pi(0),\pi(1),\ldots,\pi(\ell-1),
 \pi(0),\pi(1),\ldots,\pi(\ell-1).
 \tag{1.1}
\]

Every coordinate has cyclic transition gap exactly \(\ell\).  Hence, after
the standard fixed-pair interpretation, every cut copy of this cycle is a
genuine radius-\(H\) rotor run for every \(H<\ell\).

### Theorem 1.1 (linear translate tiling)

For every \(\ell=2^h\), there is a linear subspace

\[
 K\le \mathbb F_2^\ell,
 \qquad |K|={2^\ell\over 2\ell},
 \tag{1.2}
\]

such that the translates

\[
 \{C_{\rm id}+k:k\in K\}
 \tag{1.3}
\]

are pairwise vertex-disjoint and partition \(Q_\ell\).  Thus the whole
orientation cube has an exact integral two-factor into \(2\ell\)-cycles of
coordinate residence \(\ell\).

#### Proof

Identify \(\mathbb F_2^{h+1}=\mathbb F_2\times\mathbb F_2^h\).  Enumerate
the hyperplane \(\{0\}\times\mathbb F_2^h\) as

\[
 p_0=0,p_1,\ldots,p_{\ell-1},
\]

and put \(T=(1,0)\).  Define a linear map

\[
 \varphi:\mathbb F_2^\ell\longrightarrow\mathbb F_2^{h+1}
\]

on the coordinate vectors by

\[
 \varphi(e_i)=p_i+p_{i+1}\quad(0\le i<\ell-1),
 \qquad
 \varphi(e_{\ell-1})=p_{\ell-1}+T.
 \tag{1.4}
\]

Let \(c_j\) be the vertex reached after the first \(j\) transitions in
(1.1), with \(0\le j<2\ell\).  Telescoping gives

\[
 \varphi(c_j)=p_j\quad(0\le j<\ell),
 \qquad
 \varphi(c_{\ell+j})=T+p_j\quad(0\le j<\ell).
 \tag{1.5}
\]

These are all \(2^{h+1}=2\ell\) syndromes exactly once.  In particular,
\(\varphi\) is onto and \(C_{\rm id}\) is a complete transversal of the
cosets of \(K=\ker\varphi\).  Therefore the translates in (1.3) are
disjoint and cover \(Q_\ell\).  Translation preserves every cube edge and
the cyclic transition word, proving the assertion. \(\square\)

This removes the physical-residence and component-count obstruction inside
one orientation cube: the reset count is exactly \(2^\ell/(2\ell)\), and
the reset overhead at depth \(H<\ell\) is \(H2^\ell/\ell\).

## 2. Why one order cannot supply the deeper SCD shadows

For a pair-flip rotor run, the depth-\(q\) lower shadow of an owner is
obtained by making the next \(q\) transition coordinates empty and retaining
the orientations of all other split pairs.  If the transition word is
\(\pi\pi\), the empty-pair set is one of the \(\ell\) cyclic
\(q\)-intervals of \(\pi\).

### Theorem 2.1 (template-capacity obstruction)

Fix an orientation stratum on \(s\) split pairs.  Suppose \(M\) selected
owners are partitioned into pair-flip rotor runs, and every run uses one of
at most \(T\) templates \((A,\pi)\), where \(A\) is its active coordinate
set and \(\pi\) is its cyclic order.  Suppose also that every template has
at most \(\ell\) possible cyclic starts.  Then the number of distinct
depth-\(q\) lower shadows among the selected owners is at most

\[
 T\ell 2^{s-q}.
 \tag{2.1}
\]

Consequently their duplicate excess is at least

\[
 \boxed{\bigl(M-T\ell 2^{s-q}\bigr)_+.}
 \tag{2.2}
\]

The same statement holds for upper shadows.

#### Proof

For one template, the set of \(q\) emptied pairs is one of at most \(\ell\)
cyclic intervals.  Once that set is fixed, a lower shadow has at most
\(2^{s-q}\) possible orientations on the remaining split pairs.  Summing
over templates proves (2.1).  For any map from \(M\) owners into at most
\(R\) targets, the duplicate excess is at least \(M-R\); use
\(R=T\ell2^{s-q}\). \(\square\)

### Corollary 2.2 (exponentially many orders are necessary)

If \(M\ge\delta 2^s\) and the depth-\(q\) duplicate excess is \(o(M)\),
then

\[
 \boxed{T\ge (\delta-o(1)){2^q\over\ell}.}
 \tag{2.3}
\]

In particular, on a Gaussian depth \(q=\Theta(\sqrt m)\), no polynomial or
\(\exp(o(\sqrt m))\) library of fixed pair-flip orders can furnish the
near-rainbow shadows required by a low-toll rotor--SCD.

For the exact tiling in Theorem 1.1, \(T=1\).  Hence at every
\(q>\log_2\ell\) its depth-\(q\) duplicate excess is at least

\[
 2^\ell-\ell2^{\ell-q}
 =2^\ell\bigl(1-\ell2^{-q}\bigr).
 \tag{2.4}
\]

Thus Theorem 1.1 is a genuine solution of the long-residence/two-factor
geometry, but not an all-depth SCD construction.  Any successful algebraic
continuation must vary the active coordinate order across exponentially many
cycles while retaining the two-sided Boolean ownership constraints.

## 3. Exact implication for the rotor--SCD lane

The complete rotor multicover has enormous multiplicity, but the audited
chronology-elimination theorem says that an \(o(Q_mW)\) SCD-colored toll is
equivalent to one integral SCD with \(o(W)\) weighted rotor path-forest toll.
Theorem 1.1 shows that long physical runs themselves admit an exact integral
tiling.  Theorem 2.1 identifies the remaining obstruction inside this
tiling architecture: simultaneous deeper-shadow ownership requires an
exponentially diverse order field, not one parity-check tile or a bounded
orbit library.

## 4. A recursive tiling with exponentially many orders

The preceding obstruction is not an obstruction to cube geometry itself.
There is an exact nonlinear cycle factor which automatically creates the
required exponential order diversity and is two-sided rainbow through half
its active dimension.

For powers of two \(\ell\), define a neighbour permutation
\(F_\ell:Q_\ell\to Q_\ell\) recursively.  For \(\ell=1\), let \(F_1\)
toggle the unique bit.  If \(\ell=2a\), write a vertex as \((u,v)\in
Q_a\times Q_a\), and set

\[
 F_{2a}(u,v)=
 \begin{cases}
  (F_a(u),v),&|u|+|v|\equiv0\pmod2,\\
  (u,F_a(v)),&|u|+|v|\equiv1\pmod2.
 \end{cases}
 \tag{4.1}
\]

Let \(\rho_\ell(x)\) be the coordinate toggled by \(F_\ell\) at \(x\).
For \(q\ge0\), define the forward deletion set and its labelled shadow by

\[
 D_q^+(x)=\{\rho_\ell(F_\ell^j x):0\le j<q\},
 \qquad
 \Sigma_q^+(x)=\bigl(D_q^+(x),x|_{[\ell]\setminus D_q^+(x)}\bigr).
 \tag{4.2}
\]

Define \(D_q^-\) and \(\Sigma_q^-\) in the same way using
\(F_\ell^{-1}\).  In the fixed-pair interpretation, \(\Sigma_q^+\) is
exactly the depth-\(q\) lower shadow and \(\Sigma_q^-\) is exactly the
depth-\(q\) upper shadow with `empty' replaced by `full'.

### Theorem 4.1 (recursive half-depth rainbow factor)

For every power of two \(\ell\ge2\):

1. \(F_\ell\) is a permutation of \(Q_\ell\), all of whose cycles have
   length \(2\ell\);
2. on every cycle its transition word is \(\pi\pi\) for a permutation
   \(\pi\) of the \(\ell\) coordinates, so every coordinate residence is
   exactly \(\ell\);
3. for every \(0\le q\le\ell/2\), both maps
   \[
    \Sigma_q^+,Sigma_q^-:Q_\ell\longrightarrow
    \{(D,\eta):|D|=q,\ \eta\in\{0,1\}^{[\ell]\setminus D}\}
   \]
   are injective.

Thus the entire orientation cube is partitioned into genuine radius-
\(\ell/2\) pair-flip rotor cycles whose lower and upper shadows are both
rainbow at every depth through \(\ell/2\).

#### Proof

The inverse of (4.1) is

\[
 F_{2a}^{-1}(u,v)=
 \begin{cases}
  (F_a^{-1}(u),v),&|u|+|v|\equiv1\pmod2,\\
  (u,F_a^{-1}(v)),&|u|+|v|\equiv0\pmod2.
 \end{cases}
 \tag{4.3}
\]

so \(F_{2a}\) is a permutation.  Since every move toggles total parity,
the two halves move alternately, and

\[
 F_{2a}^{2t}(u,v)=(F_a^t(u),F_a^t(v)).
 \tag{4.4}
\]

Inductively every \(F_a\)-cycle has length \(2a\).  Equation (4.4) then
shows that every \(F_{2a}\)-cycle has length \(4a=2(2a)\): an odd return
is excluded by parity, and an even return requires \(t\) to be a common
multiple of the two exact periods \(2a\).

During any \(2a\) successive moves of \(F_{2a}\), each half makes exactly
\(a\) moves.  By induction, any \(a\) successive moves in an
\(F_a\)-cycle use every coordinate of that half exactly once.  Hence the
first \(2a\) global moves use every coordinate exactly once, and the next
\(2a\) repeat the same interleaved order.  This proves assertions 1 and 2.

It remains to prove forward injectivity; reverse injectivity follows from
the identical alternating recursion (4.3).  Induct on \(\ell\), with
\(\ell=2\) checked directly on its four-cycle.  Write \(\ell=2a\).

If \(q=2t\), then each half makes exactly \(t\) moves, regardless of the
initial parity.  The datum \(\Sigma_{2t}^+(u,v)\) splits exactly into

\[
 \Sigma_t^+(u),\qquad \Sigma_t^+(v).
 \tag{4.5}
\]

Since \(q\le a\), one has \(t\le a/2\), and induction recovers \(u,v\)
uniquely.

If \(q=2t+1\), the half scheduled first makes \(t+1\) moves and the other
half makes \(t\) moves.  By (4.1), which half is scheduled first is
equivalent to the initial total parity.  The two cardinalities of the
deleted-coordinate sets therefore reveal that parity.  The shadow
then splits into \(\Sigma_{t+1}^+\) of that half and \(\Sigma_t^+\) of the
other.  For \(q\le a\) (and \(a\ge2\)), one has \(t+1\le a/2\), so
induction again recovers both halves.  This proves forward injectivity and,
using (4.3), reverse injectivity. \(\square\)

### Corollary 4.2 (the exponential library is actually present)

Let \(T_\ell\) be the number of distinct cyclic coordinate orders among
the cycles of \(F_\ell\).  Applying Corollary 2.2 at \(q=\ell/2\), with
\(M=2^\ell\), gives

\[
 \boxed{T_\ell\ge {2^{\ell/2}\over\ell}.}
 \tag{4.6}
\]

So the recursive product construction does exactly what the capacity bound
demands: it creates exponentially many order templates while still giving
an integral partition into long-residence cycles.

The remaining coefficient-one gate is now outside the orientation cube.
One must couple these intrastatum two-sided-rainbow factors across the
different split/full/empty pair strata so that the chosen radius census is
that of one SCD and every Boolean mask has one owner.  Theorem 4.1 removes
the long-run, residence, and within-stratum multidepth collision costs from
that coupling problem; it does not by itself supply the cross-stratum
ownership flow.
