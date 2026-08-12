# Positive winding at the weakened linear-seam scale: exact pruning and a scalar saturation model

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B=\operatorname {Cat}_r,
 \qquad W=NB,
 \qquad H=\lceil A\sqrt r\rceil,
\tag{0.1}
\]

where \(A>0\) is fixed.  Let \(\overline\nu_H^+\) be the maximum
packing of pairwise quotient-edge-disjoint, nonwrapping, positive-winding
PBBS residence intervals on the long quotient cycles.

The linear dominance-staircase seam does not require the older
\(O_A(B/N)\) quotient estimate.  For the positive-winding part, its exact
strict target is

\[
 \boxed{\overline\nu_H^+=o_A(B/H).}
\tag{0.2}
\]

This report proves the following boundary.

1. If \(K=K(r)\to\infty\), every quotient-edge-disjoint family whose
   winding is at least \(K\) has size

   \[
    \boxed{O\!\left(\frac{B}{K\sqrt r}\right)
           =o_A(B/H).}
   \tag{0.3}
   \]

   Thus at the weakened target one may discard **all diverging winding**,
   not only winding \(\Omega(\sqrt r)\).

2. There is an absolute \(K_0\) such that intervals whose terminal
   first-maximum position obeys

   \[
    \delta(D_s)\le \frac{r}{K_0(\log r)^2}
   \tag{0.4}
   \]

   form an \(o_A(B/H)\) family.  The terminal state is charged only once,
   because it is a literal edge of the full residence support.

3. These two prunings do not settle positive winding.  A formal cyclic
   model is constructed below which, simultaneously,

   * uses no more than the exact Catalan number of roots in any height
     stratum;
   * has height \(O_A(\sqrt r)\), winding only \(1\) or \(2\), and
     macroscopic terminal first-maximum position;
   * satisfies both exact endpoint deficit ledgers, their integer-floor
     centered forms, complete proper-prefix chronology, the three-block
     identity, area closure, voltage closure, and quotient-edge
     disjointness;
   * has total suffix-deficit mass \(O(B\sqrt r)\); but
   * contains \(\Omega_A(B/H)\) disjoint short-return supports.

   The model is deliberately not a PBBS/Dyck orbit: its voltage visits
   only \(2s+1<N\) spatial labels.  It is therefore a rigorous no-go for
   deductions from the listed scalar ledgers and capacities, not a
   counterexample to the genuine packing theorem.

Consequently positive winding is **not yet proved** to be \(o_A(B/H)\).
The exact residual is bounded winding, already winding one, with genuine
PBBS voltage-word compatibility.  The transported-sector matching gate
from the stronger \(B/N\) attack should be weakened accordingly: at the
linear-seam scale it is enough to prove \(o_A(B/H)\) for every fixed
winding cutoff.

No implication from \(d(D)=1\) to a return is used anywhere.

## 1. Exact quotient and physical normalization

For a return after ordinary gap \(2s+1\), the residence cutoff is

\[
 1\le s\le H-1,
\tag{1.1}
\]

and the complete quotient support has exactly \(s+2\) transition edges.
Let \(Z_H\) be the number of quotient edges on cycles of length at most
\(H+1\).  The audited voltage-itinerary estimate is

\[
 Z_H\le (2H+2)N^{2H+2}=\exp(o_A(r))=o_A(B/H).
\tag{1.2}
\]

The deck inequalities, restricted to positive-winding intervals, are

\[
 N\overline\nu_H^+
 \le \nu_H^+(P_r)
 \le 2N\overline\nu_H^+ +NZ_H.
\tag{1.3}
\]

The left inequality lifts all \(N\) spatial phases of a quotient
packing.  The right inequality is the factor-two circular-interval
packing/transversal bound followed by deck lifting; deleted short cycles
contribute \(NZ_H\).

Since \(W=NB\), equations (1.2)--(1.3) give the exact equivalence

\[
 \boxed{
 \overline\nu_H^+=o_A(B/H)
 \iff
 \nu_H^+(P_r)=o_A(W/H).}
\tag{1.4}
\]

This is the normalization relevant to the linear seam.  In particular,
the already proved critical estimate \(O(B/\sqrt r)\) is only
\(O_A(B/H)\), not the strict estimate (0.2).

## 2. The exact centered winding charge

Write the canonical first-maximum factorization as

\[
 D=P1R0S,
 \qquad
 d(D)=|S|+1,
 \qquad
 \delta(D)=|P|+1.
\tag{2.1}
\]

