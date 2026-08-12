# Lane N: five-input \(D_4\) operad audit and the growing-factor gate

Date: 2026-07-26

Method: pure mathematics only. No search or computation is used.

Sources cross-audited:

* MATH_THEOREM_D4_FIVE_INPUT_OPERAD_OBSTRUCTION_20260726.md;
* MATH_ATTACK_D4_ROOT_OPERADIC_SKELETON_INTERFACE_20260726.md;
* MATH_AUDIT_D4_FRINGE_BOUNDARY_AND_SEAM_20260726.md.

Write \(C_t=\operatorname {Cat}_t\).

## 0. Verdict

Fix five ordered spectator trees

\[
                         \mathbf A=(A_0,A_1,A_2,A_3,A_4)                \tag{0.1}
\]

and vary an outer four-node ordered binary skeleton through
\(P\in D_4\).

The abstract operadic fibre is genuine: the fourteen trees

\[
                         P[\mathbf A],\qquad P\in D_4,                  \tag{0.2}
\]

have one size, are distinct, and retain the five spectators in planar
order.

The existing \(F_4\leftrightarrow G_4\) factor does not have a dense
five-input suspension. There are two different restrictions.

1. A literal token-preserving common \(D_4\)-port cylinder forces

   \[
                         A_0=A_1=A_2=\varnothing.                       \tag{0.3}
   \]

   Only the terminal slots \(A_3,A_4\) are position-stable.

2. Johnson legality of the natural zero-slot expansion of the displayed
   first \(G_4\)-edge forces

   \[
                         A_1=A_2=A_3=\varnothing.                       \tag{0.4}
   \]

For the natural statewise lift, imposing both leaves only \(A_4\).
Therefore its sharp inherited incidence ceiling is

\[
\boxed{
                         14C_{s-4}
       =\left(\frac7{128}+o(1)\right)C_s.}              \tag{0.5}
\]

There is a positive collective rerouting beyond natural statewise
expansion. For every terminal pair \(A_3=B,A_4=C\), process a small
\(D_4\) path first and then fixed complement geodesics through \(B,C\).
This gives a literal endpoint-preserving fourteen-for-fourteen \(X/Y\)
bitrade. All terminal pairs together have incidence at most

\[
\boxed{
                         14C_{s-3}
       =\left(\frac7{32}+o(1)\right)C_s.}               \tag{0.6}
\]

Thus even the strongest proved bounded-seed terminal interface cannot
cover \(C_s-o(C_s)\) parent-aligned roots. The packets overlap and are not
automatically negative subpackets of the canonical \(F_s\).

The unrestricted five-input skeleton hypergraph has bounded average degree
\(35/8+o(1)\). This proves neither a near-perfect matching nor an
obstruction to one. More importantly, its generic early-slot edges lack
the common physical injection needed to inherit the finite \(D_4\)
ledgers.

Hence the bounded-seed escape is closed in its proposed form. A surviving
early-slot construction must use row-dependent global paths and prove the
complete \(X/Y\) ledgers afresh; it is already a genuinely growing
construction.

For that pivot, Sections 7--8 give an exact first-column completion
criterion and a universal invariant. Every growing \(D_s\)-port factor has
exactly \(C_{s-1}\) rows which insert coordinate \(2s\) first and delete
coordinate \(1\) last. If \(C_s\ge4p\), then \(C_{s-1}>p\), so no fully
balanced first-insertion histogram below cap \(p\) exists. The remaining
possible goal is the weaker one of splitting every canonical first-return
fibre while accepting this forced global endpoint load.

## 1. Operadic slots and their physical positions

Encode a full ordered binary tree \(T\) by its prefix word

\[
                         \widehat w(T)\in\{1,0\}^{2|T|+1},              \tag{1.1}
\]

where internal nodes are \(1\)'s and leaves are \(0\)'s. Deleting the last
zero gives the usual Dyck word.

Operadic substitution replaces zero \(i+1\) of \(\widehat w(P)\) by
\(\widehat w(A_i)\). Therefore

\[
                         |P[\mathbf A]|
                           =4+\sum_{i=0}^4|A_i|,                        \tag{1.2}
\]

independently of \(P\). Collapsing the marked spectators back to leaves
recovers \(P\), proving distinctness.

Let \(\lambda_i(P)\) be the position of leaf \(i\), numbered from zero, in
the nine-letter word \(\widehat w(P)\). The audited table is

