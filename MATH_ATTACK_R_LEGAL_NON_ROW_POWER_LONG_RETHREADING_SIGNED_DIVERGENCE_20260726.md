# Legal non-row-power singleton rethreading and the signed-divergence barriers

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external source is used.

## 0. Exact outcome

Put

\[
 n=2m+1,\qquad
 W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname {Cat}_m.
 \tag{0.1}
\]

This note asks for a legal non-row-power trade which rethreads a positive
fraction of the canonical odd-wreath components into long singleton-Ucycle
components while keeping the two nested prefix systems under signed control.
Fixed-pair two-copy conjugates are not used.

There is one genuine positive theorem and three sharp obstructions.

1. **A legal positive-density successor rethreading.**  For every
   \(R\in\mathcal D_{m-2}\), the two canonical MSW rows

   \[
                   1100R,\qquad1010R
   \tag{0.2}
   \]

   share an exact ordered \((m-1)\)-state.  Cross-splicing their
   successors changes no ordered \(m\)-arc and merges their two
   \(n\)-wreaths into one \(2n\)-arc singleton-Ucycle.  The
   \(J=\operatorname {Cat}_{m-2}\) displayed pairs are row-disjoint, so
   all switches are simultaneous.  Thus

   \[
   C_{\rm new}=B-J,
   \qquad
   \frac JB=\frac{m(m+1)}{(4m-6)(4m-2)}\longrightarrow\frac1{16},
   \tag{0.3}
   \]

   and a fraction \(2J/B\to1/8\) of all old wreath rows is fused.
   Every lower-prefix multiplicity is unchanged exactly.

2. **The upper system is cheaply repairable but is not signed-cancelled.**
   Protect lower ranks \(m-q\) and upper ranks \(m+1+q\),
   \(0\le q\le H\).  Two set-valued fans of length \(2H+1\) per
   switch retain every initially present upper target.  With
   \(\Delta_H^-\) the aggregate initial lower defect,

   \[
   \boxed{
   L_H\le
   W+(B-J)(m+H)+2J(2H+1)+2\Delta_H^- .}
   \tag{0.4}
   \]

   Relative to separately linearizing the old wreaths this saves exactly

   \[
                    J(m-3H-2)
                    =\left(\frac1{32}+o(1)\right)W
   \tag{0.5}
   \]

   when \(H=O(\sqrt m)\).  This is a legal literal repair theorem, not
   a signed-cancellation theorem.  In the raw rethreaded singleton spine,
   every new seam has a repeated coordinate at distance \(m+1\).  If
   \(\mathfrak S_H\) is the aggregate half-\(\ell^1\) upper-minus-lower
   occurrence divergence through these depths, then

   \[
   \boxed{
       \mathfrak S_H\ge \frac{JH(H+1)}2.}
   \tag{0.6}
   \]

   In particular, for \(H=\lfloor A\sqrt m\rfloor\),

   \[
       \mathfrak S_H\ge\left(\frac{A^2}{64}+o_A(1)\right)W.
   \tag{0.7}
   \]

   Thus the positive round obtains its coefficient saving from common
   set-valued fans, not from Gaussian signed-divergence cancellation.

3. **The complete certified successor hierarchy cannot make genuinely
   long components on positive mass.**  Every known canonical portal

   \[
                 P1100R\longleftrightarrow P1010R
   \tag{0.8}
   \]

   is the top-level primitive-token rewrite \(B_2\leftrightarrow A_1A_1\),
   where \(A_1=10\) and \(B_2=1100\).  Its component invariant is the
   ordered list of all other primitive factors together with the total
   \(A_1/B_2\)-semilength in each gap.  If \(q_m\) is the number of
   portal components, then

   \[
   \sum_{m\ge0}q_mz^m
      =\frac1{1-z-z(C(z)-1-z)},
   \qquad
   \frac{q_m}{C_m}\longrightarrow\frac{64}{81}.
   \tag{0.9}
   \]

   Moreover

   \[
       \frac1{C_m}\sum_K|K|^2\longrightarrow\frac94.
   \tag{0.10}
   \]

   Hence the fraction of rows lying in portal components of size at least
   \(s_m\to\infty\) is at most

   \[
                      \frac{9/4+o(1)}{s_m}=o(1).
   \tag{0.11}
   \]

   The entire certified catalogue therefore cannot put positive row mass
   into \(\omega(n)\)-length singleton-Ucycles, regardless of scheduling.

