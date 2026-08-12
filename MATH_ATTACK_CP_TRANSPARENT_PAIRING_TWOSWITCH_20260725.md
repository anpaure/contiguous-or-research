# The \(\mathrm{CP}_A\) gate: transparent pairing two-switches and triangular shadow trades

Date: 2026-07-25

Method: pure mathematics only.  No search, solver, or computer-assisted
enumeration is used.

## 0. Verdict

This note continues Theorem 4.8 and Corollary 4.9 of
ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md.  The target is the weak
covering-prefix gate \(\mathrm{CP}_A\), not an SCD.

One useful local multiframe move can be proved exactly.

* Take two synchronized recursive paths in adjacent pair strata of one
  coordinate matching.  Their current transition pairs are
  \[
    \{a,A\},\qquad \{b,B\}.
  \]
* Exchange their outgoing tails and replace these pairs by the matching
  two-switch
  \[
    \boxed{\{a,A\},\{b,B\}\longmapsto
           \{a,B\},\{b,A\}.}
  \]
* Transpose \(a,b\) in the useful collars carried by the exchanged tails.
  The transposed coordinate lies strictly above the middle owner, moves one
  queue position to the right at every rotor step, and falls into the
  residual block after \(H+1\) steps.  At that point the modified collar is
  exactly the old collar again.

The resulting paths are legal bridge-one paths.  They use the switched
frame internally, return to the old frame without a reset, preserve every
middle owner, preserve every lower flag, and do not increase the number of
path components.

At upper depth \(q\), the exact load change is a sum of \(q\) signed
\(2\times2\) trades:

\[
 \boxed{
 \Delta\mu_q^+
 =\sum_{k=1}^{q}
 \left(
  \mathbf e_{Q_{k,q}+A+b}
 +\mathbf e_{Q_{k,q}+B+a}
 -\mathbf e_{Q_{k,q}+A+a}
 -\mathbf e_{Q_{k,q}+B+b}
 \right).}
 \tag{0.1}
\]

Every \(Q_{k,q}\) is disjoint from \(a,b,A,B\) and has size
\(m+q-2\).  All lower load vectors are unchanged.  Complementing and
reversing the construction gives the lower-only dual move.

Thus one transparent switch can alter \(2q\) upper owner--target incidences
at depth \(q\), exactly the critical service scale in the fixed-frame
capacity bound.  A family of \(\Theta(W/H)\) owner-disjoint switches can in
principle move \(\Theta(W)\) Gaussian-depth incidences while retaining the
original

\[
 p=O(W/\ell)=o(W/H)
 \qquad(H\ll\ell)
\]

path count.

This does not prove \(\mathrm{CP}_A\).  The remaining problem is to select
and sign a critical-density family of these coherent triangular trades so
that every lower and upper target is hit.  The move below proves that local
legality, exact middle ownership, transparent frame change, and the required
shadow displacement are simultaneously possible.

## 1. Useful-state conventions

A full radius-\(H\) useful state is

\[
 \omega=(L;z_1,\ldots,z_{2H};R),
 \qquad |L|=|R|=m-H,
 \tag{1.1}
\]

where the displayed parts form an ordered partition of \([2m]\).  Its
middle owner and flags are

\[
 X(\omega)=L+\{z_1,\ldots,z_H\},
 \tag{1.2}
\]

\[
 L_q(\omega)=L+\{z_1,\ldots,z_{H-q}\},
 \qquad 0\le q\le H,
 \tag{1.3}
\]

\[
 U_q(\omega)=L+\{z_1,\ldots,z_{H+q}\},
 \qquad 0\le q\le H.
 \tag{1.4}
\]

The bridge-one rotor shift with \(x\in L\) and \(y\in R\) is

\[
 \begin{split}
 &(L;z_1,\ldots,z_{2H};R)\\
 &\quad\longrightarrow
 (L-x+y;x,z_1,\ldots,z_{2H-1};R-y+z_{2H}).
 \end{split}
 \tag{1.5}
\]

Its middle projection is the Johnson move

\[
 X\longmapsto X-z_H+y.
 \tag{1.6}
\]

Every coordinate permutation preserves (1.5).  This elementary equivariance
is what makes the temporary frame change below literal rather than merely
combinatorial.

## 2. The four-coordinate collar square

Assume \(m-H\ge3\).  Choose pairwise disjoint data