For a return root \(D_0\), put \(D_j=\tau^jD_0\).  If its two-step
winding is \(w\ge1\), the exact return equation is

\[
 \sum_{j=0}^{s-1}d(D_j)=\delta(D_s)+Nw.
\tag{2.2}
\]

Subtracting the exact integral floor \(d(D_j)\ge1\) gives

\[
 \boxed{
 \sum_{j=0}^{s-1}(d(D_j)-1)
 =Nw+\delta(D_s)-s.}
\tag{2.3}
\]

Let

\[
 \mathscr E_r=\sum_{D\in\mathcal D_r}(d(D)-1).
\tag{2.4}
\]

The audited suffix-deficit moment theorem gives absolute constants
\(0<c<C<\infty\) such that

\[
 cB\sqrt r\le \mathscr E_r\le CB\sqrt r.
\tag{2.5}
\]

For a quotient-edge-disjoint family, the deficit cores
\(D_0,\ldots,D_{s-1}\) are disjoint.  Summing (2.3) therefore yields

\[
 \boxed{
 \sum_{I\in\mathcal P^+}
 \bigl(Nw(I)+\delta(D_{s(I)}(I))-s(I)\bigr)
 \le \mathscr E_r.}
\tag{2.6}
\]

This is a quotient statement.  There is no extra factor \(N\) on its
right side.

### Theorem 2.1 (diverging winding is negligible at the weak scale)

For every integer \(K\ge1\), once \(H<N+2\),

\[
 \boxed{
 \#\{I\in\mathcal P^+:w(I)\ge K\}
 \le
 \frac{\mathscr E_r}{KN-H+2}.}
\tag{2.7}
\]

Consequently, uniformly for fixed \(A\),

\[
 \#\{I:w(I)\ge K\}
 =O\!\left(\frac{B}{K\sqrt r}\right).
\tag{2.8}
\]

If \(K=K(r)\to\infty\), this is \(o_A(B/H)\).

#### Proof

For every selected interval in the displayed class, (1.1) and
\(\delta(D_s)\ge1\) give

\[
 Nw+\delta(D_s)-s\ge KN-H+2.
\]

Sum this inequality and use (2.6), proving (2.7).  Equations (0.1) and
(2.5) then give (2.8).  Finally

\[
 \frac{B/(K\sqrt r)}{B/H}
 =\frac{H}{K\sqrt r}=\frac{A+o_A(1)}K,
\]

which tends to zero when \(K\to\infty\). \(\square\)

The conclusion is stronger, at the present target, than the previously
recorded statement that \(w\ge\eta\sqrt r\) is \(O(B/N)\).  What remains
is every fixed winding and, more generally, every bounded or slowly
growing winding below the chosen cutoff.

## 3. A terminal first-maximum pruning

Let

\[
 \Delta_{r,L}
 =\#\{D\in\mathcal D_r:\delta(D)\le L\}.
\tag{3.1}
\]

The audited prefix/spectral estimate gives absolute constants
\(c_0,C_0>0\) such that, for \(1\le L\le r\),

\[
 \Delta_{r,L}
 \le C_0(L+1)^3 4^r
       \exp\!\left[-c_0\sqrt{\frac r{L+1}}\right].
\tag{3.2}
\]

Choose an absolute \(K_0\) so large that

\[
 c_0\sqrt{K_0/2}>6,
\tag{3.3}
\]

and put

\[
 T_r=\left\lfloor\frac{r}{K_0(\log r)^2}\right\rfloor.
\tag{3.4}
\]

### Theorem 3.1 (early terminal state is negligible)

Every quotient-edge-disjoint family of residence at most \(H\) satisfies

\[
 \boxed{
 \#\{I:\delta(D_{s(I)}(I))\le T_r\}
 =o_A(B/H).}
\tag{3.5}
\]

This holds for arbitrary winding.

#### Proof

With the audited insertion-edge indexing, the full support is

\[
 Q(D_0,s)=\{e_{D_0},e_{D_1},\ldots,e_{D_{s+1}}\},
\]

and \(D\mapsto e_D\) is a bijection.  In particular the terminal state
\(D_s\) contributes the literal support edge \(e_{D_s}\).  If two
selected intervals had the same terminal root, they would share this
edge.  Quotient-edge disjointness therefore makes their terminal roots
distinct, and the left side of (3.5) is at most \(\Delta_{r,T_r}\).

For all sufficiently large \(r\),

\[
 T_r+1\le\frac{2r}{K_0(\log r)^2},
\]

so (3.2)--(3.3) give