4. **The explicit genuinely long rotor seed also fails intrinsically.**
   For odd \(m\), the strict alternating \(A,B,A,B,\ldots\) rotor
   component has \(2m(m+1)\) distinct owners and length \(\Theta(m^2)\).
   Its top signed divergence is nevertheless an invariant of its owner
   block.  If a full exact circulation places \(A_{\rm alt}\) owner
   occurrences in coordinate conjugates of these components, then

   \[
   \boxed{
      M_0^+\ge\frac{A_{\rm alt}}2,
      \qquad
      \frac12\|R_m-L_m\|_1\ge\frac{A_{\rm alt}}2.}
   \tag{0.12}
   \]

   Even if upper depth zero is omitted, the first lower shadow obeys

   \[
   \boxed{
      M_1^-\ge
      \left(\frac{A_{\rm alt}}2-\frac{2W}{m+2}\right)_+.}
   \tag{0.13}
   \]

   Thus no positive fraction of owner mass can be placed in this
   \(\Theta(m^2)\)-long coordinate orbit while either prefix system has
   \(o(W)\) defect.  No coordinate conjugation, phase choice, or
   owner-disjoint packet reverses its top sign.

There is also a correction to the former incidence-\(C_6\) route.  In
every Boolean owner-transversal rotor circulation, an incidence cell
contains at most one selected arc.  Therefore no active \(C_6\) shore
exists anywhere, and every fixed-port Boolean trade is trivial.  The
formal \(C_6\) vector remains an integral kernel identity, but it has an
empty activation face.

The exact surviving gate is consequently a genuinely new, state-moving
family of long components whose top upper profile is asymptotically
rainbow and whose nested signed divergence cancels across a many-component
flow network.  Neither the certified top-level MSW portals, the strict
alternating rotor orbit, nor the formal fixed-port \(C_6\) supplies it.

## 1. Ordered-arc successor systems

An oriented wreath word

\[
                       \omega=(w_0,\ldots,w_{n-1})
\tag{1.1}
\]

is a cyclic permutation of \([n]\).  It supplies the ordered \(m\)-arcs

\[
 e_i=(w_i,w_{i+1},\ldots,w_{i+m-1})
\tag{1.2}
\]

from the ordered prefix state of length \(m-1\) to the ordered suffix
state of length \(m-1\).  In an exact wreath factor the supports of the
\(W\) arcs (1.2) are the members of \(\binom{[n]}m\), once each.

At a common ordered state, the successor pairing of two incoming and two
outgoing arcs can be crossed.  This does not change the arc multiset.  If
the two old pairings lie on distinct directed circuits, their
transposition merges the two circuits into one.  The resulting circuit
is a literal cyclic singleton word: every consecutive pair of selected
arcs overlaps in the same ordered \((m-1)\)-word.

For \(0\le q\le H\), define the lower occurrence vector

\[
 L_q(S)=\#\{\hbox{selected arcs whose first }m-q
                  \hbox{ letters have support }S\}
 \quad\left(S\in\binom{[n]}{m-q}\right).
\tag{1.3}
\]

Define \(U_q(T)\), \(|T|=m+1+q\), to count cyclic starts whose next
\(m+1+q\) singleton letters have OR exactly \(T\).  A start whose window
repeats a coordinate has smaller OR rank and contributes to no coordinate
of \(U_q\).

In a wreath permutation, complementation sends every length-\((m+1+q)\)
cyclic interval to the opposite length-\((m-q)\) interval.  Hence, after
reindexing upper targets by complementation,

\[
                         \overline U_q^{,0}=L_q^0.
\tag{1.4}
\]

A successor switch retains every selected \(m\)-arc, and therefore

\[
                         L_q^1=L_q^0
                         \qquad(0\le q\le H).
\tag{1.5}
\]

Thus the signed upper-minus-lower change after rethreading is exactly

\[
                  D_q=\overline U_q^{,1}-L_q^1
                     =\overline U_q^{,1}-\overline U_q^{,0}.
\tag{1.6}
\]

This is the signed occurrence quantity used in Section 4.  It is distinct
from the cost of an appended set-valued provider: one provider letter may
restore many occurrences that contribute separately to (1.6).

## 2. The canonical disjoint MSW successor bank

For a Dyck root \(x\), the MSW tight coordinate word is the step-two
reading of its omitted-label word.  Fix \(R\in\mathcal D_{m-2}\), and
put