\[
 L,\quad
 c_1,\ldots,c_{H-1},\quad
 u_1,\ldots,u_H,\quad
 a,b,A,B,\quad R_0,
 \tag{2.1}
\]

with

\[
 |L|=m-H,\qquad |R_0|=m-H-3.
 \tag{2.2}
\]

Put

\[
 S=L+\{c_1,\ldots,c_{H-1}\},
 \qquad |S|=m-1,
 \tag{2.3}
\]

\[
 R_a=R_0+\{b,A,B\},
 \qquad
 R_b=R_0+\{a,A,B\},
 \tag{2.4}
\]

and define the two source states

\[
 \omega_a=
 (L;c_1,\ldots,c_{H-1},a,u_1,\ldots,u_H;R_a),
 \tag{2.5}
\]

\[
 \omega_b=
 (L;c_1,\ldots,c_{H-1},b,u_1,\ldots,u_H;R_b).
 \tag{2.6}
\]

Their middle owners are

\[
 X_a=S+a,\qquad X_b=S+b.
 \tag{2.7}
\]

Fix \(x\in L\).  The old-frame rotor successors obtained by adding \(A\)
and \(B\) are

\[
 \eta_A=
 (L-x+A;
  x,c_1,\ldots,c_{H-1},a,u_1,\ldots,u_{H-1};
  R_0+\{b,B,u_H\}),
 \tag{2.8}
\]

\[
 \eta_B=
 (L-x+B;
  x,c_1,\ldots,c_{H-1},b,u_1,\ldots,u_{H-1};
  R_0+\{a,A,u_H\}).
 \tag{2.9}
\]

Thus

\[
 \omega_a\longrightarrow\eta_A,
 \qquad
 \omega_b\longrightarrow\eta_B
 \tag{2.10}
\]

are bridge-one rotor arcs with middle supports

\[
 \{a,A\},\qquad\{b,B\}.
 \tag{2.11}
\]

Let

\[
 \tau=(a\ b).
 \tag{2.12}
\]

Direct substitution in (2.8)--(2.9) gives

\[
 \omega_a\longrightarrow\tau\eta_B,
 \qquad
 \omega_b\longrightarrow\tau\eta_A,
 \tag{2.13}
\]

again as bridge-one rotor arcs.  Their middle supports are

\[
 \{a,B\},\qquad\{b,A\}.
 \tag{2.14}
\]

Equations (2.11)--(2.14) are the local matching two-switch.  Notice that
the four middle owners involved are unchanged as a set:

\[
 S+a,\quad S+b,\quad S+A,\quad S+B.
 \tag{2.15}
\]

Only the two successor assignments and the useful collars at \(S+A,S+B\)
change.

## 3. Transparent tail-exchange theorem

The local square becomes a legal finite path surgery when the two old tails
are synchronized.

Let

\[
 P_A=(\omega_a,\alpha_1,\alpha_2,\ldots),
 \qquad
 P_B=(\omega_b,\beta_1,\beta_2,\ldots)
 \tag{3.1}
\]

be directed bridge-one rotor paths with

\[
 \alpha_1=\eta_A,\qquad \beta_1=\eta_B.
 \tag{3.2}
\]

Put

\[
 \theta=(a\ b)(A\ B).
 \tag{3.3}
\]

Assume that, through time \(H+1\),

1. \(\beta_k=\theta\alpha_k\);
2. neither \(a\) nor \(b\) belongs to the middle owner of
   \(\alpha_k,\beta_k\);
3. for \(1\le k\le H\), the state \(\alpha_k\) has \(a\) in singleton
   position \(H+k\) and \(b\) in its residual block, while \(\beta_k\)
   has \(b\) in position \(H+k\) and \(a\) residual; and
4. at time \(H+1\), both \(a,b\) lie in the residual block of each state.
5. for \(1\le k\le H\), there is a set \(S_k\), disjoint from
   \(a,b,A,B\), such that the two owners are \(S_k+A,S_k+B\);
   moreover \(b,B\) are residual in \(\alpha_k\) except for the displayed
   singleton \(a\), and \(a,A\) are residual in \(\beta_k\) except for the
   displayed singleton \(b\).

These hypotheses are verified for recursive twin tails in Section 5.

### Theorem 3.1 (transparent matching two-switch)

Under the preceding hypotheses, replace (3.1) by

