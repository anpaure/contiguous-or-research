# Noncanonical product-SCD prefix frames: Gaussian escape mass and the linear port toll

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Work in \(B_{2m}\), and put

\[
 W=\binom{2m}{m},
 \qquad q=\lfloor\sqrt m\rfloor.
\tag{0.1}
\]

Choose arbitrary SCDs of two \(m\)-coordinate half-cubes.  They may be
noncanonical and unrelated on the two shores.  Their product cells have
step lengths \(p,s\), middle width

\[
 \omega(p,s)=\min\{p,s\}+1,
\tag{0.2}
\]

and the exact width identity

\[
 \sum_{p,s}c_m(p)c_m(s)\omega(p,s)=W.
\tag{0.3}
\]

Here \(c_m(p)\) is the number of half-cube chains of step length \(p\).
It depends only on \(m,p\), not on the chosen SCD.

The universal two-fixed-pair theorem has the following robust form.  Fix
one reference coordinate pairing on each of two shores.  If
\(E_{\rm esc}\) selected depth-\(q\) occurrences do not remain in their
shore's reference pairing, then the two-copy imbalance obeys

\[
 \boxed{
 \mathfrak B_{2,q}^-
 \ge(\kappa+o(1))W-E_{\rm esc},}
\tag{0.4}
\]

where

\[
 \kappa=
 2\left[e^{-1}(2\Phi(1)-1)-\Phi(-1)\right]>0.
\tag{0.5}
\]

Consequently every construction with
\(\mathfrak B_{2,q}^-=o(W)\) must move

\[
 E_{\rm esc}\ge(\kappa-o(1))W
\tag{0.6}
\]

occurrences outside the two reference pairings.

The new product-SCD census theorem is:

> Any family of product cells carrying \(\gamma W\) capacity, where
> \(\gamma>0\) is fixed, contains \(\Omega_\gamma(W/\sqrt m)\) distinct
> cells.  This remains true for arbitrary noncanonical half-cube SCDs.

Therefore a two-shore product-SCD catalogue satisfying (0.6) uses at least

\[
 \Omega(W/\sqrt m)
\tag{0.7}
\]

frame-escaping product-prefix atoms.

If every such atom is separately initialized by a depth-\(q\) singleton
port, collar, or reverse-prefix word, its exterior charge is at least
\(q\).  Equations (0.1) and (0.7) then give

\[
 \boxed{E_{\rm port}=\Omega(W).}
\tag{0.8}
\]

Thus no **separated-prefix** noncanonical product-SCD construction can
both evade the universal two-frame deficit and keep its exterior ledger
\(o(W)\).  This conclusion is independent of the half-cube SCD rules.

The scope is sharp.  A construction may escape only by letting one
physical prefix/collar serve many different product cells, or by making
the actual state chronology cross cell boundaries with zero new
initialization cost.  Such an object is a nonlocal cross-cell braid, not a
concatenation of product-SCD prefix frames.  The theorem does not rule out
that braid.

There is also a simpler cutoff incompatibility.  The independent
product-SCD exterior word is \(o(W)\) only on a diagonal cutoff
\(H/\sqrt m\to\infty\); at every fixed \(H=A\sqrt m+o(\sqrt m)\), its
normalized cost is bounded away from zero.  Hence an economical product
exterior necessarily leaves the audited depth \(q=\lfloor\sqrt m\rfloor\)
inside the central compiler, exactly where (0.4)--(0.8) apply.

## 1. The robust two-frame escape inequality

Let \(\mathcal P_0,\mathcal P_1\) be arbitrary perfect matchings of the
\(2m\) physical coordinates.  On shore \(i\), call a selected occurrence
**internal** if its source-to-target transition preserves the
full-\(\mathcal P_i\)-pair count.  All other selected occurrences are
called escaping.  Let \(E_{\rm esc}\) be their total number over both
shores.  Assume, as in the two-copy port ledger, that every middle owner
supplies at most one selected occurrence at this depth.  Write \(\Phi\)
for the standard normal distribution function.

For a set \(S\), write \(f_i(S)\) for its number of full
\(\mathcal P_i\)-pairs.  At depth \(q\), put

\[
 A_i(a)=
 \left\{T\in\binom{[2m]}{m-q}:f_i(T)\le a\right\},
 \qquad
 A(a)=A_0(a)\cap A_1(a).
\tag{1.1}
\]

Let \(T_{\le a,q}\) and \(V_{\le a}\) be the usual target and middle-owner
lower-tail counts.  Relabelling invariance gives

\[
 |A(a)|\ge2T_{\le a,q}-N_q,
 \qquad N_q=\binom{2m}{m-q}.
\tag{1.2}
\]

### Theorem 1.1 (robust two-frame lower-tail cut)

For every integer \(a\),