\[
                         X_R=1100R,\qquad Y_R=1010R.
\tag{2.1}
\]

The exact MSW concatenation rule gives one common tail

\[
 T=(t_0,t_1,\ldots,t_{2m-4}).
\tag{2.2}
\]

Split it by parity:

\[
 E=(t_0,t_2,\ldots,t_{2m-4}),
 \qquad
 O=(t_1,t_3,\ldots,t_{2m-5}).
\tag{2.3}
\]

Then \(|E|=m-1\), \(|O|=m-2\), and, after cyclic rotation, the two
tight words are

\[
 \boxed{
 \omega_{X_R}=(4,3,E,2,1,O),
 \qquad
 \omega_{Y_R}=(2,4,E,1,3,O).}
\tag{2.4}
\]

### Theorem 2.1 (positive-density exact successor fusion)

For every \(m\ge2\), cross-splicing the successors at the common state
\(E\) in (2.4) merges the two \(n\)-wreath circuits into one
\(2n\)-arc singleton-Ucycle and preserves the complete selected ordered
\(m\)-arc multiset.

The switches for all \(R\in\mathcal D_{m-2}\) can be made
simultaneously.  With

\[
                         J=C_{m-2},
\tag{2.5}
\]

the resulting factor has \(J\) components of length \(2n\),
\(B-2J\) components of length \(n\), and therefore

\[
                         C_{\rm new}=B-J.
\tag{2.6}
\]

Every middle owner and every lower-prefix multiplicity remain exact.

#### Proof

Equation (2.4) displays the same ordered \((m-1)\)-state \(E\) in the
two rows.  Let \(i_X,i_Y\) be the two incoming arcs and \(o_X,o_Y\) the
two outgoing arcs at that state.  Replace

\[
                         i_X\mapsto o_X,\quad i_Y\mapsto o_Y
\]

by

\[
                         i_X\mapsto o_Y,\quad i_Y\mapsto o_X.
\]

Both new joins overlap in the same ordered state \(E\), so they are
literal singleton joins.  A transposition of successors lying on two
distinct permutation cycles merges those cycles into one.  No selected
arc is added or deleted, proving owner and lower-prefix preservation.

The two root classes in (2.1) are disjoint, and deleting their first four
bits recovers \(R\).  Hence the displayed row pairs are pairwise
disjoint.  Their incident arcs are disjoint, so the successor
transpositions commute, even if two abstract state labels \(E\) happen
to agree.  This proves (2.6). \(\square\)

The exact Catalan ratio is

\[
 \frac{C_{m-2}}{C_m}
 =\frac{m}{4m-6}\frac{m+1}{4m-2}
 =\frac{m(m+1)}{(4m-6)(4m-2)}.
\tag{2.7}
\]

Thus \(J/B\to1/16\), while the proportion of old rows participating in
the fused components is \(2J/B\to1/8\).

This is a zero-arc, non-row-power **circuit rethreading**: it changes the
successor pairing between two rows while retaining their individual
ordered arcs.  It is not a coordinate relabelling of two independent
copies.  Since its selected-arc incidence vector is unchanged, it is not
a nontrivial factor-fibre trade.  It is also only a bounded two-row
fusion: the new component has length \(2n\), and (2.6) still leaves
\((15/16+o(1))B\) components.

## 3. Exact two-prefix repair and literal accounting

Around one old successor transition write

\[
 \ldots,x_{-H},\ldots,x_{-1},x_0,x_1,\ldots,x_m,
 x_{m+1},\ldots,x_{m+H},\ldots,
\tag{3.1}
\]

where \(x_0,\ldots,x_{m-1}\) is the incoming ordered \(m\)-arc and
\(x_m\) is the old appended coordinate.  Put

\[
                         K=\{x_0,\ldots,x_m\}.
\tag{3.2}
\]

### Lemma 3.1 (one-transition upper fan)

Assume \(0\le H\le m\).  The set-valued word

\[
 \boxed{
  (\{x_{-H}\},\ldots,\{x_{-1}\},K,
    \{x_{m+1}\},\ldots,\{x_{m+H}\})}
\tag{3.3}
\]

has length \(2H+1\) and realizes every old upper target of rank
\(m+1+q\), \(0\le q\le H\), whose interval depends on this successor
pairing; equivalently, the interval contains the full transition block
\(x_0,\ldots,x_m\).