\[
 P_A'=
 (\omega_a,\tau\beta_1,\ldots,\tau\beta_H,
   \beta_{H+1},\beta_{H+2},\ldots),
 \tag{3.4}
\]

\[
 P_B'=
 (\omega_b,\tau\alpha_1,\ldots,\tau\alpha_H,
   \alpha_{H+1},\alpha_{H+2},\ldots).
 \tag{3.5}
\]

Then:

1. every arc of \(P_A',P_B'\) is bridge-one;
2. the two new paths use exactly the same middle owners as the two old
   paths, once each;
3. the number of path components is unchanged;
4. the first two new arcs use the switched pairs (2.14);
5. for the next \(H+1\) transitions the tails are certified by the switched frame
   \[
     \mathcal P^*
     =\mathcal P-\{\{a,A\},\{b,B\}\}
       +\{\{a,B\},\{b,A\}\};
     \tag{3.6}
   \]
6. at time \(H+1\) the useful states agree exactly with the old tails, so
   the frame returns to \(\mathcal P\) with no cut or reset.

#### Proof

The two first arcs are (2.13).  Every old internal tail arc
\(\beta_k\to\beta_{k+1}\) remains bridge-one after applying \(\tau\), since
(1.5) is coordinate-equivariant.  The same holds for the \(\alpha\)-tail.

At time \(H+1\), both \(a,b\) lie in the same residual block.  Transposing
them fixes the entire ordered state:

\[
 \tau\alpha_{H+1}=\alpha_{H+1},
 \qquad
 \tau\beta_{H+1}=\beta_{H+1}.
 \tag{3.7}
\]

Therefore the last conjugated arc joins the unmodified old tail legally.

For \(1\le k\le H\), the owners of \(\alpha_k,\beta_k\) contain neither
\(a\) nor \(b\), so \(\tau\) fixes those owners.  The new paths merely
exchange the two old owner tails after the sources.  Hence the owner
multiset and the number of path components are unchanged.

The frame statement follows by applying \(\tau\) to the old pairs.
All pairs outside (2.11) are fixed during the synchronized interval, while
(2.11) becomes (2.14).  Equation (3.7) permits the old completion pairing
to be restored without changing the physical useful state. \(\square\)

The move is transparent in the literal sense: it replaces bridge-one arcs
by bridge-one arcs and introduces no additional word position.

## 4. Exact shadow effect

Let \(\mu_q^-\) and \(\mu_q^+\) be the lower and upper target-load vectors
of a useful-state transversal.  Only the states at times
\(1,\ldots,H\) in the two tails are modified.

### Theorem 4.1 (triangular upper-shadow trade)

For the switch in Theorem 3.1,

\[
 \boxed{\Delta\mu_q^-=0\qquad(0\le q\le H).}
 \tag{4.1}
\]

For every upper depth \(1\le q\le H\), there are sets

\[
 Q_{k,q}\subseteq[2m]\setminus\{a,b,A,B\},
 \qquad |Q_{k,q}|=m+q-2
 \quad(1\le k\le q),
 \tag{4.2}
\]

such that the upper load change is exactly (0.1).

Each summand in (0.1):

* has total coefficient zero;
* has zero coordinate margins; and
* is the diagonal-to-cross exchange for the two pairings
  \(\{a,A\},\{b,B\}\) and \(\{a,B\},\{b,A\}\).

#### Proof

At time \(k\le H\), the only difference between an old tail state and its
\(\tau\)-image is that one of \(a,b\) occupies singleton position \(H+k\)
and the other lies in the residual block.  Every lower flag uses only the
base block and the first \(H\) singletons.  Hence all lower flags are
fixed, proving (4.1).

An upper depth-\(q\) flag reaches singleton position \(H+q\).  It is
therefore changed at time \(k\) if and only if \(k\le q\).  The two old
states are \(\theta\)-conjugate.  Removing the owner coordinates \(A,B\)
and the displaced coordinates \(a,b\) from their upper flags leaves one
common set \(Q_{k,q}\), disjoint from all four coordinates.  The old flags
are

\[
 Q_{k,q}+A+a,\qquad Q_{k,q}+B+b,
 \tag{4.3}
\]

whereas the new flags are

\[
 Q_{k,q}+A+b,\qquad Q_{k,q}+B+a.
 \tag{4.4}
\]