\[
\begin{array}{c|c}
i&\{\lambda_i(P):P\in D_4\}\\ \hline
0&\{2,3,4,5\}\\
1&\{4,5,6\}\\
2&\{6,7\}\\
3&\{8\}\\
4&\{9\}.
\end{array}                                             \tag{1.3}
\]

If \(n_i=|A_i|\), earlier expansions add
\(2\sum_{k<i}n_k\) symbols, so the first physical coordinate of \(A_i\)
occurs at

\[
                         \lambda_i(P)+2\sum_{k<i}n_k.                  \tag{1.4}
\]

It is independent of \(P\) only in slots \(3,4\).

### Corollary 1.1 (common-cylinder restriction)

Under the token-preserving interface of the existing context theorem, a
common \(D_4\)-port cylinder may have nonempty spectators only in slots
\(3,4\).

#### Proof

That interface requires one row-independent injection of the eight local
coordinates and one fixed exterior spectator state. Every token belonging
to a fixed spectator must therefore keep its physical label in all
fourteen rows. Equation (1.4) rules this out in slots \(0,1,2\).
\(\square\)

This conclusion is deliberately about the literal spectator-preserving
interface. It does not rule out a new row-dependent reclassification of
all coordinates.

## 2. A port counterexample at \(s=5\)

Put the one-node spectator \(10\) in slot \(1\) and leave all other slots
empty. Four expanded roots have up-step sets

\[
\begin{array}{c|c}
P&\text{up-step positions of }P[\mathbf A]\\ \hline
1234&\{1,2,3,4,6\}\\
1357&\{1,3,4,7,9\}\\
1245&\{1,2,4,5,6\}\\
1236&\{1,2,3,5,8\}.
\end{array}                                             \tag{2.1}
\]

Their intersection is \(\{1\}\), and their union is
\(\{1,\ldots,9\}\). Every expanded Dyck root contains coordinate \(1\)
and excludes coordinate \(10\). Thus the full fourteen-root family has
exactly one constantly selected and one constantly unselected coordinate.

### Proposition 2.1 (no common affine face)

This slot-\(1\) family is not a common \(D_4\)-port cylinder, even after a
common coordinate permutation.

#### Proof

A semilength-five cylinder obtained from a \(D_4\) face and one fixed
spectator node has roots

\[
                         O^+\cup\iota(P),\qquad P\in D_4,               \tag{2.2}
\]

with one common injection \(\iota:[8]\hookrightarrow[10]\).
The \(D_4\) ports have one constantly selected and one constantly
unselected local coordinate. The fixed spectator contributes one more of
each, so (2.2) has two constant columns of each type. This contradicts
the census above. \(\square\)

The obstruction is already present at the endpoint ports.

## 3. Natural statewise expansion fails a Johnson edge

For a balanced four-set word \(x\), define the natural zero-slot expansion
\(\mathsf E_{\mathbf A}(x)\) by inserting \(w(A_i)\) immediately before
zero \(i+1\), for \(0\le i\le3\), and appending \(w(A_4)\).

For a Dyck port this is its operadic substitution. On non-Dyck
intermediate states it is the canonical natural extension considered
here; uniqueness among all row-dependent extensions is not asserted.

The first row of \(G_4\) begins

\[
                         x=11110000
                 \longrightarrow x'=11100001.                          \tag{3.1}
\]

Their expansions are

