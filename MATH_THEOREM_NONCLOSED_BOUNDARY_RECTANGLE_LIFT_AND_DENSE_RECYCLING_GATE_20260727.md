# A nonclosed boundary rectangle has zero vertical collateral

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\tag{0.1}
\]

and assume \(H\ge3\) and \(m\ge6H+4\).  A common-core path has an
exposed word \(w_1,\ldots,w_{m-2H}\) and retains phases
\(1,\ldots,d\).  Its literal signed-rank targets are recalled in
Section 2.

There is an exact two-top nonclosed macro with the following action.
For every \((m-2)\)-set \(R\) and four distinct labels
\(a,b,z,z'\notin R\), it changes two literal common-core paths and has

\[
 \Delta_r=0\quad(0<|r|\le H),
\tag{0.2}
\]

whereas at the middle row

\[
 \boxed{
 \Delta_0=
 e_{R\cup\{a,z\}}+e_{R\cup\{b,z'\}}
 -e_{R\cup\{a,z'\}}-e_{R\cup\{b,z\}}.}
\tag{0.3}
\]

The identity is first an untagged deck identity.  It remains exact for
the actual nested signed-rank catalogue by using the same phase-tag
schedule on the two tops.  Section 2 checks the shifted promotion
formula separately: at lower depth \(q\) the only changed phase is
\(q+2\), at upper depth \(1\) it is phase \(1\), and at larger upper
depths there is no change.  Identical tags therefore retain or delete
the two cancelling terms together.

Thus the first genuinely useful escape from the closed chronology
obstruction is already present: **two nonneutral boundary swaps can
cancel their complete vertical collars and leave one standard
hypersimplex rectangle at the middle.**  The companion top remains
changed, so this does not contradict the closed-routing obstruction.

Let \(A\) be the \(2m\times\binom{2m}{m}\) singleton-incidence matrix.
The rectangles (0.3) generate the full integral lattice

\[
 \boxed{
 \ker_{\mathbb Z}A
 =\{z\in\mathbb Z^{\binom{[2m]}m}:Az=0\}.}
\tag{0.4}
\]

Consequently every zero-singleton-marginal middle displacement has a
**formal signed physical lift with exactly zero collateral at every
other protected depth**.  More generally, every zero-total middle
displacement \(z\) has a formal lift whose total nonmiddle \(L^1\) toll
is at most

\[
                         2H\,\|Az\|_1.
\tag{0.5}
\]

This is the desired sub-\(H\) amortization in its sharp algebraic form:
the vertical toll is charged only to the net singleton-marginal change,
not to the number of middle transfers.  In particular it is zero when
the initial and target loads have the same legal marginals, as they do
in the near-flat marginal-fibre theorem.

There is, however, a separate and quantitative installation gate.
Equations (0.2)--(0.5) are relations in the signed catalogue generated
by literal path-option differences.  They do not assert that an
arbitrary sum can be installed in one table with each top used once.
Indeed the explicit master-order state is at total-variation distance
\((1-o(1))W\) from every load of collision energy \(o(W)\).  Hence any
route from that state using boundary swaps as its only middle-nonneutral
primitive needs

\[
                             (1-o(1))W
\tag{0.6}
\]

boundary swaps.  In the calibrated regime
\(H=(1+o(1))\sqrt{m\log m}\), a bank offering one toggle on each of the
\(N=\binom{2m}{M}=(1+o(1))W/m\) tops is therefore too small by a factor
\(m\).  What survives is a precise dense-recycling problem: organize
\(\Theta(W)\) chronological boundary swaps on \(N\) tops into the
collar-neutral rectangles (0.3), reusing an average of
\(\Theta(m)\) nonneutral states per top.

## 1. Exact two-top construction

Fix disjoint data

\[
 |R|=m-2,\qquad a,b,z,z'\notin R,
\tag{1.1}
\]

with \(a,b,z,z'\) distinct.  Split

\[
 R=R_{\rm hid}\mathbin{\dot\cup}R_{\rm act},
 \qquad |R_{\rm hid}|=3H,\qquad
 |R_{\rm act}|=m-3H-2.
\tag{1.2}
\]

Choose a \(2H\)-set \(Q\subset R_{\rm hid}\), put
\(P=R_{\rm hid}\setminus Q\), and order both \(Q\) and \(P\).
Also choose an ordered set

\[
 F=(f_1,\ldots,f_{H-3}),\qquad |F|=H-3,
\tag{1.3}
\]

and two further labels \(x,y\), all outside
\(R\cup\{a,b,z,z'\}\).  This uses

\[
 (m-2)+4+(H-3)+2=M+1\le2m
\]

labels.  Define the two distinct tops

\[
 \begin{aligned}
 U  &=R\cup\{a,b,z,z'\}\cup F\cup\{x\},\\
 U' &=R\cup\{a,b,z,z'\}\cup F\cup\{y\}.
 \end{aligned}
\tag{1.4}
\]

Choose any order \(\rho\) of \(R_{\rm act}\).  The two exposed words are

\[
 \begin{aligned}
 w  &=(a,b,x,f_1,\ldots,f_{H-3},z,z',\rho),\\
 w' &=(b,a,y,f_1,\ldots,f_{H-3},z',z,\rho).
 \end{aligned}
\tag{1.5}
\]

Each has length

\[
                  H+2+(m-3H-2)=m-2H,
\]

as required.  Complete them to literal cyclic top orders by

\[
                         (Q,P,w),\qquad (Q,P,w').
\tag{1.6}
\]

Let \(\widehat w\) and \(\widehat w'\) be obtained by interchanging
the first two exposed letters of \(w\) and \(w'\), respectively.  The
old shore is

\[
                         (U,w),(U',w')
\tag{1.7}
\]

and the new shore is

\[
                  (U,\widehat w),(U',\widehat w').
\tag{1.8}
\]

Both shores choose one literal path at each of the same two tops.
The set \(Q\) is one common protected \(2H\)-core, and \(P\) is the
unused \(H\)-letter prefix in the core-safe normal form.  Thus
(1.6)--(1.8) are actual common-core configurations, not whole-top words
standing in for exposed words.

## 2. Independent check at every complementary length

For a word beginning \((u,v,c_1,c_2,\ldots)\), swapping \(u,v\) has
zero deck derivative at \(h=0,1\).  For \(h\ge2\), phase \(1\) contains
both letters, every phase \(i\ge3\) contains neither, and phase \(2\)
is the only changed phase.  If

\[
 K_h=U\setminus\{u,v,c_1,\ldots,c_{h-1}\},
\tag{2.1}
\]

then its exact derivative is

\[
                   g_{u,v}(K_h):=e_{K_h\cup\{v\}}
                                      -e_{K_h\cup\{u\}}.
\tag{2.2}
\]

For the first top in (1.4), denote this core by \(K_h\).  For the
second top denote it by \(K'_h\).  The early top discrepancy \(x/y\)
is removed from both complements as soon as \(h\ge2\).  The two tail
orders then have identical prefix sets except when the prefix has
length exactly \(H-1\):

\[
 K_h=K'_h\quad(2\le h\le2H,\ h\ne H),
\tag{2.3}
\]

while

\[
                         K_H=R\cup\{z'\},
 \qquad                  K'_H=R\cup\{z\}.
\tag{2.4}
\]

The first swap is oriented \(a\to b\), whereas the second is oriented
\(b\to a\).  Therefore

\[
 \Delta_h=g_{a,b}(K_h)-g_{a,b}(K'_h).
\tag{2.5}
\]

Equations (2.3) and the separate \(h=0,1\) check prove cancellation
at every auxiliary length \(h\ne H\).  At \(h=H\), equations
(2.2), (2.4), and (2.5) give

\[
 \begin{aligned}
 \Delta_H={}&e_{R\cup\{b,z'\}}-e_{R\cup\{a,z'\}}\\
             &+e_{R\cup\{a,z\}}-e_{R\cup\{b,z\}},
 \end{aligned}
\]

which is (0.3), including its signs.

### Actual signed promotion traces

For completeness, in the core-safe promotion convention the phase-\(j\)
target at signed rank \(m+r\) is

\[
 C_j(r)=U\setminus
 \{w_{j+r},w_{j+r+1},\ldots,w_{j+H-1}\},
\tag{2.6}
\]

where \(w_1,w_2,\ldots\) is the exposed middle word and indices at most
zero lie in the unused prefix.  If \(r=-q<0\), every phase through
\(q+1\) contains both \(w_1,w_2\), phase \(q+2\) contains \(w_2\) but
not \(w_1\), and all later phases contain neither.  Thus phase \(q+2\)
is the unique lower-depth change.  Its omitted interval has length
\(H+q\), so its derivative is (2.2) with \(h=H+q\).  Since \(h>H\),
(2.3) cancels the two tops.

If \(r=1\), phase \(1\) is the unique changed phase and its omitted
interval is \(\{w_2,\ldots,w_H\}\), corresponding to \(h=H-1\).
Again (2.3) cancels the two tops.  If \(r\ge2\), every omitted interval
starts after \(w_2\), so each top is unchanged.  At \(r=0\) all middle
phases are present and (0.3) is the already computed action.

Give the two tops identical phase tags.  The unique changed lower or
upper phase is then active on both tops or on neither.  Hence the
cancellations above hold simultaneously in the actual tagged catalogue,
not merely in the complete untagged decks.

The cancellation uses two changed endpoint tops.  Hence it is outside
the hypothesis of the closed-companion chronology theorem, which
requires every nonfocal top to be restored.

## 3. The rectangle lattice is exactly the zero-marginal lattice

Let \(\mathcal R_m\) be the integral lattice generated by the vectors
in (0.3).  Plainly \(\mathcal R_m\subseteq\ker_{\mathbb Z}A\).  We prove
the reverse inclusion in two steps.

### Lemma 3.1 (every symmetric exchange is a rectangle sum)

Let \(P,Q\in\binom{[2m]}m\), let \(a\in P\setminus Q\), and let
\(b\in Q\setminus P\).  Put

\[
 P'=P-\{a\}+\{b\},\qquad Q'=Q-\{b\}+\{a\}.
\]

Then

\[
                         e_{P'}+e_{Q'}-e_P-e_Q\in\mathcal R_m.
\tag{3.1}
\]

#### Proof

On the ground set \([2m]\setminus\{a,b\}\), the Johnson graph on
\((m-1)\)-sets is connected.  Choose a path

\[
 P-\{a\}=K_0,K_1,\ldots,K_t=Q-\{b\}.
\]

For \(K\) on this path put

\[
                         g(K)=e_{K\cup\{b\}}-e_{K\cup\{a\}}.
\]

If \(K_i=S\cup\{z\}\) and \(K_{i+1}=S\cup\{z'\}\), then

\[
 g(K_i)-g(K_{i+1})
 =e_{S\cup\{b,z\}}+e_{S\cup\{a,z'\}}
  -e_{S\cup\{a,z\}}-e_{S\cup\{b,z'\}},
\]

which is a rectangle of the form (0.3), up to orientation.  Summing
along the path telescopes to (3.1).  \(\square\)

### Lemma 3.2 (symmetric exchanges generate every fibre)

If \(z\in\mathbb Z^{\binom{[2m]}m}\) and \(Az=0\), then \(z\) is an
integral sum of symmetric-exchange vectors (3.1).

#### Proof

Split \(z=z^+-z^-\) into two multisets of \(m\)-sets.  The two
multisets have the same number of members, because summing all rows of
\(Az=0\) gives \(m\sum_Dz_D=0\).  Label their members arbitrarily as
the row vertices of two bipartite incidence graphs.  Both graphs have
row degree \(m\), and \(Az=0\) says that they have the same degree at
every ground-coordinate vertex.

The standard alternating-cycle switching argument for bipartite graphs
with a fixed degree sequence transforms one graph into the other by
two-row, two-coordinate switches.  Such a switch replaces two rows
\(P,Q\) by

\[
                         P-a+b,\qquad Q-b+a

\]

for some \(a\in P\setminus Q\), \(b\in Q\setminus P\).  It is exactly
the symmetric exchange (3.1).  Summing the switches gives \(z\).
\(\square\)

Lemmas 3.1--3.2 prove (0.4).  Notice that no positivity or path through
one coefficient fibre is asserted: this is an equality of integral
signed lattices.

## 4. Collateral is charged only to singleton-marginal change

Let \(z\in\mathbb Z^{\binom{[2m]}m}\) have total sum zero, and put

\[
                              e=Az.
\tag{4.1}
\]

Then \(\sum_i e_i=0\).  Pair positive and negative units of \(e\).  For
each pair \(a\to b\), choose an \((m-1)\)-set \(K\) avoiding \(a,b\)
and put

\[
                         u_{a,b,K}=e_{K\cup\{b\}}
                                      -e_{K\cup\{a\}}.
\tag{4.2}
\]

The sum \(u\) of these

\[
                           s={1\over2}\|e\|_1
\tag{4.3}
\]

unit transfers satisfies \(Au=e\).  Hence \(z-u\in\ker A\), and
Section 3 writes \(z-u\) as a sum of the collar-neutral two-top macros
of Section 1.

Every unit transfer (4.2) is one literal boundary swap.  At each
nonmiddle protected length its derivative has \(L^1\)-norm at most two,
and there are fewer than \(2H\) such lengths.  Thus all the rectangle
terms cost zero and the unpaired swaps cost at most

\[
                    4Hs=2H\|Az\|_1,
\]

which proves (0.5).  In particular \(Az=0\) gives exact zero vertical
collateral in the formal signed catalogue.

This is precisely the correct interface with near-flat marginal
rounding: if a physical coefficient \(K\) and its abstract low-collision
target \(L\) have the same singleton marginals, then \(A(L-K)=0\).
The all-depth toll of the required middle displacement is therefore not
the obstruction at the signed-relation level.

## 5. Sparse open banks cannot reach the near-flat target

Assume in this section the calibrated regime
\(H=(1+o(1))\sqrt{m\log m}\).

The preceding positive result does not make the lift sparse.  Let
\(\mathcal S_\sigma\) be the legal master-order coefficient from
`MATH_THEOREM_PSI_TWO_BASE_EXCHANGE_FLATNESS_AND_ISOLATED_HIGH_STATE_20260727.md`,
and let \(K\) be its middle load.  Its total mass is

\[
                         T=\rho W=(1-o(1))W,
\tag{5.1}
\]

and its support is contained in a set \(\mathcal A_\sigma\) with

\[
                         |\mathcal A_\sigma|
                         \le2m\,2^{-H}W=o(W).
\tag{5.2}
\]

Let \(L\) be any nonnegative integer load of total \(T\) with
\(\Psi(L)=o(W)\).  Since

\[
                         (L_D-1)_+\le\binom{L_D}{2},
\]

the mass of \(L\) on \(\mathcal A_\sigma\) is at most

\[
 \sum_{D\in\mathcal A_\sigma}L_D
 \le|\mathcal A_\sigma|+\Psi(L)=o(W).
\tag{5.3}
\]

Therefore

\[
 {1\over2}\|K-L\|_1
 \ge\sum_{D\notin\mathcal A_\sigma}L_D
 =T-o(W)=(1-o(1))W.
\tag{5.4}
\]

One boundary swap changes the middle load by one unit transfer and has
\(L^1\)-norm two.  Middle-neutral moves do not affect (5.4).  Thus any
chronological route from \(K\) to \(L\) using boundary swaps as its only
middle-nonneutral steps needs at least \(T-o(W)\) such swaps.  This is
(0.6).

In particular, if every top is equipped with at most one boundary
toggle, then the entire bank has at most

\[
 N=\binom{2m}{M}=(1+o(1)){W\over m}=o(W)
\]

nonneutral steps and cannot perform the lift.  The same conclusion
holds for every \(o(W)\)-size open bank, even though its swaps may be
paired into perfectly collar-neutral rectangles.

## 6. Exact boundary

Proved:

1. an explicit two-top, two-boundary-swap macro on literal common-core
   paths;
2. exact cancellation at every \(h\ne H\), with the middle signs
   checked in (0.3);
3. realization of every elementary hypersimplex rectangle;
4. generation of the complete zero-singleton-marginal lattice by these
   physical rectangle directions;
5. formal vertical toll at most \(2H\|Az\|_1\) for an arbitrary
   zero-total middle displacement, and zero toll when \(Az=0\); and
6. a statewise lower bound of \((1-o(1))W\) boundary swaps for lifting
   the master-order state to any \(\Psi=o(W)\) load.

Not proved:

1. that a long signed rectangle decomposition can be ordered as legal
   transitions of one actual table;
2. that the required initial shores occur with enough multiplicity in
   an arbitrary current coefficient;
3. that \(\Theta(W)\) swaps can be recycled through only
   \(N\sim W/m\) tops while retaining one path per top at every time; or
4. coefficient one.

The nonclosed lift question is therefore no longer blocked by
all-depth collateral.  Its exact residual is **dense composability**:
turn the collar-neutral rectangle lattice into a chronological flow
with average top reuse \(\Theta(m)\).  A sparse catalyst bank cannot do
this, and the closed router cannot do it, but neither theorem rules out
a dense recyclable open bank.
