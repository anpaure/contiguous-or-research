# Stateful Pósa rotations and the coherent BTK sink obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Exact outcome

Let

\[
 \Omega=A\mathbin{\dot\cup}B,\qquad |A|=|B|=m,
 \qquad W=\binom{2m}{m},
\]

and put

\[
H=\lfloor\sqrt m\,\omega\rfloor,
 \qquad \omega=\log\log m.
\tag{0.1}
\]

The displayed choice is the canonical slowly super-Gaussian scale.  All
finite statements below hold for arbitrary integral \(H\); the
asymptotic isolation census uses only \(H/\sqrt m\to\infty\) and
\(H\le m\).

There are two conclusions.

First, Pósa rotation has an exact word-level form in the corrected
two-queue automaton. If

\[
 R=(X_0,X_1,\ldots,X_s)
\]

is two-sided \(H\)-safe and \(X_iX_s\) is a Johnson chord, put

\[
 R^{(i)}=(X_0,\ldots,X_i,X_s,X_{s-1},\ldots,X_{i+1}).
\tag{0.2}
\]

Then \(R^{(i)}\) is two-sided \(H\)-safe if and only if, starting from
the actual live queues at \(X_i\), the automaton accepts the chord and
the first

\[
                 \min\{H-1,s-i-1\}
\tag{0.3}
\]

transitions of the reversed suffix. No static endpoint test is being
used. Complement-reversal carries (0.2) to the corresponding rotation
at the opposite end of \(R^\dagger\), so paired stateful rotations
commute with dagger exactly.

Second, this stateful rotation theorem does not rescue the fixed
BTK/product-SCD atlas. Put the standard BTK SCD on each half and use its
whole rank-\(m\) product diagonals as atoms. The atom's own last five
insertions create a reachable history cut. Every atom of length \(h\)
satisfying

\[
                     7\le h\le H-8
\tag{0.4}
\]

is isolated in the exact one-sided endpoint digraph: neither orientation
can be followed by, or preceded by, any whole oriented BTK product atom.
Thus the obstruction already holds in the lower insertion queue; the
upper queue only adds restrictions. The number of isolated atoms is

\[
 (1-o(1))\binom m{\lfloor m/2\rfloor}^{2}
 =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.
\tag{0.5}
\]

Therefore every state-valid route made from whole BTK atoms contains at
most one atom from (0.4); in fact such an atom is a singleton whole-atom
component. This remains true after arbitrary Pósa rotations, alternating
cycles, and simultaneous compound exchanges which keep the atoms whole.
In particular a whole-atom cover has

\[
 p\ge(1-o(1))\binom m{\lfloor m/2\rfloor}^{2},
\tag{0.6}
\]

not \(O(W/m)\).