\[
 \boxed{
 \mathfrak B_{2,q}^-
 \ge
 2\bigl(2T_{\le a,q}-N_q-V_{\le a}\bigr)
 -E_{\rm esc}.}
\tag{1.3}
\]

The right side may be replaced by its positive part.

#### Proof

Every internal occurrence landing in \(A(a)\) starts from an owner whose
type in its own shore is at most \(a\).  Since one owner supplies at most
one selected depth-\(q\) occurrence, the internal contribution to
\(\sum_{T\in A(a)}r_T\) is at most \(2V_{\le a}\).  Escaping occurrences
contribute at most \(E_{\rm esc}\).  Hence

\[
 \sum_{T\in A(a)}r_T\le2V_{\le a}+E_{\rm esc}.
\tag{1.4}
\]

Since \(|r_T-2|\ge2-r_T\), equations (1.2)--(1.4) give

\[
 \begin{aligned}
 \mathfrak B_{2,q}^-
 &\ge2|A(a)|-\sum_{T\in A(a)}r_T\\
 &\ge4T_{\le a,q}-2N_q-2V_{\le a}-E_{\rm esc},
 \end{aligned}
\]

which is (1.3). \(\square\)

At \(q=\lfloor\sqrt m\rfloor\), take the Gaussian threshold corresponding
to \(t=-1\).  The matching-type central limit gives

\[
 2\bigl(2T_{\le a,q}-N_q-V_{\le a}\bigr)
 =(\kappa+o(1))W.
\tag{1.5}
\]

Equations (1.3)--(1.5) prove (0.4)--(0.6).  Notice that no relation between
\(\mathcal P_0\) and \(\mathcal P_1\) is used.  An occurrence generated by
a genuinely non-pair-frame product transition is simply charged to
\(E_{\rm esc}\).

## 2. Product-cell widths are SCD-independent

A symmetric chain in \(B_m\) with minimum rank \(a\) has step length

\[
 p=m-2a.
\tag{2.1}
\]

The number of such chains is

\[
 c_m(p)
 =\binom ma-\binom m{a-1}.
\tag{2.2}
\]

Thus \(c_m(p)\) is the same for every SCD.  A product of chains of step
lengths \(p,s\) is the grid \([0,p]\times[0,s]\).  Its middle diagonal has
width \(\omega(p,s)\) from (0.2).  Product cells partition \(B_{2m}\), so
their middle diagonals partition the middle layer, proving (0.3).

The following concentration statement is the load-bearing point.

### Lemma 2.1 (Gaussian concentration of product-cell width)

There are absolute constants \(C,c>0\) such that, for every fixed
\(L\ge1\),

\[
 \sum_{\max\{p,s\}>L\sqrt m}
 c_m(p)c_m(s)\omega(p,s)
 \le Ce^{-cL^2}W
\tag{2.3}
\]

for all sufficiently large \(m\).

#### Proof

The chain census telescopes.  Up to the harmless parity rounding,

\[
 \sum_{p>L\sqrt m}c_m(p)
 =
 \binom m{\lfloor(m-L\sqrt m)/2\rfloor}.
\tag{2.4}
\]

The standard central-binomial ratio bound therefore gives

\[
 \sum_{p>L\sqrt m}c_m(p)
 \le
 C\frac{2^m}{\sqrt m}e^{-cL^2}.
\tag{2.5}
\]

Also

\[
 \sum_s c_m(s)(s+1)=2^m,
\tag{2.6}
\]

because the SCD chains partition \(B_m\).  Since
\(\omega(p,s)\le s+1\), the total width of cells with
\(p>L\sqrt m\) is at most the product of (2.5) and (2.6).
Interchanging \(p,s\), and using

\[
 W=\Theta(4^m/\sqrt m),
\tag{2.7}
\]

proves (2.3). \(\square\)

### Theorem 2.2 (positive capacity needs many prefix atoms)

For every fixed \(\gamma>0\), there is \(b_\gamma>0\) such that the
following holds for all sufficiently large \(m\).  If a family
\(\mathcal Q\) of product cells has total middle capacity

\[
 \sum_{Q\in\mathcal Q}\omega(Q)\ge\gamma W,
\tag{2.8}
\]

then

\[
 \boxed{|\mathcal Q|\ge b_\gamma\,{W\over\sqrt m}.}
\tag{2.9}
\]

The same assertion holds after combining two shores.

#### Proof

Choose a constant \(L=L(\gamma)\) so large that the right side of (2.3)
is at most \(\gamma W/2\).  At least \(\gamma W/2\) of the capacity in
(2.8) then comes from cells with
\(\max\{p,s\}\le L\sqrt m\).  Every such cell has width at most
\(L\sqrt m+1\).  Hence

\[
 |\mathcal Q|
 \ge\frac{\gamma W/2}{L\sqrt m+1},
\]

