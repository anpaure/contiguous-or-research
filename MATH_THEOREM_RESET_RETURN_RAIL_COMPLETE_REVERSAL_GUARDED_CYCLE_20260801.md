# A resident return rail turns the rolling reset into a complete-reversal guarded cycle

**Date:** 2026-08-01  
**Lane:** K, literal three-return lift / rolling-reset closure  
**Status:** unconditional local all-depth construction.  The combined reset
and return rail is a simple resident Johnson cycle; its opposite phase is
the complete reversal.  The phases have identical immediate palettes,
every derivative-row inventory, and complete cyclic interval-OR decks.  A
protected embedding into the global owner palette and the exterior/common
residual compiler remain open.

## 0. Outcome

Let `d>=1`, let the central owner rank be `r`, and assume

\[
                         r\ge 2d+2,
 \qquad                  k-r\ge2d+1.                        \tag{0.1}
\]

There is an explicit two-phase packet on

\[
                         M=4d+2                              \tag{0.2}
\]

distinct rank-`r` roots with all of the following properties.

1. Each phase is one simple Johnson cycle; the second is the complete
   directed reversal of the first.
2. The complete rank-`r-1` and rank-`r+1` immediate palettes are simple
   and identical in the two phases.
3. Every nonconstant coordinate run has length at least `d+1`.
4. The complete cyclic interval-union spectrum agrees at every width.
5. The maximal cyclic depth-`d` antecedents are nonempty and are literal
   reversals up to the forced index shift.  Consequently every lower
   derivative-row inventory and the complete antecedent interval-OR deck
   also agree.
6. In the four-resource projection, the attachment overlay is one cycle
   and the predecessor overlay is two parity cycles.  Opening a common
   edge gives exactly the one attachment return and two predecessor returns
   of the opened rolling reset.

Thus the previously separate rolling reset and resident long square rail
fit together without a residence or internal all-width casualty.  The
remaining problem is no longer the literal three-return packet; it is a
global protected-host/common-residual theorem.

## 1. Open the rolling reset

Put

\[
                         n=d+1,
 \qquad                  N=2n.                              \tag{1.1}
\]

Choose a permanent core `K` of rank `r-n` and private coordinates

\[
                         X_0,\ldots,X_{N-1}
\]

outside `K`.  Define the usual two-queue reset roots

\[
 T_a=K\cup\{X_a,X_{a+1},\ldots,X_{a+n-1}\},
 \qquad a\in\mathbb Z_N.                                  \tag{1.2}
\]

They form a simple Johnson cycle.  Open its edge between

\[
                         E=T_0,
 \qquad                  F=T_{N-1}.                         \tag{1.3}
\]

Put

\[
 L=E\cap F,qquad \delta=E-L=X_{n-1},qquad
 \alpha=F-L=X_{N-1}.                                      \tag{1.4}
\]

The forward reset path is

\[
                         E=T_0,T_1,\ldots,T_{N-1}=F.        \tag{1.5}
\]

## 2. The return rail

Condition (0.1) gives

\[
 |K|=r-d-1\ge d+1.                                        \tag{2.1}
\]

Choose distinct

\[
                         x_1,\ldots,x_d,b\in K              \tag{2.2}
\]

and distinct

\[
 y_1,\ldots,y_d\notin K\cup\{X_0,\ldots,X_{N-1}\}.         \tag{2.3}
\]

The second inequality in (0.1) is exactly the supply needed for (2.3).
Write

\[
 X[j]=\{x_1,\ldots,x_j\},\qquad
 Y[j]=\{y_1,\ldots,y_j\}.
\]

Define

\[
 P_j=(L-X[j])+Y[j]+\alpha,qquad0\le j\le d,               \tag{2.4}
\]

so `P_0=F`, and

\[
 Q_0=(L-X[d])+Y[d]+\delta,                                 \tag{2.5}
\]

\[
 Q_j=
 L-\{x_{j+1},\ldots,x_d\}
  +\{y_{j+1},\ldots,y_d\}+\delta,qquad1\le j\le d,       \tag{2.6}
\]

so `Q_d=E`.  This is the long return path

\[
 F=P_0,P_1,\ldots,P_d,Q_0,Q_1,\ldots,Q_d=E.                \tag{2.7}
\]

It is the rail `R_d` from
`MATH_THEOREM_BOOLEAN_HEX_RESIDENT_LONG_SQUARE_COLLAR_20260801.md`, now
attached directly to the rolling-reset seam.

## 3. The complete-reversal cycle

Without repeating the closing root, put

\[
\begin{aligned}
 Z^+=(&T_0,T_1,\ldots,T_{N-1},
       P_1,\ldots,P_d,Q_0,\ldots,Q_{d-1}).
\end{aligned}                                               \tag{3.1}
\]

Its cyclic closing edge is `Q_(d-1)->Q_d=T_0`.  Let `Z-` be the same
cyclic word with the opposite orientation, based at `T_0`:

\[
 Z^-=(T_0,Q_{d-1},\ldots,Q_0,P_d,\ldots,P_1,
       T_{N-1},T_{N-2},\ldots,T_1).                         \tag{3.2}
\]

### Theorem 3.1 (simple exact-q1 cycle)

`Z+` and `Z-` are opposite orientations of one simple rank-`r` Johnson
cycle of length `4d+2`.  Its immediate lower and upper colours are all
distinct.

#### Proof

The reset roots are distinct cyclic windows.  Every internal return root
contains at least one fresh `y_j`, so it is not a reset root.  The strict
prefix/suffix construction separates all `P` and `Q` roots, and `alpha`
versus `delta` separates their two halves.  Every successive pair differs
by one exchange, proving Johnson adjacency.

The reset path already has simple immediate palettes.  The return path's
palette formulas are those of the resident-rail theorem and are simple.
Every return upper colour contains a fresh `y_j`, whereas no reset colour
does.  Every return lower colour also contains a fresh `y_j`, except

\[
                         F-x_1\quad\hbox{and}\quad E-x_d.    \tag{3.3}
\]

Every reset lower colour contains the permanent core `K`, hence contains
both `x_1,x_d`; (3.3) cannot collide with it.  The two exceptions are
distinct because one contains `alpha` and the other `delta`.  Thus the
complete q1 palettes are simple.  Reversal changes no undirected edge, so
the two phases use the identical palettes. \(\square\)

## 4. Exact residence

### Theorem 4.1 (all positive runs are long)

Every nonconstant cyclic positive run in `Z+` has length at least `d+1`.
More precisely:

\[
\begin{array}{c|c}
\hbox{coordinate type}&\hbox{positive-run length}\\ \hline
y_j&d+1\\
\alpha,\delta&2d+1\\
x_j&3d+1\\
X_i\in(E\cap F)-K&3d+1\\
X_i\notin E\cup F&d+1.
\end{array}                                                \tag{4.1}
\]

Coordinates of `K-{x_1,...,x_d}` are constant one, and all other ground
coordinates are constant zero.  The same statement holds in `Z-`.

#### Proof

On the return rail, `y_j` occupies

\[
                         P_j,\ldots,P_d,Q_0,\ldots,Q_{j-1},
\]

exactly `d+1` consecutive roots.  It is absent on the reset path.

Coordinate `x_j` occupies the complementary return pieces

\[
                         Q_j,\ldots,Q_d,P_0,\ldots,P_{j-1}.
\]

Those pieces have total length `d+1`; the reset path replaces the seam
`E--F` by `N-1` edges and contains `x_j` everywhere, adding `N-2=2d`
internal roots to the same run.  Its length is therefore `3d+1`.

On the reset path, `alpha` has its ordinary `d+1`-root run ending at `F`,
and on the return it has the `d+1`-root run beginning at `F`.  Their shared
endpoint is counted once, giving `2d+1`; `delta` is symmetric at `E`.

Every private reset coordinate common to `E,F` occurs on the entire return
rail.  Its two boundary pieces on the opened reset path therefore merge
through the rail, giving `(d+1)+2d=3d+1`.  A private reset coordinate in
neither endpoint retains its internal reset run of length `d+1` and is
absent on the return.  This proves (4.1).  Reversal preserves every cyclic
run. \(\square\)

### Corollary 4.2

The combined cycle is legal for the depth-`d` residence criterion.  Unlike
the short square by itself, no exterior extension is needed to lengthen a
short positive run *inside this closed component*.

## 5. Complete internal OR and lower-row transparency

### Theorem 5.1 (all-width cyclic transparency)

Reversal gives a value-preserving bijection between every cyclic interval
of `Z+` and a cyclic interval of `Z-`.  Hence their complete cyclic
interval-union spectra agree at every width.

#### Proof

Equations (3.1)--(3.2) are reversals of the same cyclic root word.  Reverse
the endpoints and order of any cyclic interval; its member sets, and hence
their union, are unchanged. \(\square\)

The residence theorem gives a cyclic depth-`d` antecedent.  For definiteness
take the maximal erosion

\[
 A_j^+=\bigcap_{t=j-d}^{j}Z_t^+.                           \tag{5.1}
\]

The protected anchor `b` occurs in every root, so every `A_j^+` is
nonempty.  The run criterion gives

\[
                         D^dA^+=Z^+.                        \tag{5.2}
\]

Define `A-` by the same formula from `Z-`.

### Theorem 5.2 (literal reversed antecedent)

With indices modulo `M=4d+2`,

\[
                         A_i^-=A_{d-i}^+.                   \tag{5.3}
\]

Consequently, for every `0<=q<=d`, the row `D^q A-` is a reversal and
rotation of `D^q A+`.  Their complete row inventories agree, and the two
antecedent words themselves have identical cyclic interval-OR spectra at
every width.