Summing (4.4) minus (4.3) over \(1\le k\le q\) proves (0.1).
Every coordinate appears with the same multiplicity on the two sides of
one summand, which proves the margin assertions. \(\square\)

Thus one switch changes at most \(2q\) upper occurrences at depth \(q\)
and

\[
 2\sum_{q=1}^Hq=H(H+1)
 \tag{4.5}
\]

upper owner--depth incidences in total.  These constants are exact before
possible coincidences among targets belonging to different \((k,q)\).

### Corollary 4.2 (lower-dual switch)

Complement every state, reverse the useful singleton order, and reverse
the path directions.  The resulting legal transparent switch preserves
all upper flags and has the complement-dual signed trade on the lower
flags.

### Corollary 4.3 (a sufficient hole-filling sign test)

At depth \(q\), let \(n_q^-(T)\) and \(n_q^+(T)\) be the negative and
positive multiplicities of \(T\) in (0.1).  If the old load satisfies

\[
 \mu_q^+(T)\ge n_q^-(T)+1
 \quad\text{whenever }n_q^-(T)>0,
 \tag{4.6}
\]

then the switch creates no new upper hole at depth \(q\).  Every target
with old load zero and \(n_q^+(T)>0\) becomes covered.

#### Proof

Equation (4.6) leaves every negatively charged target with positive final
load.  Every positively charged old hole receives positive load. \(\square\)

The test is deliberately one-sided.  Duplicates may be spent to fill holes;
no SCD ownership or exact target multiplicity is required by
\(\mathrm{CP}_A\).

## 5. Recursive fixed-frame realization

The hypotheses of Theorem 3.1 are not artificial.  They occur in the
recursive \(F_\ell\) cover in adjacent pair strata.

Fix a coordinate matching \(\mathcal P\) containing

\[
 p=\{a,A\},\qquad r=\{b,B\}.
 \tag{5.1}
\]

Choose two pair strata which agree everywhere except that:

* in the first stratum, \(p\) is split with orientation \(a\) and \(r\)
  is empty;
* in the second, \(r\) is split with orientation \(b\) and \(p\) is
  empty.

Choose the same \(\ell-1\) other active split pairs in both strata.  Let

\[
 \theta=(a\ b)(A\ B)
 \tag{5.2}
\]

identify their \(\ell\)-dimensional orientation fibres, and use
\(\theta\)-conjugate copies of the recursive factor \(F_\ell\).

### Lemma 5.1 (recursive twin-tail lemma)

Assume \(H<\ell\).  At every corresponding occurrence at which the first
path flips \(p\) and the second flips \(r\), the two radius-\(H\) collar
paths satisfy all hypotheses of Theorem 3.1.

#### Proof

Equivariance under the coordinate bijection \(\theta\) gives
\(\beta_k=\theta\alpha_k\).  The current transitions remove \(a,b\) and
insert \(A,B\), respectively.  In the radius-\(H\) rotor state, the removed
coordinate begins at middle singleton position \(H\).  After the current
transition it occupies position \(H+1\), then moves right by one singleton
position at every rotor step.

The transition word on an \(F_\ell\)-cycle is \(\pi\pi\).  Hence the
current active pair is not used again for the next \(\ell-1\) transitions.
The other special pair is empty and inactive in that stratum.  Consequently
the owners have the common form \(S_k+A,S_k+B\), and the opposite special
pair stays residual on each side.  Since
\(H<\ell\), neither \(a\) nor \(b\) can return to a middle owner during the
next \(H\) transitions.  After \(H+1\) total transitions, the removed
coordinate has fallen past position \(2H\) into the residual block.  The
inactive coordinate was residual throughout.  This proves all five tail
hypotheses. \(\square\)

For the standard Gaussian choice \(H=\lceil A\sqrt m\rceil\), one may take
a power of two

\[
 H\ll\ell\ll m.
 \tag{5.3}
\]

The low-split exceptional strata have exponentially small middle mass.
Cutting the remaining \(2\ell\)-cycles once gives a fixed-frame recursive
path cover with

\[
 p_0=O(W/\ell)+o(W/H)=o(W/H).
 \tag{5.4}
\]

Every application of Theorem 3.1 to two distinct path components preserves
this component count.

## 6. Exact reduction to a switching transversal