\[
 \Delta_{r,T_r}
 \le C_0 r^3 4^r r^{-6}
 =O(4^r/r^3).
\tag{3.6}
\]

But \(B/H=\Theta_A(4^r/r^2)\).  The ratio in (3.6) is
\(O_A(1/r)\), proving (3.5). \(\square\)

Combining Theorems 2.1 and 3.1 leaves, for any chosen
\(K(r)\to\infty\), only intervals satisfying

\[
 1\le w<K(r),
 \qquad
 \delta(D_s)>\frac{r}{K_0(\log r)^2}.
\tag{3.7}
\]

The second inequality cannot be fed back into (2.3) to obtain a strict
factor: it increases the charge \(Nw\) only by a relative
\(O(1/\log^2r)\).  The next construction shows that this failure is
structural for scalar data.

## 4. A height-respecting scalar saturation model

This section constructs an abstract cyclic system.  Every displayed
identity is one of the audited scalar PBBS identities, but no claim is
made that its vertices are Dyck words.

Fix \(A>0\).  Choose a constant

\[
 C_A>4/A^2.
\tag{4.1}
\]

Take an infinite sequence of integers \(s\to\infty\) satisfying

\[
 s\not\equiv1\pmod3,
 \qquad
 s\not\equiv2\pmod5,
\tag{4.2}
\]

and choose odd integers \(e=e(s)\) with

\[
 e/s\longrightarrow C_A.
\tag{4.3}
\]

Set

\[
 N=e(2s+1),
 \qquad
 r=(N-1)/2.
\tag{4.4}
\]

Then

\[
 \frac{s}{\sqrt r}\longrightarrow\frac1{\sqrt{C_A}},
 \qquad
 \frac Hs\longrightarrow A\sqrt{C_A}>2.
\tag{4.5}
\]

In particular \(s+1\le H-1\) for all sufficiently large members of the
sequence.

Let

\[
 b_{r,h}=\#\{D\in\mathcal D_r:\operatorname {ht}(D)=h\}.
\tag{4.6}
\]

The audited lower spectral term implies that, for a constant
\(c_A>0\),

\[
 \sum_{h\le s}b_{r,h}\ge c_A B
\tag{4.7}
\]

eventually.  Indeed, by (4.5), the cutoff \(s\) is a fixed positive
multiple of \(\sqrt r\).

For each height \(1\le h\le s\), define

\[
 w_h=
 \begin{cases}
  1,&h\equiv s-1\pmod2,\\
  2,&h\equiv s\pmod2,
 \end{cases}
\tag{4.8}
\]

and attach the constant block data

\[
 \boxed{
 \begin{aligned}
  a_h=b_h^{\rm pos}&=e(s-w_h),\\
  c_h=\widehat c_h&=e(2w_h+1).
 \end{aligned}}
\tag{4.9}
\]

The superscript on \(b_h^{\rm pos}\) distinguishes the complementary
first-maximum position from the Catalan height count in (4.6).

### Lemma 4.1 (all scalar identities and proper chronology)

For each \(h\le s\), the data (4.9) satisfy:

\[
 a_h+b_h^{\rm pos}+c_h=N,
\tag{4.10}
\]

\[
 c_h=N-a_h-b_h^{\rm pos},
 \qquad
 \widehat c_h=N-b_h^{\rm pos}-a_h=c_h,
\tag{4.11}
\]

\[
 \boxed{sc_h=Nw_h+a_h}
\tag{4.12}
\]

on both endpoint parities, and

\[
 \boxed{s(c_h-1)=Nw_h+a_h-s.}
\tag{4.13}
\]

Moreover \(a_h\equiv b_h^{\rm pos}\equiv h\pmod2\), the area increment
\(a_h-b_h^{\rm pos}\) is zero, and the return in (4.12) is consecutive:
every proper even-time and odd-time endpoint residue is nonzero modulo
\(N\).

#### Proof

Equations (4.10)--(4.11) follow from

\[
 2e(s-w_h)+e(2w_h+1)=e(2s+1)=N.
\]

Also

\[
 \begin{aligned}
 Nw_h+a_h
 &=e(2s+1)w_h+e(s-w_h)\\
 &=es(2w_h+1)=sc_h,
 \end{aligned}
\]

which proves (4.12), and subtracting \(s\) proves (4.13).
Because \(e\) is odd and (4.8) gives \(s-w_h\equiv h\pmod2\), the
parity statement follows.  Equality of the two position variables gives
zero area increment.

For chronology, use the exact decreasing endpoint potential