\[
\begin{aligned}
\mathsf E_{\mathbf A}(x)
 &=1111\,A_0\,0\,A_1\,0\,A_2\,0\,A_3\,0\,A_4,\\
\mathsf E_{\mathbf A}(x')
 &=111\,A_0\,0\,A_1\,0\,A_2\,0\,A_3\,0\,1\,A_4.
\end{aligned}                                           \tag{3.2}
\]

Put

\[
                         M=A_0\,0\,A_1\,0\,A_2\,0\,A_3\,0.             \tag{3.3}
\]

After deleting their common prefix \(111\) and suffix \(A_4\), the words
are \(1M\) and \(M1\). Their Hamming distance is the number of bit changes
in

\[
                         1,m_1,\ldots,m_{|M|},1.                        \tag{3.4}
\]

### Lemma 3.1 (first-edge restriction)

If at least one of \(A_1,A_2,A_3\) is nonempty, the two words in (3.2)
have Hamming distance at least four and Johnson distance at least two.

#### Proof

Every nonempty Dyck spectator starts with \(1\) and ends with \(0\).
Immediately before each of \(A_1,A_2,A_3\) is a separator \(0\), so a
nonempty one creates a \(0\to1\) change inside \(M\). The final displayed
zero of \(M\), followed by the terminal \(1\) in (3.4), creates another.
A binary string beginning and ending with \(1\) has equally many
\(1\to0\) and \(0\to1\) changes. Hence there are at least four.
For equal-weight words, Johnson distance is half Hamming distance.
\(\square\)

For the tuple of Section 2,

\[
 \mathsf E_{\mathbf A}(x)=1111010000,\qquad
 \mathsf E_{\mathbf A}(x')=1110100001,                  \tag{3.5}
\]

whose five-sets intersect in three coordinates. Their union has size
seven instead of six, so the corresponding \(Y\)-colour is illegal too.

Thus natural first-edge legality requires (0.4). This is a necessary
condition only.

## 4. Exact terminal-slot product bitrades

The natural expansion is not the only possible routing. Let
\(B=B_0,\ldots,B_b=\overline B\) and
\(C=C_0,\ldots,C_c=\overline C\) be fixed complement geodesics on two
disjoint spectator grounds. Let

\[
 X_0^G(P),X_1^G(P),\ldots,X_4^G(P)=\overline P         \tag{4.1}
\]

be the row rooted at \(P\) in either anchored \(D_4\)-factor
\(G\in\{F_4,G_4\}\).

For the terminal-slot operadic port, define the global row

\[
\begin{array}{ll}
X_t^G(P)\cup B\cup C,&0\le t\le4,\\
\overline P\cup B_k\cup C,&1\le k\le b,\\
\overline P\cup\overline B\cup C_\ell,&1\le\ell\le c.
\end{array}                                             \tag{4.2}
\]

### Theorem 4.1 (terminal product interface)

For every ordered spectator pair \((B,C)\), the rows (4.2) built from
\(F_4\) and from \(G_4\) form an endpoint-preserving fourteen-for-fourteen
bitrade with identical complete \(X\)-state and \(Y\)-colour ledgers.

#### Proof

The start of (4.2) is the common-cylinder interpretation of the terminal
operadic port

\[
                         p_1\cdots p_7\,w(B)\,0\,w(C),                  \tag{4.3}
\]

and the end is its literal complement
\(\overline P\cup\overline B\cup\overline C\).
Every consecutive pair changes one coordinate, so each row is a
complement geodesic.

During the first segment, the small \(F_4\) and \(G_4\) factors have equal
\(X/Y\) ledgers, pushed through one common affine embedding with fixed
spectators \(B,C\). Every later state and colour is identical row by row
on the two sides. The join from the local segment to the \(B\)-segment
depends only on the common local endpoint \(\overline P\); the second join
depends only on \(\overline P,\overline B\). Hence the complete ledgers
agree. \(\square\)

This theorem gives actual local bitrades, but not their occurrence as
negative packets inside the canonical \(F_s\), nor simultaneous
compatibility of overlapping spectator pairs in one ambient factor.

## 5. Coverage ceilings

The natural common-port lift satisfies both (0.3) and (0.4), so only
\(A_4\) remains. There are \(C_{s-4}\) choices and at most

\[
                         14C_{s-4}
        =\left(\frac7{128}+o(1)\right)C_s               \tag{5.1}
\]

root incidences.

For the collectively rerouted terminal cylinders of Theorem 4.1, the
ordered spectator pair has total size \(s-4\). Therefore

\[
                         [z^{s-4}]C(z)^2=C_{s-3}        \tag{5.2}
\]

candidate bitrades, with incidence at most

\[
                         14C_{s-3}
        =\left(\frac7{32}+o(1)\right)C_s.               \tag{5.3}
\]

This already rules out a near-complete parent-aligned packetization by
the entire literal common-cylinder family, even if every candidate could
be selected without overlap.

The same Catalan count occurs if one ignores the common-port condition and
keeps only the first-edge condition (0.4), which leaves \(A_0,A_4\).
These are different families; equality of their counts must not be used
to identify them.

## 6. The unrestricted skeleton hypergraph

The number of ordered five-spectator tuples of total size \(s-4\) is

\[
 E_s=[z^{s-4}]C(z)^5
      =\frac5{2s-3}\binom{2s-3}{s-4}.                  \tag{6.1}
\]

They define a fourteen-uniform tuple-indexed hypergraph on \(D_s\).
Its exact average representation degree is

\[
 \frac{14E_s}{C_s}
   =\frac{35(s-2)(s-3)}
          {2(2s-1)(2s-3)}
       \longrightarrow\frac{35}{8}.                    \tag{6.2}
\]

For a fixed skeleton shape, a tree determines its five hanging
spectators uniquely if that decomposition exists. Hence every vertex has
degree at most fourteen.

The edges overlap. Bounded average and maximum degree do not imply an
almost-perfect matching. Conversely they do not rule one out. Even an
abstract almost-perfect matching would not inherit the \(F_4/G_4\) ledgers
on generic early-slot tuples.

## 7. Exact completion criterion for a growing \(D_s\) factor

Let

\[
 \mathcal X=\binom{[2s]}s,\qquad
 \mathcal Y=\binom{[2s]}{s+1},\qquad
 D=D_s,\qquad\overline D=\{[2s]\setminus P:P\in D\},    \tag{7.1}
\]

and put

\[
                         U=\mathcal X\setminus\overline D,\qquad
                         V=\mathcal X\setminus D.                       \tag{7.2}
\]

Prescribe full first columns

\[
                         P\subset Y_P\supset Q_P,
                                  \qquad P\in D,                        \tag{7.3}
\]

with distinct \(Y_P\)'s and distinct \(Q_P\in V\). Let
\(\mathcal Y_0=\{Y_P\}\), \(\mathcal Q_0=\{Q_P\}\).

### Theorem 7.1 (Hall plus marked monodromy)

The prescribed arcs extend to the two ownership matchings

\[
 M^\uparrow:U\longleftrightarrow\mathcal Y,\qquad
 M^\downarrow:\mathcal Y\longleftrightarrow V                         \tag{7.4}
\]

if and only if

\[
 |N(A)\setminus\mathcal Y_0|\ge|A|
       \quad(A\subseteq U\setminus D),                                 \tag{7.5}
\]

and

\[
 |N(B)\setminus\mathcal Q_0|\ge|B|
       \quad(B\subseteq\mathcal Y\setminus\mathcal Y_0).                \tag{7.6}
\]

For any such extensions, set

\[
                         T=M^\downarrow\circ M^\uparrow:U\to V         \tag{7.7}
\]

and close it to a permutation of \(\mathcal X\) by

\[
                         \widehat T(\overline P)=P,
                                      \qquad P\in D.                    \tag{7.8}
\]

The matchings form a \(D_s\)-port complement-path factor if and only if
every cycle of \(\widehat T\) contains exactly one marked closure arrow
\(\overline P\to P\).

#### Proof

After fixing (7.3), (7.5)--(7.6) are precisely Hall's conditions for the
two residual bipartite matchings.

The union of the matchings alternates through \(X\)- and \(Y\)-states.
Its directed successor on \(X\) is \(T\). Adding (7.8) closes every desired
path. A cycle with no marked arrow is an unwanted alternating cycle; a
cycle with two marked arrows joins two port pairs. Exactly one marked
arrow gives a path from \(P\) to \(\overline P\).

There are \(C_s\) marked arrows. Every path from an \(s\)-set to its
complement has Johnson length at least \(s\), while

\[
                         |U|=\binom{2s}s-C_s=sC_s.                     \tag{7.9}
\]

Thus all \(C_s\) paths have exactly \(s\) successor arcs and are
complement geodesics. \(\square\)

Relative to a canonical factor, the two matching symmetric differences
are disjoint unions of even alternating cycles. A legal growing factor is
therefore a coordinated pair of alternating-cycle systems satisfying the
marked-cycle condition. Hall alone is insufficient.

A necessary sign check is: if the upward cycles have lengths \(2k_C\) and
the downward cycles lengths \(2\ell_D\), then

\[
                 \sum_C(k_C-1)\equiv
                 \sum_D(\ell_D-1)\pmod2.               \tag{7.10}
\]

Every valid closed successor has cycle type \((s+1)^{C_s}\), hence the
same sign as the canonical one.

A literal first-return rotation \(P\to P'\) cannot itself be the first
successor in (7.3): \(P'\in D\), whereas every noninitial \(X\)-state lies
in \(V=\mathcal X\setminus D\). Abstract rotation-graph connectivity proves
none of Hall, colour ownership, or marked monodromy. Auxiliary non-Dyck
states are essential.

## 8. Universal endpoint first-insertion invariant

In one row

\[
                         P=X_0,X_1,\ldots,X_s=\overline P,              \tag{8.1}
\]

let \(a(P)\) be the transition at which coordinate \(1\) is deleted and
\(b(P)\) the transition at which coordinate \(2s\) is inserted.
Every Dyck port contains \(1\) and excludes \(2s\).

The number of \(X\)-states in the row containing both endpoint coordinates
is

\[
                              (a(P)-b(P))_+.            \tag{8.2}
\]

The number of adjacent-union \(Y\)-states containing both is larger by
one exactly when \(b(P)\le a(P)\).

### Theorem 8.1 (forced endpoint rows)

Every exact \(D_s\)-port factor has exactly \(C_{s-1}\) rows satisfying

\[
                         b(P)=1,\qquad a(P)=s.           \tag{8.3}
\]

Equivalently, exactly \(C_{s-1}\) rows insert coordinate \(2s\) first and
delete coordinate \(1\) last.

#### Proof

Exact \(X\)-ownership gives

\[
 \sum_{P\in D}(a(P)-b(P))_+
   =\binom{2s-2}{s-2}=(s-1)C_{s-1}.                    \tag{8.4}
\]

Subtracting the \(X\)-containment count from the exact \(Y\)-containment
count gives

\[
\begin{aligned}
\#\{P:b(P)\le a(P)\}
 &=\binom{2s-2}{s-1}-\binom{2s-2}{s-2}\\
 &=C_{s-1}.                                            \tag{8.5}
\end{aligned}
\]

Every positive summand in (8.4) is at most \(s-1\), and only a row counted
in (8.5) can contribute. The right side of (8.4) is the maximum possible
total \(C_{s-1}(s-1)\). Thus every counted row has
\(a(P)-b(P)=s-1\), forcing (8.3). \(\square\)

### Corollary 8.2 (full first-insertion balance is impossible)

If \(C_s\ge4p\), every exact \(D_s\)-port factor has

\[
 h(2s)=C_{s-1}
   =\frac{s+1}{2(2s-1)}C_s>\frac14C_s\ge p.            \tag{8.6}
\]

No growing factor can put every first-insertion target below cap \(p\).

The theorem does not identify which canonical first-return fibres supply
these forced rows. The \(D_4\) factor shows that they can move between
fibres. Hence the weaker requirement

\[
 \#\{P\in\mathcal F_{s,j}:b_1(P)=x\}\le p
       \quad\text{for every canonical first-return fibre }
       \mathcal F_{s,j}\text{ and every }x              \tag{8.7}
\]

is not ruled out. Conditions (7.5)--(7.8), together with (8.7), are the
exact surviving root-scale construction problem.

## 9. Proved boundary

Proved:

1. Abstractly, all fourteen bracketings retain five ordered spectators.
2. The first three physical slots move and do not supply the literal
   common port interface.
3. The natural \(G_4\) first edge fails whenever one of
   \(A_1,A_2,A_3\) is nonempty.
4. Natural common-port suspension reduces to the right suffix and has
   incidence at most \((7/128+o(1))C_s\).
5. A collective product routing makes every terminal-slot pair into a
   genuine fourteen-row \(X/Y\) bitrade, but their total incidence is at
   most \((7/32+o(1))C_s\).
6. Neither the terminal family nor the unrestricted bounded-degree
   skeleton hypergraph supplies a near-complete embedded packet bank.
7. A growing factor must satisfy the Hall and marked-monodromy theorem.
8. The forced endpoint load \(C_{s-1}\) rules out fully balanced
   first-insertion targets at the fatal cap.

Not ruled out:

* a row-dependent early-slot fourteen-row bitrade;
* embedding a large disjoint subfamily of terminal product bitrades in one
  noncanonical ambient factor;
* auxiliary packets whose row support grows with \(s\);
* a genuinely growing \(D_s\)-port factor satisfying the per-fibre
  condition (8.7).

Each surviving option requires a new complete \(X/Y\) construction and
does not inherit exactness from the finite \(D_4\) certificate.