#### Proof

Since `Z_i^-=Z_{-i}^+`,

\[
 A_i^-
 =\bigcap_{t=i-d}^{i}Z_{-t}^+
 =\bigcap_{s=-i}^{d-i}Z_s^+
 =A_{d-i}^+.
\]

Sliding union commutes with reversal up to the same cyclic shift, proving
the derivative statement.  The interval-OR statement follows directly
from (5.3). \(\square\)

### Corollary 5.3 (internal compiler transport)

Any occurrence-labelled matching which uses only short cells wholly inside
this closed component transports to the opposite phase by reversing its
cell intervals.  This is an exact isomorphism of the **internal**
target--cell incidence graph, not merely equality of aggregate target
counts.

## 6. The three projected returns are now closed literally

For every undirected cycle edge `Z_i Z_(i+1)`, let

\[
 I_i=Z_i\cap Z_{i+1},\qquad U_i=Z_i\cup Z_{i+1}.             \tag{6.1}
\]

The forward atom is `(I_i,U_i;Z_i,Z_(i+1))`; the reverse atom is its typed
orientation reversal.

### Theorem 6.1 (closed three-return lift)

The head--owner attachment overlay of the two phases is one alternating
cycle.  The lower--tail overlay is one alternating cycle.  The typed
tail--head predecessor overlay is exactly two alternating parity cycles.

#### Proof

At each owner `U_i`, the head changes from `Z_(i+1)` to `Z_i`, so
alternation advances one step around the `M`-cycle and gives one attachment
cycle.  The lower--tail statement is symmetric.  In the predecessor
overlay, two alternating steps change the root index by two.  Since

\[
                         M=4d+2
\]

is even, `gcd(M,2)=2`, giving exactly two parity components. \(\square\)

Opening the two phase orientations of one common edge removes one edge from
each predecessor parity component and the common owner column from the
attachment component.  It therefore recovers one attachment path and two
predecessor paths.  The return rail closes precisely the three paths
exported by the opened rolling reset, and all projections come from one
literal phase pair.

## 7. What this changes—and what it does not

This construction closes, locally and simultaneously:

* owner simplicity;
* both immediate palettes;
* depth-`d` residence;
* the complete cyclic root OR deck;
* every derivative-row inventory;
* a nonempty literal antecedent and its complete internal OR deck;
* the one attachment and two predecessor returns;
* internal compiler-cell transport under phase reversal.

It still does **not** prove a global word or an additive bound.

1. **Root-palette planting.**  The `2d` internal return roots must replace
   other rank-`r` occurrences in a spanning owner factor; they cannot simply
   be appended to a coefficient-one middle layer.
2. **Global topology.**  The packet is a closed component.  It must be
   opened and joined to the ambient path forest without losing unique
   targets.
3. **Exterior cross-windows.**  The cyclic/internal decks agree, but after
   concatenation with an unchanged exterior, intervals crossing a packet
   boundary need not correspond unless the exterior sockets are reversed
   or protected.
4. **Global upper completeness.**  Phase invariance preserves the packet's
   internal deck; it does not assert that the union of packet and ambient
   witnesses covers every upper target.
5. **Common residual compiler.**  Internal incidences reverse exactly, but
   cells crossing the cut and assignments elsewhere still require one
   common residual Hall matching.
6. **Regeneration.**  No same-parity Pascal theorem yet reproduces this
   protected component with bounded inherited state.

The next theorem is therefore a **protected complete-reversal host lemma**:
embed this `4d+2`-root component in an upper-complete owner factor with one
phase-common exterior cut and a common residual compiler.  The literal
residence and three-return parts no longer need to be supplied externally.

## 8. Independent H100 `-O3` replay

`scratch/audit_reset_return_rail_complete_reversal_20260801.cpp` constructs
the tight-coordinate instance

\[
                         r=2d+2,qquad k=4d+3
\]

for every `1<=d<=12`.  It checks root and q1 simplicity, all cyclic positive
runs, every-width cyclic OR spectra, maximal factorization, nonempty source
letters, reversal of the antecedent, every derivative-row inventory, and
the `1+2` projected cycle decomposition.

The H100 command was

```text
g++ -std=c++20 -O3 -Wall -Wextra -pedantic \
  scratch/audit_reset_return_rail_complete_reversal_20260801.cpp \
  -o /dev/shm/audit_reset_return_rail_complete_reversal_20260801
/dev/shm/audit_reset_return_rail_complete_reversal_20260801
```

The frozen verdict is

```text
PASS_RESET_RETURN_RAIL_COMPLETE_REVERSAL cases=12 d=1..12 roots=4d+2
q1=simple attachment=one_cycle predecessor=two_parity_cycles
residence>=d+1 cyclic_OR=all_widths antecedent=nonempty_reversal
all_derivative_rows=equal
```