\[
 Y_j=a_h-jc_h
 =e\bigl((s-w_h)-j(2w_h+1)\bigr).
\tag{4.14}
\]

At \(j=s\), this equals \(-w_hN\).  By (4.2),

\[
 \gcd(2w_h+1,2s+1)=1
\]

for \(w_h=1,2\).  Hence the unique solution modulo \(2s+1\) of
\(Y_j\equiv0\pmod N\) is \(j\equiv s\pmod{2s+1}\).  No integer
\(1\le j<s\) is a solution; also \(Y_0=a_h\in(0,N)\).  Thus there is
no proper odd-time return.

There is a separate even-time check.  After \(j\) complete step-two
moves the accumulated voltage is \(jc_h\).  Equations (4.2) and (4.9)
give

\[
 \gcd(c_h,N)=e,
 \qquad
 \frac{N}{\gcd(c_h,N)}=2s+1.
\tag{4.14a}
\]

Thus \(jc_h\not\equiv0\pmod N\) for every \(1\le j\le s\).  No
proper even-time return occurs either.  Together the two checks give the
complete proper-prefix chronology. \(\square\)

### Theorem 4.2 (critical scalar packing with exact height inventory)

There is a formal union of directed quotient cycles which uses at most
\(b_{r,h}\) vertices of every exact height \(h\), satisfies Lemma 4.1 at
every vertex, has total deficit mass \(O_A(B\sqrt r)\), and contains a
pairwise edge-disjoint family of admissible positive-winding supports of
size

\[
 \boxed{\Omega_A(B/H).}
\tag{4.15}
\]

All windings in this family belong to \(\{1,2\}\), and every terminal
first-maximum position lies in \([N/3,2N/3]\) for all sufficiently large
\(r\).

#### Proof

For each \(h\le s\), take

\[
 q_h=\left\lfloor\frac{b_{r,h}}N\right\rfloor
\tag{4.16}
\]

formal directed cycles of length \(N\), all of height \(h\), and put the
constant data (4.9) on each cycle.  This uses \(Nq_h\le b_{r,h}\)
vertices of height \(h\).  Equation (4.7) gives

\[
 \sum_{h\le s}Nq_h
 \ge c_AB-Ns
 =(c_A-o(1))B.
\tag{4.17}
\]

The voltage around one cycle is \(Nc_h\), hence is zero modulo \(N\).
The area increment is identically zero.  Thus both cyclic scalar closure
conditions hold.

By Lemma 4.1, every start on such a cycle has a consecutive return of
step-two duration \(s\).  Its full support has \(s+2\) quotient edges.
Cut the cycle at one edge and choose starts at spacings \(s+2\).  This
gives

\[
 \left\lfloor\frac{N}{s+2}\right\rfloor
\]

pairwise nonwrapping, edge-disjoint supports on each cycle.  Therefore

\[
 \begin{aligned}
 P_r^{\rm form}
 &=\left(\sum_{h\le s}q_h\right)
      \left\lfloor\frac{N}{s+2}\right\rfloor\\
 &\ge(c_A-o(1))\frac{B}{s+2}
 =\Omega_A(B/H),
 \end{aligned}
\tag{4.18}
\]

where the polynomial floor losses are negligible compared with \(B\),
and the last equality uses (4.5).

The deficit at every used vertex lies between \(3e\) and \(5e\).  Since
\(e=\Theta_A(\sqrt r)\), its total mass is at most

\[
 5eB=O_A(B\sqrt r).
\tag{4.19}
\]

If one insists on any prescribed absolute constant in this resource
bound, retain a sufficiently small positive \(A\)-dependent fraction of
the cycles.  Equation (4.18) remains \(\Omega_A(B/H)\).

Finally

\[
 \frac{a_h}{N}=\frac{s-w_h}{2s+1}\longrightarrow\frac12,
\tag{4.20}
\]

uniformly for \(w_h\in\{1,2\}\).  This proves the terminal assertion.
\(\square\)

### Why Theorem 4.2 is not a PBBS counterexample

For a formal cycle of type \(h\),

\[
 \gcd(c_h,N)
 =e\gcd(2w_h+1,2s+1)=e.
\tag{4.21}
\]

Hence the step-two voltage visits only

\[
 \frac Ne=2s+1<N
\tag{4.22}
\]

spatial labels.  A genuine PBBS component has the audited complete
omitted-coordinate coverage and voltage-word reconstruction property.
In fact \(a_h,b_h^{\rm pos},c_h\) are all multiples of \(e\), so adding
the intervening odd phases does not leave that residue class modulo
\(e\).  The full one-step omitted-label itinerary still visits only
\(2s+1\) labels.  The formal system therefore cannot be promoted to a
PBBS orbit.