#### Proof

At depth \(q\), the affected old intervals are indexed by
\(0\le t\le q\) and have OR

\[
 T_{q,t}
 =\{x_{-t},x_{-t+1},\ldots,x_{m+q-t}\}.
\tag{3.4}
\]

In (3.3), take the last \(t\) left singleton letters, the core \(K\),
and the first \(q-t\) right singleton letters.  Their contiguous OR is
exactly (3.4). \(\square\)

One successor transposition changes two old transitions.  Put

\[
 \delta_q^-=\#\{S\in\tbinom{[n]}{m-q}:L_q^0(S)=0\},
 \qquad
 \Delta_H^-=\sum_{q=0}^H\delta_q^-.
\tag{3.5}
\]

The initial complement identity (1.4) makes the initial upper missing
count equal to \(\delta_q^-\) at the same depth.

### Theorem 3.2 (literal two-prefix compiler for the fusion bank)

The fused factor of Theorem 2.1 has a literal set-valued contiguous-OR
word covering every initially covered lower and upper target through
depth \(H\), and every missing target can be appended separately, with
the length bound (0.4).

#### Proof

Linearize every final singleton circuit by repeating its first \(m+H\)
symbols.  Since the circuit lengths sum to \(W\), this costs

\[
                         W+(B-J)(m+H).
\]

Lower targets are retained by (1.5).  Apply Lemma 3.1 to the two changed
old transitions of every switch; this costs \(2J(2H+1)\) and retains
every old upper target.  Finally append each initially missing lower and
upper target as one set-valued letter, at total cost \(2\Delta_H^-\).
This proves (0.4). \(\square\)

The separately linearized wreath factor costs \(W+B(m+H)\) before the
same initial-defect append.  Subtracting (0.4) gives the exact saving

\[
 J(m+H)-2J(2H+1)=J(m-3H-2).
\tag{3.6}
\]

For \(H=O(\sqrt m)\), the fan term is

\[
                 O(JH)=O\!\left(\frac{WH}{m}\right)=o(W),
\]

and (2.7) gives (0.5).

The theorem preserves the initial lower histogram; it does **not** prove
that the initial MSW lower defect \(\Delta_H^-\) is \(o(W)\).

## 4. The same fusion bank has linear Gaussian signed divergence

Assume \(m\ge3\) in this section.

The two new seams at one portal are, from (2.4),

\[
                         4,3,E,1,3
\tag{4.1}
\]

and

\[
                         2,4,E,2,1.
\tag{4.2}
\]

In (4.1) the two copies of \(3\), and in (4.2) the two copies of \(2\),
are at forward distance exactly

\[
                         |E|+2=m+1.
\tag{4.3}
\]

There is no shorter new recurrence.  A distance below \(m\) would repeat
a coordinate inside one selected ordered \(m\)-arc.  At distance exactly
\(m\), the two adjacent selected \(m\)-arcs would have the same support,
contradicting exact middle ownership.  Rotating or interchanging the two
circuits only moves or exchanges the seams.
Reversing both reverses the same distances, while reversing only one
destroys equality of the ordered state \(E\).  Thus (4.3) cannot be
removed by an orientation choice at this portal.

### Theorem 4.1 (rank-correct mass-loss inequality)

Let \(D_q\) be the signed vector (1.6) after all \(J\) disjoint portal
switches.  For every \(0\le q\le H\le m\),

\[
                         \boxed{\|D_q\|_1\ge2qJ.}
\tag{4.4}
\]

Consequently

\[
 \boxed{
  \frac12\sum_{q=0}^H\|D_q\|_1
       \ge\frac{JH(H+1)}2.}
\tag{4.5}
\]

#### Proof

Fix one repeated pair at distance \(d=m+1\).  A cyclic interval of
length \(d+q=m+1+q\) contains both copies for exactly \(q\) consecutive
starting positions.  Each such interval has OR rank at most \(m+q\), so
it contributes no occurrence to the rank-\((m+1+q)\) vector.

The two cross transitions of one fused \(2n\)-cycle are separated by
exactly \(n\) selected arcs.  Every deficient window just counted crosses
the corresponding cross transition.  Since its length is at most \(n\),
the two deficient-start blocks are disjoint.  Different row pairs lie in
different fused components.  Hence at least \(2qJ\) of the \(W\) starts
are rank-deficient at depth \(q\).

Before switching, every length at most \(n\) interval of a wreath
permutation has distinct symbols.  Therefore