which proves (2.9).  For two shores apply the same estimate to their
disjoint labelled cell catalogues. \(\square\)

The theorem counts physical product-prefix atoms, not merely frame labels.
Assigning a different coordinate pairing to every cell does not alter the
bound.

## 3. The separated-prefix no-go

Consider a two-shore product-SCD construction satisfying:

1. every selected depth-\(q\) occurrence belongs to a labelled product
   cell and each cell supplies at most its middle width in occurrences;
2. occurrences internal to the two reference pairings satisfy the
   capacity-one hypothesis of Theorem 1.1;
3. every product cell carrying an escaping occurrence is initialized by
   its own literal \(q\)-port, or by another cell-local prefix/collar of
   length at least \(\eta q\), where \(\eta>0\) is fixed; and
4. no physical prefix letters are shared between two labelled cells.

These are exactly the separated-prefix hypotheses.  The half-cube SCDs,
cell orientations, increment orders, and pairing assigned to each cell
are otherwise arbitrary.

### Theorem 3.1 (noncanonical product-prefix Gaussian no-go)

If

\[
 \mathfrak B_{2,q}^-=o(W),
\tag{3.1}
\]

then the cell-local exterior charge satisfies

\[
 \boxed{E_{\rm port}\ge c_\eta W}
\tag{3.2}
\]

for a constant \(c_\eta>0\).

#### Proof

Theorem 1.1 gives

\[
 E_{\rm esc}\ge(\kappa-o(1))W.
\tag{3.3}
\]

By the capacity condition in hypothesis 1, the escaping cells have total
middle capacity at least \(E_{\rm esc}\).  Apply Theorem 2.2 with, say,
\(\gamma=\kappa/2\).  There are at least

\[
 b_{\kappa/2}{W\over\sqrt m}
\tag{3.4}
\]

distinct escaping prefix atoms.  Each costs at least
\(\eta q=(\eta+o(1))\sqrt m\), and the charges are disjoint by hypothesis
4.  Multiplying proves (3.2). \(\square\)

The theorem also has a quantitative sharing contrapositive.  If the total
port ledger is \(o(W)\), the \(\Omega(W/\sqrt m)\) escaping atoms cannot
have independent Gaussian prefixes.  Indeed, if every nonshared port has
length at least \(\eta q\), only \(o(W/\sqrt m)\) atoms can have such a
port.  Thus all but an \(o(1)\) fraction of the forced escaping atoms must
receive their prefixes from positions already serving other cells, or
their cross-cell junctions must retain an \(H\)-safe inherited state with
no fresh prefix.  Either conclusion is a macroscopic nonlocal coupling.

## 4. Exterior-cutoff audit

The exact product-SCD exterior word is independent of the chosen
half-cube SCDs: both its chain census and its word lengths depend only on
the minimum ranks.  Two previously proved estimates give the sharp
cutoff distinction:

1. if \(H/\sqrt m\to\infty\), its length is \(o(W)\);
2. if \(H=A\sqrt m+o(\sqrt m)\) for fixed \(A<\infty\), even its
   optimistically middle-credited residual has limiting normalized cost
   \(G(A)>0\).

Thus a product-SCD exterior with \(o(W)\) cost must be cut beyond every
fixed Gaussian depth.  In particular the rank \(m-q\), with
\(q=\lfloor\sqrt m\rfloor\), remains a central obligation.  Theorem 3.1
then shows that a separated product-prefix repair of that obligation has
linear cost.

This produces the promised dichotomy:

\[
 \boxed{
 \begin{array}{c}
 \text{fixed-Gaussian product exterior}\\
 \text{or separated frame-escaping product prefixes}
 \end{array}
 \quad\Longrightarrow\quad
 \Omega(W)\text{ additional cost}.}
\tag{4.1}
\]

## 5. Logical boundary

Proved here:

1. the robust two-frame imbalance inequality with an explicit escape-mass
   correction;
2. the SCD-independent Gaussian concentration of product-cell widths;
3. the \(\Omega(W/\sqrt m)\) atom count for every positive-capacity
   product-cell family; and
4. the linear exterior toll for every separated-prefix noncanonical
   product-SCD construction which evades the two reference frames.

Not proved here:

1. a no-go for an \(H\)-safe state sequence crossing product-cell
   boundaries without fresh prefixes;
2. a no-go for one physical collar shared by an unbounded number of cells;
3. a no-go for an anchored higher-order catalogue which abandons the
   two-copy balance objective; or
4. coefficient one.

The conclusion is therefore sharp at the requested architectural
boundary.  Changing the SCD inside each half-cube does not create enough
large product cells to hide the required frame escape.  With independent
prefixes the escape costs linearly.  A surviving construction must share
prefix states across cells on positive mass, which is precisely the
nonlocal Gaussian-annulus braid still missing from the program.