The exact escapes are internal atom splitting and long stateful
connectors. They cannot be dismissed by the sink count. The valid
compound extension is this: if two complete high-end BTK atoms of
lengths \(h,h'\) are joined by an arbitrary \(d\)-edge connector, then
their active alphabets overlap in at least \(h-4d\) coordinates.
More sharply, the last \(4d+1\) insertions of the first atom contain an
active label of the second. Consequently the join is \(H\)-unsafe
whenever

\[
                 4d+1\le h,\qquad h'+5d+1\le H.
\tag{0.7}
\]

Since \(|h'-h|\le2d\), the simpler sufficient obstruction is

\[
                 4d+1\le h,\qquad h+7d+1\le H.
\tag{0.8}
\]

Thus every bounded or \(o(h)\)-length compound connector is still
blocked on the short BTK band. A surviving whole-atom route must spend
\(\Omega(h)\) physical transitions between typical consecutive atoms,
or split one of them internally. At \(h=\Theta(\sqrt m)\), this is a
tight \(\Theta(W)\) global transition-capacity demand, not a
contradiction. Internal pivots obey the exact one-sided support criterion
in Section 4.

The obstruction is for one fixed BTK product atlas.  A genuinely
owner-disjoint mixed \(D,D^c\) atlas may have cross-colour arcs not seen
by the record-tail comparison, and raw complementation does not preserve
one SCD chainwise.  Thus the theorem closes whole-atom fixed-BTK Pósa
routing, not every possible complement-equivariant moving-frame route.

## 1. The exact two-queue word

Write a directed Johnson transition as

\[
 X_{t+1}=X_t-a_t+b_t,
 \qquad \sigma_t=\{a_t,b_t\}.
\tag{1.1}
\]

Immediately before edge \(t\), retain the insertion and removal queues

\[
 \begin{aligned}
  \mathcal I_t&=(b_j:\max\{0,t-H+1\}\le j<t),\\
  \mathcal D_t&=(a_j:\max\{0,t-H+1\}\le j<t).
 \end{aligned}
\tag{1.2}
\]

The transition is accepted exactly when

\[
                       a_t\notin\mathcal I_t,
             \qquad   b_t\notin\mathcal D_t.
\tag{1.3}
\]

Equivalently, in every interval of at most \(H\) consecutive transitions
the support pairs are pairwise disjoint. Indeed, an earlier insertion
followed by removal of the same coordinate is exactly a lower-rank
failure, and an earlier removal followed by reinsertion is exactly an
upper-rank failure. Same-role repetition forces an intervening
opposite-role repetition by legality. Thus (1.3) is necessary and
sufficient for

\[
 \left|\bigcap_{j=0}^{q}X_{t+j}\right|=m-q,
 \qquad
 \left|\bigcup_{j=0}^{q}X_{t+j}\right|=m+q
\tag{1.4}
\]

for every available \(q\le H\).

When an old transition is read backwards, its directed labels are
interchanged:

\[
 X_{t+1}\longrightarrow X_t=X_{t+1}-b_t+a_t.
\tag{1.5}
\]

This convention is important in the rotation theorem.

## 2. Exact stateful Pósa rotation

### Theorem 2.1 (word-level Pósa criterion)

Let \(R=(X_0,\ldots,X_s)\) be a simple two-sided \(H\)-safe Johnson
path. Fix \(0\le i\le s-2\), suppose \(X_i\sim_J X_s\), and define
\(R^{(i)}\) by (0.2). Initialize the automaton at \(X_i\) with the live
queues produced by the prefix \(X_0,\ldots,X_i\). Read, in order,

1. the chord \(X_i\to X_s\); and
2. the reversed old transitions
   \[
   X_s\to X_{s-1}\to\cdots\to X_{i+1}.
   \]

Then \(R^{(i)}\) is two-sided \(H\)-safe if and only if the chord and the
first \(\min\{H-1,s-i-1\}\) reversed transitions are accepted
sequentially.

#### Proof

The support word of \(R^{(i)}\) is

\[
 \sigma_0,\ldots,\sigma_{i-1},\tau,
 \sigma_{s-1},\sigma_{s-2},\ldots,\sigma_{i+1},
\tag{2.1}
\]

where \(\tau=X_i\mathbin\triangle X_s\) is the chord support. The old
edge \(\sigma_i\) is absent.

Every interval wholly inside the prefix was already safe. Every interval
wholly inside the reversed suffix is the reversal of an old interval and
has the same support pairs, so it was already safe. The only new
intervals cross \(\tau\). Sequentially applying (1.3) from the actual
prefix queues tests all of them.

After \(H-1\) reversed-suffix transitions have been accepted, every
prefix transition and the chord itself has expired from the queue. From
then on the live queue consists entirely of a reversed old suffix, whose
internal safety is known. Hence no later test is new. This proves
sufficiency. Necessity follows directly from the automaton test on the
new path. \(\square\)

The theorem is history-conditioned. The same physical chord can be legal
after one prefix and illegal after another.

### Proposition 2.2 (dagger commutation)

For a route \(R\), put

\[
 R^\dagger=(X_s^c,X_{s-1}^c,\ldots,X_0^c).
\tag{2.2}
\]

Then

\[
 (R^{(i)})^\dagger
 =(X_{i+1}^c,\ldots,X_s^c,X_i^c,\ldots,X_0^c).
\tag{2.3}
\]

This is precisely the Pósa rotation of \(R^\dagger\) performed at its
opposite end with the complementary chord \(X_s^cX_i^c\). In
particular, a state-valid rotation and its forced dagger mate remain
complement-equivariant.

#### Proof

Equation (2.3) is obtained by reversing (0.2) and complementing every
owner. Complementation and reversal preserve every support pair and
reverse its age order, so Theorem 2.1 applies on the mate exactly as on
the original route. \(\square\)

The standard BTK symmetry is reverse-complement followed by one fixed
ground-coordinate permutation and, for the product, the half swap. The
same calculation applies with that fixed permutation composed with
dagger. It transfers lower and upper hole counts by a bijection. It
should not be confused with the false assertion that one SCD is permuted
by raw complementation alone.

## 3. What a rotation preserves

Fix a decomposition of the route into atomic paths. Suppose the pivot
edge \(X_iX_{i+1}\) is a seam between two atoms. Every atom in the
suffix is merely read in reverse, and every old suffix seam other than
the pivot is also read in reverse. A lower target is an intersection of
a consecutive owner block, so reversing that block does not change the
target. It follows that every atom-internal lower target is retained
exactly.

### Corollary 3.1 (base-atlas zero loss)

If the required one-sided target family is already covered by windows
internal to the atoms, then every state-valid Pósa rotation at an
inter-atom seam preserves that coverage exactly. New crossing targets
may duplicate old targets, but duplicates cannot create a missing target.

This statement is relative to the original atom atlas. If targets first
created by an earlier seam are themselves treated as indispensable, a
later Pósa rotation can delete them. The exact support ledger follows.

## 4. Exact one-sided missing-shadow criterion

Fix a depth \(q\le H\). Let

* \(\mathcal R_q\) be the set of lower targets supplied by all windows
  unchanged by the rotation;
* \(\mathcal O_q\) be the set supplied by old windows crossing the
  deleted edge \(X_iX_{i+1}\); and
* \(\mathcal N_q\) be the set supplied by new windows crossing the chord.

Let \(\mathcal U_q=\binom{\Omega}{m-q}\). Then exactly

\[
 \begin{aligned}
  M_q(R)&=|\mathcal U_q|-|\mathcal R_q\cup\mathcal O_q|,\\
  M_q(R^{(i)})&=|\mathcal U_q|-|\mathcal R_q\cup\mathcal N_q|,
 \end{aligned}
\tag{4.1}
\]

and therefore

\[
 \boxed{
 M_q(R^{(i)})-M_q(R)
 =|\mathcal O_q\setminus\mathcal R_q|
  -|\mathcal N_q\setminus\mathcal R_q|.}
\tag{4.2}
\]

This is the exact one-sided missing-shadow test. In particular, the
rotation does not increase holes exactly when

\[
 |\mathcal N_q\setminus\mathcal R_q|
 \ge |\mathcal O_q\setminus\mathcal R_q|.
\tag{4.3}
\]

For the unweighted all-depth functional the exact criterion is

\[
 \sum_{q=1}^{H}|\mathcal N_q\setminus\mathcal R_q|
 \ge
 \sum_{q=1}^{H}|\mathcal O_q\setminus\mathcal R_q|.           \tag{4.3a}
\]

If nonincrease is required separately at every depth, one needs (4.3)
for each \(q\), not merely the summed inequality (4.3a).

The stronger containment

\[
                  \mathcal O_q\subseteq\mathcal R_q
\tag{4.4}
\]

makes the old seam entirely redundant and is sufficient without using
any new target. Equation (4.2), not chronological occurrence count, is
the literal missing-shadow criterion.

At most \(q\) old and \(q\) new \(q\)-windows meet one replaced edge, so

\[
                     M_q(R^{(i)})-M_q(R)\le q.
\tag{4.5}
\]

The resulting crude aggregate bound is \(H(H+1)/2\) per rotation. It is
not suitable at a linear number of rotations; (4.3) must be used.

### Internal pivots

Let an atom have edges \(1,\ldots,h\), and delete its \(t\)-th edge,
\(1\le t\le h\). The exact number of its internal \(q\)-windows which
cross that edge is

\[
 c_q(t,h)
 =\left(
   \min\{t-1,h-q\}-\max\{0,t-q\}+1
  \right)_+.
\tag{4.6}
\]

If \(H\ge h\), summing over every available depth gives

\[
 \boxed{
 \sum_{q=1}^{h}c_q(t,h)=t(h-t+1)\ge h.}
\tag{4.7}
\]

Indeed, the left side counts all edge intervals contained in
\(\{1,\ldots,h\}\) and containing edge \(t\). Such an interval is
specified by choosing its left endpoint in \(\{1,\ldots,t\}\) and its
right endpoint in \(\{t,\ldots,h\}\).

Thus rotating at an atom boundary can be zero-loss relative to the base
atlas, whereas rotating through the inside of an \(h\)-edge atom exposes
at least \(h\) old base occurrences. Whether the associated target
identities become holes is governed exactly by (4.2).

## 5. The BTK adjacent-endpoint overlap

For a binary word \(w=w_1\cdots w_m\), let

\[
 D_w(t)=\sum_{j=1}^{t}(2w_j-1),
\tag{5.1}
\]

and let \(\mathcal R(w)\) be the set of strict ascending record times of
\(D_w\). In the standard BTK parenthesis matching, these are exactly the
unpaired one-positions. If \(w\) is the high member of rank \(k\ge m/2\)
and \(h=2k-m\), the coordinates used between the symmetric ranks
\(m-k\) and \(k\) are exactly the last \(h\) elements of
\(\mathcal R(w)\).

For completeness, both assertions and the perturbation constant are
proved next.

### Lemma 5.0 (record tails and four-edit stability)

Let \(w\) be a binary word.

1. Its unpaired one-positions in the BTK matching are exactly
   \(\mathcal R(w)\).
2. If \(|w|=k\ge m/2\), \(h=2k-m\), and
   \(\tau_1<\cdots<\tau_M\) are its record times, then the active
   coordinates between ranks \(m-k\) and \(k\) are
   \[
                  \{\tau_{M-h+1},\ldots,\tau_M\}.       \tag{5.1a}
   \]
3. Exchanging one zero and one one changes the complete record-time set
   in at most four positions. Changing one bit changes it in at most two
   positions.

#### Proof

After cancellation of all BTK \(01\)-pairs in a prefix, its uncancelled
word has the form \(1^a0^b\).  A newly read one is unpaired exactly when
\(b=0\), equivalently when the new height is larger than every preceding
height.  This proves the first assertion.  Successive record events first
hit levels \(1,\ldots,M\), where \(M=\max_tD_w(t)\).  Hence the BTK chain
containing \(w\) has minimum rank \(a_0=k-M\).  Its rank-\((m-k)\)
member uses the first

\[
                    (m-k)-a_0=M-h
\]

unpaired positions, while \(w\) uses all \(M\).  Their difference is
(5.1a).

For the perturbation assertion, first exchange positions \(u<v\), with
\(w_u=0,w_v=1\), to obtain \(w'\).  Then

\[
 D_{w'}(t)=D_w(t)+2\quad(u\le t<v),                 \tag{5.1b}
\]

and the walks agree outside that interval.  Put
\(P=\max_{t<u}D_w(t)\).  Inside \([u,v)\), both walks have the same local
record times.  Such a time is a global record for \(w\) once its old
height is at least \(P+1\), and for \(w'\) once its old height is at least
\(P-1\).  Thus the lift can change only the first local visits to the two
levels \(P-1,P\), at most two times.  When the walks reunite at \(v\),
their accumulated maxima differ by at most two.  On the common suffix,
only the first at most two future record levels can therefore differ.
This proves the four-position bound.  The opposite exchange follows by
interchanging \(w,w'\).

For a one-bit change, the walks agree before the changed position and
differ by the constant \(2\) or \(-2\) thereafter.  Relative to the
common prefix maximum, only the first two suffix record levels can be
created or suppressed.  This proves the two-position bound. \(\square\)

We also use the following elementary ordered-tail fact.  If finite
ordered sets \(E,E'\) obey \(|E\mathbin\triangle E'|\le d\), and
\(T_s(E),T_t(E')\) are their terminal \(s\)- and \(t\)-sets, then

\[
              |T_s(E)\setminus T_t(E')|
                 \le d+(s-t)_+.                         \tag{5.1c}
\]

Indeed, first replace \(T_s(E)\) by \(T_t(E)\), losing exactly
\((s-t)_+\) possible members.  Insert the elements of \(E'\setminus E\)
and then delete those of \(E\setminus E'\).  Each single edit changes a
terminal \(t\)-set in at most one member, proving (5.1c).

Applying Lemma 5.0 and (5.1c) gives the exact adjacent-endpoint input.

### Lemma 5.1 (BTK active-tail stability)

Let \(X\) be the high endpoint of a BTK product diagonal \(P\) of length
\(h\ge5\), and let \(Y\) be any Johnson-adjacent product-diagonal
endpoint. If \(Q\) is the atom ending at \(Y\), then \(Y\) is high,

\[
                         h(Q)\in\{h-2,h,h+2\},
\tag{5.2}
\]

and

\[
 \boxed{|I_A(P)\cap I_A(Q)|\ge h-4>0.}
\tag{5.3}
\]

At low endpoints the reverse-complement/half-swap statement holds with a
nonempty common physical active-label set.

#### Proof

The \(A\)-rank of a Johnson neighbor differs by at most one. Since the
rank of \(X\cap A\) is \((m+h)/2\) and \(h\ge5\), the neighbor remains
strictly above \(m/2\) and is a high endpoint. This proves (5.2).

An \(A\)-internal Johnson move exchanges two bits and changes the strict
record set in at most four places; a cross-half move changes one bit and
changes it in at most two places; a \(B\)-internal move leaves the
\(A\)-word fixed. If ordered sets differ in at most \(d\) elements, their
terminal tails of lengths \(s,t\) lose at most

\[
                         d+(s-t)_+
\]

elements from the first tail. With \(d\le4\) and \(s=t=h\), or with
\(d\le2\) and \(|s-t|=2\), at most four members of \(I_A(P)\) are lost.
This proves (5.3). The low statement is its BTK anti-automorphic image.
\(\square\)

## 6. Generated-history coherent sinks

### Theorem 6.1 (both orientations are sinks)

Let \(P\) be a BTK product diagonal of length \(h\) satisfying

\[
                              5\le h,\qquad 2h+3\le H. \tag{6.0}
\]
After either complete orientation of \(P\) is traversed, there is no
two-sided \(H\)-safe coherent continuation consisting of one Johnson
seam followed by any complete oriented BTK product diagonal.

#### Proof

First traverse \(P\) from low to high. A successor atom \(Q\) must be
entered at a Johnson-adjacent endpoint \(Y\). By Lemma 5.1 it is entered
at its high endpoint and is therefore traversed high to low. Choose

\[
                         c\in I_A(P)\cap I_A(Q).
\]

The coordinate \(c\) occurs on one edge of \(P\) and one edge of \(Q\).
In the concatenated word

\[
                 P\ ;\ \hbox{seam}\ ;\ Q,
\]

their edge indices differ by at most

\[
                  h+h(Q)\le2h+2\le H-1.
\tag{6.1}
\]

Hence the occurrences lie among \(H\) consecutive edges, violating
(1.4). If the seam itself uses \(c\), the violation occurs sooner.

For the reverse orientation, \(P\) ends at its low endpoint. Apply the
low-end part of Lemma 5.1 to get the same repeated-label contradiction.
\(\square\)

The obstruction is generated by \(P\)'s own word; no adversarial formal
queue is inserted.

The full active tail is not needed.  The last five insertions already
give the sharp bounded-history port lock used below.

### Lemma 6.2 (natural five-edge port lock)

Let a whole BTK product atom \(P\), of length at least five, be followed
by a whole atom \(Q\) across a literal endpoint seam.  The endpoints at
the seam are both high or both low.  If

\[
                              h(Q)+6\le H,             \tag{6.2}
\]

then the concatenation is not lower \(H\)-safe, in either of the two
possible endpoint types.

#### Proof

Suppose first that \(P\) is traversed low to high.  Its last five
transitions insert a five-set

\[
                         F_P\subseteq I_A(P).          \tag{6.3}
\]

The next endpoint is high, and \(Q\) is traversed high to low.  Lemma
5.1 gives

\[
                         |I_A(P)\setminus I_A(Q)|\le4, \tag{6.4}
\]

so there is a \(z\in F_P\cap I_A(Q)\).  Both seam endpoints contain
\(z\), hence the seam fixes it.  The transition inserting \(z\) in
\(P\) is one of the last five old transitions, whereas reverse \(Q\)
removes \(z\) on one of its \(h(Q)\) internal transitions.  Indexing the
seam as transition zero, the insertion index lies in
\(\{-5,-4,-3,-2,-1\}\) and the removal index lies in
\(\{1,\ldots,h(Q)\}\).  Their inclusive residence span is therefore at
most \(h(Q)+6\).  Condition (6.2) makes the lower queue reject.

If \(P\) is traversed high to low, its last five transitions insert five
members of its \(B\)-active tail.  Both seam endpoints are low, so the
forward traversal of \(Q\) removes its \(B\)-active tail.  Apply the same
record-tail estimate in the \(B\)-half.  The identical span calculation
proves the claim. \(\square\)

### Theorem 6.3 (coherent isolation)

Every whole BTK product atom \(P\) satisfying

\[
                              7\le h(P)\le H-8        \tag{6.5}
\]

has neither a predecessor nor a successor whole atom in the exact lower
\(H\)-memory endpoint digraph.  This remains true after adding the upper
queue.

#### Proof

Every endpoint-neighbour atom \(Q\) has

\[
                     h(Q)\in\{h(P)-2,h(P),h(P)+2\}.  \tag{6.6}
\]

Thus \(h(Q)\ge5\), and for the order \(P\to Q\),

\[
                         h(Q)+6\le h(P)+8\le H.       \tag{6.7}
\]

Lemma 6.2 rejects that order in either orientation.  For the reverse
order \(Q\to P\), the predecessor has length at least five and the
successor has

\[
                              h(P)+6\le H-2<H,         \tag{6.8}
\]

so Lemma 6.2 rejects that order as well.  The witness in each case lies
in the last five transitions of the actual predecessor, so this is a
coherently generated history obstruction. \(\square\)

### Corollary 6.4 (Pósa closure is trapped)

Suppose a state-valid whole-atom route ends in a sink atom \(P\). A Pósa
rotation at an earlier atom boundary whose reversed suffix contains \(P\)
and at least one further atom would put \(P\), in one of its two
orientations, before a successor atom. Theorem 6.1 forbids this. A
rotation of the final atom alone may change its entrance port or
orientation, but its terminal physical atom is still \(P\).

Thus the stateful Pósa endpoint closure cannot move past its final sink.

### Corollary 6.5 (compound-exchange invariant)

In every state-valid directed route formed from whole BTK atoms, each
atom satisfying (0.4) is an isolated singleton component. Consequently:

1. no path or cycle component containing another atom can contain it;
2. no directed cycle component contains one; and
3. every simultaneous alternating-cycle or compound seam exchange which
   preserves all atoms whole obeys the same statements.

This is stronger than failure of a particular local search: it is an
invariant of the entire whole-atom feasible fibre.

## 7. Exact sink and raw-endpoint census

Put

\[
                         c_m=\binom m{\lfloor m/2\rfloor}.
\tag{7.1}
\]

If \(h=m-2r\), every SCD has exactly

\[
 P_h=\binom mr^2-\binom m{r-1}^2
\tag{7.2}
\]

product diagonals of length \(h\). Let

\[
 L=\max\{h\in\mathbb Z:h\equiv m\pmod 2,\ 5\le h,\
                         2h+3\le H\},
 \qquad r_L={m-L\over2}.
\tag{7.3}
\]

Then \(L=H/2+O(1)\), and telescoping (7.2) gives the exact identity

\[
 \sum_{\substack{0\le h\le L\\h\equiv m\ (2)}}P_h
 =c_m^2-
   \binom m{r_L-1}^2.
\tag{7.4}
\]

Consequently the sink count itself is exactly

\[
 |\mathcal S_H|
 =c_m^2-\binom m{r_L-1}^2
  -\sum_{\substack{0\le h<5\\h\equiv m\ (2)}}P_h.
\tag{7.5}
\]

The central-binomial ratio satisfies

\[
 {\binom m{r_L-1}^2\over c_m^2}
 =\exp\left[-{L^2\over m}+o(L^2/m)\right]
 =\exp\left[-{\omega^2\over4}+o(\omega^2)\right]
 =o(1).
\tag{7.6}
\]

The finitely many \(h<5\) terms are \(o(c_m^2)\). Hence the sink family
\(\mathcal S_H\) has

\[
                         |\mathcal S_H|=(1-o(1))c_m^2.
\tag{7.7}
\]

For the stronger isolated family in Theorem 6.3, let \(\ell\) be the
least integer at least seven with \(\ell\equiv m\pmod2\), and let \(U\)
be the greatest integer at most \(H-8\) with
\(U\equiv m\pmod2\).  Telescoping (7.2) gives the exact count

\[
 |\mathcal I_H|
 =\binom m{(m-\ell)/2}^{\!2}
  -\binom m{(m-U-2)/2}^{\!2}.                     \tag{7.7a}
\]

The first term is \((1-o(1))c_m^2\).  Since
\((U+2)/\sqrt m\to\infty\), the second is
\(c_m^2\exp[-\Omega(H^2/m)]=o(c_m^2)\).  Therefore

\[
                         |\mathcal I_H|=(1-o(1))c_m^2.          \tag{7.7b}
\]

Orient every atom in \(\mathcal I_H\) both ways and retain the exact
terminal queues created by its own word.  Distinct atoms have distinct
terminal owners.  If \(\mathfrak S_H\) is this set of decorated states,
Theorem 6.3 gives the literal history-conditioned Hall cut

\[
 \boxed{
   \Gamma^+(\mathfrak S_H)=\varnothing,
   \qquad
   |\mathfrak S_H|=2|\mathcal I_H|
   =\left({4\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.}        \tag{7.7c}
\]

The exact raw endpoint count is

\[
 |\mathcal E|=2c_m^2-S_0,
\tag{7.8}
\]

where \(S_0=0\) for odd \(m\), while for even \(m\)

\[
 S_0=c_m^2-\binom m{m/2-1}^2=O(c_m^2/m).
\tag{7.9}
\]

Thus

\[
 {2|\mathcal I_H|\over|\mathcal E|}=1-o(1):
\tag{7.10}
\]

an asymptotically full fraction of oriented BTK atom exits are coherent
state sinks.

This coexists with the exact large raw average. The middle Johnson graph
is \(m^2\)-regular with least eigenvalue \(-m\), so for every vertex set
\(E\),

\[
 {2e_J(E)\over|E|}
 \ge {m(m+1)|E|\over W}-m.
\tag{7.11}
\]

Since

\[
 |\mathcal E|=\left({4\over\sqrt\pi}+o(1)\right){W\over\sqrt m},
\]

(7.11) gives raw average endpoint degree at least

\[
                 \left({4\over\sqrt\pi}+o(1)\right)m^{3/2}.
\tag{7.12}
\]

Equations (7.10)--(7.12) diagnose the failure exactly: raw endpoint
census and raw average expansion do not survive the generated history of
the fixed BTK atoms.

## 8. The \(O(W/m)\) component obstruction

By Theorem 6.3, every retained atom in \(\mathcal I_H\) is a singleton
route component. If \(u\) middle owners are omitted, at most \(u\) whole
isolated atoms can be omitted. Therefore every whole-atom route cover has

\[
                         p\ge|\mathcal I_H|-u.
\tag{8.1}
\]

In particular, with no atom surgery and \(u=o(W/\sqrt m)\),

\[
 p\ge\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m},
\tag{8.2}
\]

which exceeds \(O(W/m)\) by a factor of order \(\sqrt m\).

The hypothesis \(u=o(W/\sqrt m)\) in this direct component conclusion is
essential. Deleting one owner from every sink costs only
\(\Theta(W/\sqrt m)=o(W)\) owners and leaves the whole-atom category.
Thus (8.2) is not by itself a coefficient-one no-go. The next section
shows that even a compound connector must have length comparable with a
typical atom; it does not convert this into a hole lower bound.

## 9. Compound connectors and the distance-\(d\) obstruction

The sink theorem concerns one seam. The BTK record description extends
it to an arbitrary connector.

### Lemma 9.1 (record-tail Lipschitz bound)

Let \(X,Y\) be high-side middle owners joined by a \(d\)-edge Johnson
path all of whose owners remain on the high side.
Put

\[
 h=2|X\cap A|-m,\qquad h'=2|Y\cap A|-m,
\]

and let \(I_h(X),I_{h'}(Y)\) be their BTK active record tails. Then

\[
 \boxed{|I_h(X)\cap I_{h'}(Y)|\ge h-4d.}
\tag{9.1}
\]

Also

\[
                         |h-h'|\le2d.
\tag{9.2}
\]

#### Proof

The endpoint hypothesis in Lemma 5.1 was used only to identify the tail
length with a product-atom length; Lemma 5.0 and (5.1c) apply to every
adjacent pair of high-side owners.  They give the
one-sided loss bound

\[
 |I_{h_j}(X_j)\setminus I_{h_{j+1}}(X_{j+1})|\le4.
\]

Along the stated \(d\)-edge path, every element of the initial tail absent
from the final tail must be lost for the first time at one of the
\(d\) steps. The union bound gives loss at most \(4d\), proving (9.1).
One Johnson move changes the \(A\)-rank by at most one and hence changes
the excess by at most two, proving (9.2). \(\square\)

The high-side hypothesis is automatic when \(2d<h\), because the initial
\(A\)-rank exceeds \(m/2\) by \(h/2\).

### Theorem 9.2 (generated-history distance-\(d\) port lock)

Let a complete BTK atom \(P\) of length \(h\) be traversed low to high.
After it, read an arbitrary \(d\)-edge Johnson connector ending at the
high endpoint of a complete BTK atom \(Q\) of length \(h'\), and traverse
\(Q\) high to low. If

\[
                         4d+1\le h,\qquad h'+5d+1\le H,
\tag{9.3}
\]

then the complete word is not two-sided \(H\)-safe. The low-end statement
is identical under the BTK anti-automorphism.

#### Proof

The inequality \(4d+1\le h\) implies \(2d<h\), so every connector
owner remains on the high side and Lemma 9.1 applies.

The first inequality lets us take the set \(F\) of labels inserted on
the final \(4d+1\) transitions of \(P\). Thus

\[
                         F\subseteq I_A(P),\qquad |F|=4d+1.
\]

Lemma 9.1 says that at most \(4d\) members of the whole tail
\(I_A(P)\) are absent from \(I_A(Q)\). Hence some

\[
                         c\in F\cap I_A(Q).
\]

If the connector itself changes \(c\), the repeated-label obstruction
already occurs no later than that connector transition. Otherwise \(c\)
is removed during the reverse traversal of \(Q\). Its insertion is at
most \(4d+1\) transitions before the exit of \(P\); the connector has
\(d\) transitions; and its removal lies among the \(h'\) transitions of
\(Q\). The inclusive residence span is therefore at most

\[
                         (4d+1)+d+h'=h'+5d+1.
\]

The second inequality makes this at most \(H\), contradicting lower
\(H\)-safety. This one-sided contradiction is already enough; the upper
queue can only remove further transitions.
\(\square\)

By (9.2), the convenient sufficient form

\[
                         4d+1\le h,\qquad h+7d+1\le H
\tag{9.4}
\]

implies (9.3). Thus a compound exchange of bounded length, or more
generally \(d=o(h)\), cannot join typical complete BTK atoms while
\(h=o(H)\).

This does not yield a global component lower bound once long connectors
or internal atom pieces are allowed. The exact owner identities give

\[
                         \sum_h(h+1)P_h=W,
 \qquad                  \sum_hhP_h=W-c_m^2=(1-o(1))W.
\tag{9.5}
\]

Accordingly, spending \(\Theta(h)\) connector transitions for each of
\(\Theta(W/\sqrt m)\) typical atoms has total scale \(\Theta(W)\), which
is feasible only at constant-density efficiency. It is neither
superlinear nor negligible. A proof of an \(O(W/m)\)-component cover
must therefore solve a genuine global packing problem for these long
connectors, while an internal-pivot construction must satisfy (4.3) at
all depths.

One tempting stronger conclusion is invalid and is expressly retracted:
an uncut sink need not remain terminal after other atoms are split,
because it may be followed by an internal atom piece rather than by a
whole product atom. Hence the whole-atom sink count alone does not force
one internal cut in every sink atom and does not imply a linear
missing-shadow or occurrence loss under arbitrary atom surgery.

## 10. Final proved/conditional boundary

Proved:

1. the exact live-queue criterion for one word-level Pósa rotation;
2. exact commutation with complement/reversal;
3. exact preservation of every atom-internal lower target under seam-
   pivot rotations;
4. the exact one-sided support identity (4.2);
5. the natural five-edge port lock and coherent isolation theorem for
   every fixed BTK atom in (0.4), in both orientations;
6. the explicit empty-neighborhood lifted Hall cut (7.7c), of size
   \((4/\sqrt\pi+o(1))W/\sqrt m\), despite raw average degree
   \(\Theta(m^{3/2})\);
7. stability of the sink obstruction under every whole-atom Pósa,
   alternating-cycle, or compound exchange; and
8. the distance-\(d\) obstruction (9.3)--(9.4), which closes every
   bounded-length compound connector on the typical short band.

Not proved:

1. a global packing of the \(\Omega(h)\)-length connectors left open by
   Theorem 9.2;
2. the all-depth support inequality (4.3) after internal atom surgery;
3. an \(O(W/m)\)-component construction using a non-BTK SCD, mixed
   moving frames, or internal BTK surgery; or
4. coefficient one.

The fixed, whole-atom BTK route is therefore definitively closed. The
smallest surviving operation is an internal atom split or a genuinely
different SCD frame, together with a proof of the all-depth support
condition (4.3). Ordinary raw endpoint expansion and ordinary Pósa
rotation do not address that operation.