\[
 \sum_T U_q^0(T)=W,
 \qquad
 \sum_T U_q^1(T)\le W-2qJ.
\]

After complement reindexing, the total coordinate sum of \(D_q\) is at
most \(-2qJ\).  The \(\ell^1\)-norm is at least the absolute coordinate
sum, proving (4.4).  Summing \(q\) proves (4.5). \(\square\)

Using \(J=(1/16+o(1))B=(1/32+o(1))W/m\) and
\(H^2=(A^2+o_A(1))m\) gives (0.7).

This lower bound is deliberately compatible with Theorem 3.2.  The
signed ledger charges each destroyed rank occurrence, whereas one fan
core services a triangular family of such occurrences.  The raw spine
does not cancel; the literal compiler compresses its repair.

## 5. Complete invariant of the certified portal graph

Factor a Dyck word uniquely into primitive excursions.  Let

\[
 A_1=10,\qquad B_2=1100,
\]

and call every primitive excursion of semilength at least three a large
token.  Since \(P,R\) in (0.8) are complete Dyck words, a certified
portal changes exactly one top-level token

\[
                         B_2\longleftrightarrow A_1A_1.
\tag{5.1}
\]

It fixes the ordered large-token list and the total small semilength in
every gap.  Conversely every two tilings of a fixed gap by parts one and
two are connected using (5.1).  These data are therefore complete
component invariants.

Let

\[
 C(z)=\sum_{m\ge0}C_mz^m,
 \qquad
 G(z)=\sum_{k\ge3}C_{k-1}z^k=z(C(z)-1-z).
\tag{5.2}
\]

### Theorem 5.1 (component count and square-mass)

The component-count generating function is

\[
                         Q(z)=\frac1{1-z-G(z)}.
\tag{5.3}
\]

If the portal components are \(K\), then their size-square generating
function is

\[
 \sum_{m\ge0}\left(\sum_{K\subseteq\mathcal D_m}|K|^2\right)z^m
 =\frac{F_2(z)}{1-G(z)F_2(z)},
\tag{5.4}
\]

where

\[
 F_2(z)=\sum_{s\ge0}F_{s+1}^2z^s
       =\frac{1-z}{1-2z-2z^2+z^3}.
\tag{5.5}
\]

Consequently (0.9)--(0.11) hold.

#### Proof

A component is a sequence of large tokens, with one nonnegative integer
small semilength in every gap.  There is one component choice for each
gap size, giving gap series \((1-z)^{-1}\).  The ordinary sequence
construction gives

\[
 \frac{(1-z)^{-1}}{1-G(z)(1-z)^{-1}}
 =\frac1{1-z-G(z)},
\]

which is (5.3).

A gap of total small semilength \(s\) has \(F_{s+1}\) tilings by
\(A_1,B_2\).  Component sizes multiply over gaps.  When component sizes
are squared and summed, the gap series is therefore \(F_2(z)\), proving
(5.4).  Formula (5.5) is the standard Fibonacci-square recurrence and
also follows directly by multiplying its rational denominator through
the coefficient sequence.

Put \(\sigma=\sqrt{1-4z}\).  At \(z=1/4\),

\[
 C(z)=2-2\sigma+O(\sigma^2),
 \qquad
 G(z)=\frac3{16}-\frac12\sigma+O(\sigma^2).
\]

Therefore

\[
 Q(z)=\frac{16}{9}-\frac{128}{81}\sigma+O(\sigma^2),
\]

and comparison with the singular coefficient \(-2\sigma\) of \(C(z)\)
gives \(q_m/C_m\to64/81\).

Also

\[
 F_2(1/4)=\frac{48}{25},
 \qquad
 G(1/4)F_2(1/4)=\frac9{25}.
\]

Thus the right side of (5.4) has expansion

\[
                         3-\frac92\sigma+O(\sigma^2),
\]

and singular-coefficient comparison gives (0.10).  Finally,

\[
 \sum_{|K|\ge s_m}|K|
 \le\frac1{s_m}\sum_K|K|^2,
\]

which proves (0.11). \(\square\)

Within this certified graph, successor transpositions along a spanning
forest merge all rows of one portal component into one singleton circuit.
Thus (5.3) is also the exact minimum component count attainable from this
catalogue alone.  Its limiting fusion rank is only

\[
                         \left(\frac{17}{81}+o(1)\right)B.
\]