Start with the fixed-frame recursive path cover in Section 5 and its one
full useful state at every middle owner.  Cut the recursive cycles at a
common phase, so the nonexceptional paths have a common forward layer
coordinate.  Apply a family \(\mathcal S^+\) of upper switches from
Theorem 3.1 and a family \(\mathcal S^-\) of lower-dual switches.

Call the family **time-compatible** if its collar bubbles are disjoint on
every current strand and, at each switch layer, its tail exchanges form a
matching of the strands present at that layer.  Equivalently, the exchanges
compose layer by layer as permutations of the path strands.

### Proposition 6.1 (switching-to-\(\mathrm{CP}_A\) implication)

If a time-compatible family of switches can be chosen so that the final
useful flags cover every lower and upper target through depth \(H\), then
the resulting states form a covering prefix transversal with a bridge-one
path cover having

\[
 p=p_0=o(W/H).
 \tag{6.1}
\]

Consequently \(\mathrm{CP}_A\) holds.

#### Proof

At a fixed layer, the switched successor arcs form a bijection from the
incoming strands to the outgoing strands.  Inducting over the common layer
coordinate shows that every middle owner is still used once and every
initial strand has one continuation to the terminal layer.  Disjoint collar
bubbles make all useful-state modifications legal simultaneously.
Therefore the component count remains \(p_0\).  The coverage hypothesis is
exactly the definition of a covering prefix transversal.  Corollary 4.9 of
the multi-frame resolution note now applies. \(\square\)

At Gaussian depth \(q=\Theta(H)\), one switch changes at most \(2q\)
occurrences.  The fixed-frame deficit is \(\Theta_A(W)\), so at least
\(\Omega_A(W/H)\) switches are necessary.  This agrees with the available
packing scale: one switch occupies two tail intervals of \(H+1\) owners,
and hence a middle-owner partition can contain at most \(O(W/H)\)
owner-disjoint switches.

The constants therefore close at the correct order.  There is no local
reset or component-count obstruction.  The remaining assertion is the
following purely integral support theorem.

> **Coherent triangular switching transversal — UNPROVED.**  In the
> fixed-frame recursive path cover, choose
> \(O_A(W/H)\) time-compatible upper and lower transparent switches
> so that the sum of their signed trades, applied to the fixed-frame shadow
> loads, is positive on every target through depth \(H\).

This is weaker than constructing an SCD.  It allows arbitrary final
multiplicities, uses duplicates as the resource in Corollary 4.3, and asks
only for coverage.

## 7. Audit

1. **Flush length.**  The removed coordinate starts at position \(H\) in
   the source, occupies positions \(H+1,\ldots,2H\) during the next \(H\)
   states, and reaches the residual block at time \(H+1\).  Rejoining at
   time \(H\) would be an off-by-one error.
2. **No hidden reset.**  Every new arc is either one of the explicit rotor
   arcs (2.13) or the coordinate conjugate of an old bridge-one arc.
3. **Middle ownership.**  The two sources keep their labels and exchange
   entire tails.  Applying \(\tau\) does not change a tail owner because
   \(a,b\) are absent from it.
4. **Component count.**  The theorem is stated for two path components.
   It exchanges their terminal tails and leaves two components.  A
   same-component switch requires a separate cyclic-order audit.  For many
   switches, owner-disjointness alone is insufficient; Proposition 6.1
   additionally requires a common forward layering and strand-permutation
   compatibility.
5. **Frame meaning.**  The temporary matching is the genuine two-switch
   (3.6), not merely a renamed certificate for the old transition.
6. **Shadow scope.**  The upper formula (0.1) accounts for every changed
   flag.  All lower flags are pointwise fixed.  The dual move is needed for
   lower repair.
7. **Point margins.**  Every signed \(2\times2\) trade has zero total and
   zero coordinate margins, as any exact-factor shadow difference must.
8. **Coverage, not SCD.**  Corollary 4.3 spends duplicate load and preserves
   positivity.  No exact nonmiddle ownership or radius census is asserted.
9. **Critical density.**  The local move proves feasibility at the
   \(\Theta(W/H)\) scale; it does not prove that favorable, disjoint signs
   can be selected at that density.
10. **No general converse.**  The note supplies a sufficient
    \(\mathrm{CP}_A\) construction route.  It makes no claim that every
    near-optimal OR word has this recursive-frame normal form.

The legal multiframe move and its complete shadow effect are proved above.
The coherent switching transversal is the only statement marked unproved.