This failure is exactly the scope boundary.  The model proves that the
following data, even imposed simultaneously, do not imply (0.2):

* exact height-stratum capacities and the height--gap restriction;
* trace length and quotient-edge disjointness;
* both endpoint winding ledgers and the centered integer floor;
* proper first-return chronology;
* the three-block identity, area closure, and cycle-voltage closure;
* the correct \(B\sqrt r\) first-deficit resource scale; and
* terminal first maxima bounded away from both endpoints.

It does not rule out a phase-localized weight using the literal Dyck word,
complete coordinate coverage, transported sector pairs, or Pascal slots.

## 5. The correctly weakened transported-sector gate

For one genuine positive-winding return, the audited two-endpoint
staircase contains an even--odd transported cell of length at least

\[
 \frac{wN}{2s-1}\ge\frac{N}{2H-1}.
\tag{5.1}
\]

Choosing one such cell from every member of a quotient-edge-disjoint
family gives a matching: its even roots are distinct and its half-shifted
roots are distinct.  Summing cell lengths only reproduces the scalar
winding budget, so (5.1) alone stops at \(O(B/\sqrt r)\).

At the old \(B/N\) target, the proposed transported-sector lemma asked
for \(O_A(B/N)\) throughout \(w=o(\sqrt r)\).  That is stronger than the
linear seam requires.  The exact sufficient replacement is:

> **Weak genuine transported-sector gate (unproved).**  For every fixed
> \(A>0\) and every fixed integer \(K\ge1\), every matching obtained by
> choosing one cell satisfying (5.1) from each genuine PBBS return with
> \(s\le H-1\) and \(1\le w\le K\) has size
> \[
>   o_A(B/H).
> \tag{5.2}
> \]

Indeed, (5.2) bounds all winding at most \(K\), while Theorem 2.1 gives

\[
 \limsup_{r\to\infty}
 \frac{\#\{I:w(I)>K\}}{B/H}
 \le\frac{C_A}{K}.
\tag{5.3}
\]

Letting \(K\to\infty\) proves (0.2).  Theorem 4.2 shows that the word
“genuine” in (5.2) is indispensable even at this weaker scale.

## 6. Audit and exact implication boundary

1. **Cutoff indexing.**  Residence at most \(H\) means \(s+1\le H\),
   so the deficit core has \(s\le H-1\) roots and the full support has
   \(s+2\) edges.

2. **Centered floor.**  The denominator in Theorem 2.1 is exactly
   \(KN-H+2\), from \(\delta(D_s)\ge1\) and \(s\le H-1\).

3. **Terminal injectivity.**  The terminal root is charged through its
   indexed edge in the full support, not through the shorter deficit
   core.  Edge-disjointness therefore makes terminal roots distinct.

4. **Deck factor.**  All estimates in Sections 2--5 are quotient
   estimates.  Multiplication by \(N\) occurs only in (1.3), and
   \(B/H\) upstairs becomes \(W/H\) physically.

5. **Formal chronology.**  The exclusions in (4.2) are precisely
   \(\gcd(3,2s+1)=\gcd(5,2s+1)=1\).  They cover both windings used in
   (4.8), and infinitely many \(s\) satisfy them.

6. **Height inventory.**  The model does not place \(B\) vertices in one
   artificial height.  It uses at most the actual number \(b_{r,h}\) at
   every exact height, and loses only \(Ns=O(r^{3/2})=o(B)\) vertices to
   cycle divisibility.

7. **Scope of the no-go.**  Theorem 4.2 is not a Dyck orbit and not a
   lower bound for \(\overline\nu_H^+\).  It closes only the scalar
   inference architecture explicitly listed after (4.22).

The proved/conditional boundary is therefore

\[
 \boxed{
 \begin{aligned}
  &w\to\infty:
    &&o_A(B/H)\quad\text{proved},\\
  &\delta(D_s)\le r/[K_0(\log r)^2]:
    &&o_A(B/H)\quad\text{proved},\\
  &1\le w\le K\text{ fixed, genuine PBBS}:
    &&o_A(B/H)\quad\text{open},\\
  &\text{scalar ledgers and capacities alone}:
    &&\Omega_A(B/H)\quad\text{formally attainable},\\
  &\text{positive-winding contribution to coefficient one}:
    &&\text{not yet proved}.
 \end{aligned}}
\tag{6.1}
\]