More importantly, (0.11) says that almost all fused circuits contain only
\(O(1)\) old wreaths.  No scheduling of the known portals gives the
required growing component mass.

## 6. Intrinsic obstruction for the strict alternating long rotor

Assume in this section that

\[
                         m=2r+1\ge3.
\tag{6.1}
\]

The strict alternating rotor component has length

\[
                         2L,\qquad L=m(m+1).
\tag{6.2}
\]

Its position permutation \(G=BA\) has two cycles, of lengths \(m\) and
\(m+1\).  Let \(Z\) be the label set in the \(m\)-cycle.  Relative to
\(Z\sqcup Z^c\), the owner block splits as

\[
 \mathcal B_\uparrow
 =\mathcal I_{m,r}(Z)\times\mathcal I_{m+1,r+1}(Z^c),
\tag{6.3}
\]

\[
 \mathcal B_\downarrow
 =\mathcal I_{m,r+1}(Z)\times\mathcal I_{m+1,r}(Z^c).
\tag{6.4}
\]

Both shores have size \(L\), and their union consists of
\(2L\) distinct middle owners.

### Theorem 6.1 (intrinsic top sign)

For one strict alternating component,

\[
 \boxed{
 L_m=\mathbf1_{\mathcal B_\uparrow}
       +\mathbf1_{\mathcal B_\downarrow},
 \qquad
 R_m-L_m=\mathbf1_{\mathcal B_\uparrow}
       -\mathbf1_{\mathcal B_\downarrow},
 \qquad
 R_m=2\mathbf1_{\mathcal B_\uparrow}.}
\tag{6.5}
\]

The signed partition in (6.5) is determined by the unlabelled owner
block \(\mathcal B\).  Indeed, its coordinate degrees are

\[
 d_{\mathcal B}(x)=
 \begin{cases}
 m(m+1),&x\in Z,\\
 m^2,&x\in Z^c,
 \end{cases}
\tag{6.6}
\]

and for \(X\in\mathcal B\),

\[
                         (R_m-L_m)(X)=m-2|X\cap Z|.
\tag{6.7}
\]

Consequently every coordinate automorphism of \(\mathcal B\) preserves
both signed shores.  Two coordinate-conjugate alternating components
with the same owner block have identical, never opposite, top divergence.

#### Proof

The two lower owner orbits are precisely (6.3)--(6.4), each with load
one.  In the rotor divergence identity at rank \(m\), the positive base
set

\[
                         U_m=\{m+2,\ldots,n\}
\]

has intersection profile \((r,r+1)\), while the negative base set

\[
                         V_m=\{1,m+2,\ldots,n-1\}
\]

has profile \((r+1,r)\).  Their \(G\)-orbits are therefore
\(\mathcal B_\uparrow\) and \(\mathcal B_\downarrow\), respectively.
This proves (6.5).

For \(x\in Z\), the two product shores contain it in

\[
 (r)(m+1)+(r+1)(m+1)=m(m+1)
\]

owners.  For \(x\in Z^c\), the corresponding count is

\[
 m(r+1)+mr=m^2.
\]

These degrees differ by \(m\), so the owner block intrinsically recovers
\(Z\) as its high-degree coordinate class.  Formula (6.7) is \(+1\)
on (6.3) and \(-1\) on (6.4).  It follows that every block automorphism
preserves the signs. \(\square\)

### Corollary 6.2 (owner-disjoint packets cannot cancel)

Let \(t\) coordinate-conjugate alternating components have pairwise
disjoint owner blocks, and put

\[
                         A=2Lt.
\tag{6.8}
\]

Then

\[
 \boxed{
  \left\|\sum_{i=1}^t(R_m-L_m)_i\right\|_1=A,
  \qquad
  \frac12\left\|\sum_{i=1}^t(R_m-L_m)_i\right\|_1
      =\frac A2.}
\tag{6.9}
\]

#### Proof

Each component contributes \(+1\) on \(L\) owners and \(-1\) on
another \(L\) owners.  Pairwise owner-disjointness makes all these
supports disjoint, so equality holds in the triangle inequality. \(\square\)

### Theorem 6.3 (arbitrary-completion upper and lower hole bounds)

Let a full integral owner-transversal rotor circulation contain whole
strict alternating components on \(A_{\rm alt}\) owners.  The remaining
components are arbitrary.  Let \(M_0^+\) denote the number of missing
upper \(q=0\) targets, and let \(M_1^-\) denote the number of missing
lower \(q=1\) targets.  Then (0.12)--(0.13) hold.

#### Proof

By (6.5), the alternating part has \(A_{\rm alt}\) upper rank-\(m\)
occurrences supported on exactly \(A_{\rm alt}/2\) targets.  The other
\(W-A_{\rm alt}\) occurrences can cover at most that many additional
targets.  Since the rank-\(m\) target universe has size \(W\),

\[
 |\operatorname {supp}R_m|
 \le \frac{A_{\rm alt}}2+W-A_{\rm alt}
 =W-\frac{A_{\rm alt}}2.
\]

This proves the first inequality in (0.12).  Globally \(L_m\equiv1\).
On the doubled shore of every alternating block, \(R_m-L_m\ge1\), so
the positive mass of this signed vector is at least
\(A_{\rm alt}/2\).  Its coordinate sum is zero; hence its half-\(\ell^1\)
norm is at least \(A_{\rm alt}/2\).  This proves the second inequality.

At lower rank \(m-1=2r\), the two prefix position sets of one alternating
component have the same intersection profile \((r,r)\).  The Chinese
remainder theorem makes their two length-\(L\) \(G\)-orbits equal.
Therefore the \(2L\) lower occurrences of one component have load two
on only \(L\) targets.  The alternating part supports at most
\(A_{\rm alt}/2\) targets, and the completion supports at most
\(W-A_{\rm alt}\) further targets.  Since

\[
 \binom n{m-1}=\frac{m}{m+2}W
               =W-\frac{2W}{m+2},
\]

the number of lower holes is at least (0.13). \(\square\)

If \(M_0^+=o(W)\), Theorem 6.3 forces
\(A_{\rm alt}=o(W)\).  If upper depth zero is not charged but
\(M_1^-=o(W)\), it again forces \(A_{\rm alt}=o(W)\).  Under exact
lower depth-one coverage it gives the sharper bound

\[
                         A_{\rm alt}\le\frac{4W}{m+2}.
\tag{6.10}
\]

The number of alternating cycles on these owners is

\[
                         \frac{A_{\rm alt}}{2m(m+1)}.
\]

Relative to putting those owners in \(n\)-wreaths, their total possible
component saving is at most \(A_{\rm alt}/n\).  Hence the two-prefix
bounds make the saving \(o(W/m)\), not a positive fraction of the
baseline \(W/n\).

The obstruction is stronger than rank-one balancing.  At rank one a
packet of \(t\) components could cancel only when their \(m\)-coordinate
classes form a regular design, necessarily with \(n\mid t\).  For
\(t=n\), the cyclic length-\(m\) intervals in \(\mathbb Z_n\) satisfy
this class-regularity equation.  Owner-disjoint flow completion is a
separate condition.  The intrinsic rank-\(m\) sign (6.9) shows that no
nonempty owner-disjoint packet cancels the full nested family.

## 7. Universal correction to the incidence-hexagon route

Return to the injective de Bruijn rotor model.  Its arcs are injective
\((n-1)\)-words

\[
                         e=(x_1,\ldots,x_{n-1}),
\]

with owner maps

\[
 \kappa_0(e)=\{x_1,\ldots,x_m\},
 \qquad
 \kappa_1(e)=\{x_2,\ldots,x_{m+1}\}.
\tag{7.1}
\]

Assume \(m\ge2\).

Let \(y\) be a nonnegative owner-transversal flow:

\[
 \sum_{\kappa_0(e)=X}y_e=1
 \qquad(X\in\tbinom{[n]}m),
\tag{7.2}
\]

together with de Bruijn vertex balance.

### Lemma 7.1 (shifted-owner equality)

Every such flow satisfies

\[
                         \boxed{
 \sum_{\kappa_1(e)=X}y_e=1
 \qquad(X\in\tbinom{[n]}m).}
\tag{7.3}
\]

#### Proof

Sum vertex balance over all \((n-2)\)-vertices whose first \(m\)
entries have support \(X\).  Their total outgoing mass is the owner row
(7.2).  Their total incoming mass is exactly the left side of (7.3).
\(\square\)

Fix an injective \((n-3)\)-word \(w\), whose complementary labels are
\(\{a,b,c\}\), and form the six incidence-cell arcs

\[
                         e_{pq}=(p,w,q),\qquad p\ne q.
\tag{7.4}
\]

Every one has the same shifted owner

\[
                         \kappa_1(e_{pq})
                         =\{w_1,\ldots,w_m\}.
\]

### Theorem 7.2 (universal cell occupancy and fixed-port rigidity)

For every nonnegative owner-transversal flow,

\[
                         \boxed{
 \sum_{p\ne q}y_{e_{pq}}\le1.}
\tag{7.5}
\]

Consequently no Boolean circulation contains either alternating
three-arc shore of the incidence \(C_6\).  Moreover, two Boolean
owner-transversal circulations with the same tail and head port degrees
are identical.  Equivalently, every fixed-port Boolean trade is trivial.

#### Proof

Inequality (7.5) is the shifted-owner row (7.3) restricted to the six
displayed arcs.

The split tail--head incidence graph decomposes by the common interior
word \(w\).  Its component at \(w\) is
\(K_{3,3}\) minus the diagonal perfect matching, hence one \(C_6\).
Its integer circulation kernel is generated by the difference of its two
alternating three-edge shores.  A nonzero port-preserving Boolean
replacement would require one feasible factor to contain an entire
shore, contradicting (7.5). \(\square\)

The same contradiction has a direct flow interpretation.  An active
shore enters the three heads \((w,a),(w,b),(w,c)\).  Flow forces one
selected outgoing arc at each head, but all these outgoing arcs have the
one owner \(\{w_1,\ldots,w_m\}\).

Thus the formal \(C_6\) vector really is in the tail, head, owner, and
prefix kernel, but the corresponding integral face is empty.  Any legal
rotor trade must move neighbouring states and ports at the same time.

## 8. Audited boundary

The following statements are proved.

1. The \(C_{m-2}\) disjoint MSW successor switches are legal, integral,
   non-row-power singleton-Ucycle circuit rethreadings.  They fuse
   \(1/8+o(1)\) of the old rows in pairs and preserve every lower-prefix
   multiplicity.  They are zero-arc switches, not factor-fibre mobility.
2. Their entire initially present upper ledger is repairable with
   \(2(2H+1)C_{m-2}=o(W)\) set-valued letters at Gaussian height.
3. Their raw singleton spine has aggregate signed divergence at least
   \((A^2/64+o_A(1))W\) at \(H=A\sqrt m\).  The fan theorem is a
   compressed repair, not cancellation.
4. The complete certified portal graph has component density
   \(64/81+o(1)\) and bounded normalized second component moment
   \(9/4+o(1)\).  It cannot create growing circuits on positive row
   mass.
5. The explicit \(\Theta(m^2)\)-long strict alternating rotor component
   has an intrinsic, non-reversible top divergence.  Positive owner
   density forces linear upper top holes and linear lower depth-one
   holes, even with arbitrary completion.
6. The incidence-\(C_6\) port kernel has no integral activation point;
   every fixed-port Boolean rotor trade is trivial.

What is **not** proved is a universal obstruction to every possible
non-row-power exact factor.  The surviving architecture must use a new
many-state, exterior-moving trade with all of the following properties:

\[
\begin{gathered}
\text{owner-simple long components on }\Theta(W)\text{ owners},\\
\text{upper rank-}m\text{ support }W-o(W),\\
\text{aggregate lower holes }o(W),\\
\text{and nested signed-divergence norm }o(W).
\end{gathered}
\tag{8.1}
\]

Local nested-star divergence atoms satisfy the signed equation on owner
fibres, but their de Bruijn flow completion requires selected sources to
be unions of \(BA\)-orbits of length \(m(m+1)\).  The owner matching and
the orbit flow have not been rounded simultaneously.  Theorems 6.1--6.3
show that the most obvious such orbits, the strict alternating ones,
cannot be the required positive-density solution.

Two independent adversarial audits checked the decisive steps.  Both
rederived the \(2H+1\) fan indexing, the \(2qJ\) rank-correct mass loss
and \(A^2/64\) Gaussian constant, the \(64/81\) component-density and
\(9/4\) square-mass constants, the signs in (6.5), both
arbitrary-completion hole bounds, and the shifted-owner proof of
fixed-port rigidity.  They also enforced the two scope distinctions used
above: the MSW operation is a zero-arc circuit rethreading rather than
factor-fibre mobility, and a \(2n\)-cycle is bounded fusion rather than
the required \(\omega(n)\)-long component.

No coefficient-one theorem is claimed.
