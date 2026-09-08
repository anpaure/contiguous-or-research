# The globally shifted \(B+2\) hinge: exact endpoint obstruction and a one-coordinate core-swap repair

**Date:** 2026-08-07  
**Status:** unconditional local theorem and exact global scope boundary.
The proposed width-\((d+2)\) hinge has the desired flag, owner, immediate
lower, and immediate upper values, but its unpunctured terminal letter
makes the next owner window unusable.  Replacing that one terminal letter
by a one-coordinate puncture removes the owner obstruction and realizes
the hinge as an exact transition between two Johnson-adjacent shared rail
cores.  The puncture has one exact cost: it destroys the separate
authoritative PBBS successor-coatom suffix.  Thus the repaired packet has
zero immediate edge-palette sidecars but exports one named
successor-coatom/compiler ticket.  One transition is length-neutral inside
an ambient word.  A positive-density family still requires a theorem
allowing the \((d+3)\)-position transition supports and the exported
tickets to be handled consistently.

## 1. Parameters and the proposed shifted hinge

Put

\[
 L=d+2.
\tag{1.1}
\]

Assume \(d\ge2\) and \(m\ge2d+2\).  Choose pairwise disjoint sets and
labels

\[
 K,\ C,\ A=\{a_0,a_1,\ldots,a_{d-1}\},
 \quad u,\ b^-,\ b,
\tag{1.2}
\]

with

\[
 |C|=d,\qquad |K|=m-2d-2.
\tag{1.3}
\]

Define

\[
 M=K\mathbin{\dot\cup}A,\qquad
 R=M\mathbin{\dot\cup}C,\qquad
 I=R\mathbin{\dot\cup}\{u\},
 \qquad
 Y_{\rm forced}=R\mathbin{\dot\cup}\{b\}.
\tag{1.4}
\]

Then

\[
 |M|=m-d-2,\qquad |R|=m-2,\qquad
 |I|=|Y_{\rm forced}|=m-1.
\tag{1.5}
\]

Index a source segment by \(0,\ldots,L\).  The originally proposed
unpunctured letters are

\[
\begin{aligned}
 X_0&=C+b^-,\\
 X_1&=C+a_0,\\
 X_2&=K+a_0+u,\\
 X_{i+2}&=K+a_0+a_i
       &&(1\le i\le d-1),\\
 X_L&=C+b.
\end{aligned}
\tag{1.6}
\]

There are \(L+1=d+3\) positions.

## 2. Every advertised local row is correct

### Proposition 2.1 (literal suffix, owner, q1, and upper rows)

For (1.6),

\[
\begin{aligned}
 \bigcup_{t=3}^{L-1}X_t&=M,\\
 \bigcup_{t=2}^{L-1}X_t&=M+u,\\
 \bigcup_{t=1}^{L-1}X_t&=I,\\
 \bigcup_{t=3}^{L}X_t&=Y_{\rm forced},
\end{aligned}
\tag{2.1}
\]

and

\[
\begin{aligned}
 \bigcup_{t=0}^{L-1}X_t&=I+b^-,\\
 \bigcup_{t=1}^{L}X_t&=I+b,\\
 \bigcup_{t=0}^{L}X_t&=I+b^-+b.
\end{aligned}
\tag{2.2}
\]

Thus the two consecutive length-\(L\) windows are distinct rank-\(m\)
Johnson neighbours, their native shared length-\((L-1)\) source window
has value \(I\) of rank \(m-1\), and their length-\((L+1)\) span is the
rank-\((m+1)\) union colour.  The final length-\(d\) suffix is the
separate forced coatom \(Y_{\rm forced}=R+b\).

#### Proof

The letters \(X_3,\ldots,X_{L-1}\) contain \(K+a_0\) and, once each,
all of \(a_1,\ldots,a_{d-1}\), proving the first identity in (2.1).
Adding \(X_2\) adds \(u\), and adding \(X_1\) adds \(C\).  Appending the
unpunctured \(X_L=C+b\) to the \(M\)-suffix gives
\(Y_{\rm forced}=M+C+b\).  The remaining identities add \(b^-\), \(b\),
or both. \(\square\)

Hence the local rank calculation that motivated the \(B+2\) route is
valid.

## 3. Exact obstruction in the unpunctured segment

The right endpoint is nevertheless frozen.  Namely,

\[
 \bigcup_{t=2}^{L}X_t=I+b.
\tag{3.1}
\]

The letter \(X_1=C+a_0\) is completely redundant in the right owner:
\(C\) is repeated in \(X_L\), and \(a_0\) is repeated in every internal
letter.

### Theorem 3.1 (two-start endpoint-hole obstruction)

For the unpunctured segment, every interval beginning at position \(1\)
or at position \(2\) whose union has rank \(m\) has the same value

\[
 T_+=I+b.
\tag{3.2}
\]

Consequently, suppose a word of length \(W+d+2\) contains \(H\) such
segments with pairwise distinct right-owner targets \(T_+\).  Then

\[
 \boxed{H\le d+2.}
\tag{3.3}
\]

In particular, the unpunctured segment cannot support a
positive-density hinge bank.

#### Proof

For intervals starting at \(1\), the prefix through \(L-1\) has value
\(I\) and rank \(m-1\); adjoining \(X_L\) first reaches rank \(m\), with
value \(T_+\).  Longer prefixes either retain that value or have rank
greater than \(m\).

For intervals starting at \(2\), the prefix through \(L-1\) has value
\(M+u\), of rank \(m-d-1\).  Adjoining \(X_L\) first reaches rank \(m\),
again with value \(T_+\), by (3.1).  Monotonicity gives the same
conclusion for longer prefixes.

Choose one witnessing interval for each of the \(W\) distinct rank-\(m\)
targets in the full word.  Equal-rank distinct targets are incomparable,
so the chosen intervals have pairwise distinct left endpoints.  For one
hinge, the two starts \(1,2\) can support only its single target \(T_+\);
at most one can be selected.  Start pairs belonging to hinges with
different \(T_+\)-values are disjoint: a common start would, by the
previous paragraph, force the two \(T_+\)-values to agree.  Hence every
hinge forces at least one unused left endpoint.  A length-\((W+d+2)\)
word has only \(d+2\) left endpoints outside the selected \(W\), proving
(3.3). \(\square\)

This obstruction is independent of any run/gap or upper-palette issue.

## 4. The one-coordinate puncture

Choose

\[
 z\in C.
\tag{4.1}
\]

Retain \(X_0,\ldots,X_{L-1}\) from (1.6), but replace the terminal letter
by

\[
 \boxed{X_L=(C-\{z\})+b.}
\tag{4.2}
\]

Define two rail cores

\[
 G=K\mathbin{\dot\cup}C,
 \qquad
 G'=(G-\{z\})\mathbin{\dot\cup}\{a_0\}.
\tag{4.3}
\]

They have the same rank

\[
 |G|=|G'|=m-L
\tag{4.4}
\]

and form a directed Johnson core swap

\[
 \boxed{G\longrightarrow G'=G-z+a_0.}
\tag{4.5}
\]

## 5. Exact left- and right-rail normal forms

Let \((\alpha_t)\) be an old toggle stream on the left, with

\[
 \alpha_0,\ldots,\alpha_{L-1}
 =
 b^-,a_0,u,a_1,\ldots,a_{d-1}.
\tag{5.1}
\]

At ordinary left positions put

\[
 X_t=G+\alpha_t.
\tag{5.2}
\]

Let \((\beta_t)\) be a new toggle stream on the right, with

\[
 \beta_1,\ldots,\beta_L
 =
 z,u,a_1,\ldots,a_{d-1},b,
\tag{5.3}
\]

and at ordinary positions \(t>L\) put

\[
 X_t=G'+\beta_t.
\tag{5.4}
\]

At positions \(0,\ldots,L\), use the punctured exceptional letters
(1.6), (4.2).

### Theorem 5.1 (core-swap window identity)

Every length-\(L\) source window satisfies

\[
 \boxed{
 \bigcup_{t=s}^{s+L-1}X_t
 =
 \begin{cases}
 G\cup\{\alpha_s,\ldots,\alpha_{s+L-1}\},
       &s\le0,\\[2mm]
 G'\cup\{\beta_s,\ldots,\beta_{s+L-1}\},
       &s\ge1.
 \end{cases}}
\tag{5.5}
\]

This holds for every window meeting the splice, not merely the two central
windows.

#### Proof

If \(s<0\), the window contains an ordinary full-\(G\) letter.  If
\(s=0\), the \(C\)-letters and the \(K\)-letters together supply \(G\).
The only repeated old toggle is \(a_0\); every old window containing one
of its internal repetitions also contains its designated position \(1\).
Thus no extra old toggle is introduced.

If \(s=1\), the exceptional letters supply \(K\), \(C-\{z\}\), and
\(a_0\), hence all of \(G'\).  If \(s\ge2\), the window contains an
ordinary full-\(G'\) letter.  Relative to \(G'\), the labels in positions
\(1,\ldots,L\) outside the core are exactly
\(z,u,a_1,\ldots,a_{d-1},b\).  The repetitions of \(a_0\) now lie in the
new core and introduce no extra toggle.  This proves (5.5). \(\square\)

### Corollary 5.2 (flat Johnson owners)

If every relevant length-\((L+1)\) toggle block has distinct labels, then
all values in (5.5) have rank \(m\), and consecutive values are distinct
Johnson neighbours.  (Equivalently, each length-\(L\) block is simple and
its outgoing and incoming toggles differ.)  The only transition at which
the core description changes is

\[
\begin{aligned}
 T_-&=I+b^-
     =G+\{b^-,a_0,u,a_1,\ldots,a_{d-1}\},\\
 T_+&=I+b\\
     &=G'+\{z,u,a_1,\ldots,a_{d-1},b\},
\end{aligned}
\tag{5.6}
\]

and it deletes \(b^-\) and inserts \(b\).

The next owner is no longer frozen.  If
\(\beta_{L+1}=w\), then

\[
 T_2
 =G'+\{u,a_1,\ldots,a_{d-1},b,w\}
 =T_+-z+w.
\tag{5.7}
\]

Thus the puncture changes the former repeated transition into the Johnson
step \(z\mapsto w\).

## 6. Exact immediate rows and the forced-coatom cost

The first three suffix identities in (2.1) do not use \(X_L\), so they
survive unchanged:

\[
 M,\qquad U=M+u,\qquad I=M+C+u
\tag{6.1}
\]

are literal consecutive suffix values.

Across the core swap,

\[
\begin{aligned}
 T_-\cap T_+&=I
              =\bigcup_{t=1}^{L-1}X_t,\\
 T_-\cup T_+&=I+b^-+b
              =\bigcup_{t=0}^{L}X_t.
\end{aligned}
\tag{6.2}
\]

The next lower overlap is also literal:

\[
 T_+\cap T_2
 =I-z+b
 =\bigcup_{t=2}^{L}X_t.
\tag{6.3}
\]

Away from the core swap, (5.5) gives the ordinary rail formulas

\[
\begin{aligned}
 T_s\cap T_{s+1}
 &=G_\star+\{\text{the shared \(L-1\) toggles}\},\\
 T_s\cup T_{s+1}
 &=G_\star+\{\text{the \(L+1\) consecutive toggles}\},
\end{aligned}
\tag{6.4}
\]

where \(G_\star\) is \(G\) or \(G'\).  Both are native source intervals.
Hence the splice creates

\[
 \boxed{\text{zero local lower-q1 sidecars and zero local upper sidecars}.}
\tag{6.5}
\]

Global palette injectivity still requires the usual distinctness of all
named toggle-window values across different splices.

The authoritative PBBS successor coatom is not \(I\).  It is

\[
 \boxed{
 Y_{\rm forced}=M+C+b=T_+-u.}
\tag{6.6}
\]

Before puncturing, it was the literal final length-\(d\) suffix
\(\bigcup_{t=3}^{L}X_t\).  After (4.2), that same suffix is

\[
 \boxed{
 \bigcup_{t=3}^{L}X_t
 =M+(C-\{z\})+b
 =Y_{\rm forced}-\{z\},}
\tag{6.7}
\]

of rank \(m-2\).  No later cell in the displayed splice has been proved to
supply \(Y_{\rm forced}\).  Therefore the proof-safe local ledger is

\[
 \boxed{
 \text{zero immediate edge-palette sidecars,
 but one exported forced-coatom/compiler ticket }Y_{\rm forced}.}
\tag{6.8}
\]

The core-swap repair is consequently not, by itself, a complete PBBS
promotion ticket.

## 7. Coordinate residence

Assume every noncore toggle occurrence is separated from its next
occurrence in the corresponding stream by at least \(2L\) source
positions.

Every ordinary toggle then has one owner run of length \(L\) and an owner
gap of length at least \(L\).  Coordinates in

\[
 G\cap G'=G-\{z\}
\tag{7.1}
\]

are permanent through the splice.

The entering core coordinate \(a_0\) appears first as the old toggle at
position \(1\).  That occurrence places it in the \(L\) owners ending at
start \(1\), and from start \(1\) onward it belongs to \(G'\).  Its
positive run is therefore continuous and has length at least \(L\); its
preceding gap is protected by the old toggle spacing.

The departing core coordinate \(z\) belongs to \(G\) through start \(0\)
and occurs as the new toggle \(\beta_1=z\) at position \(1\).  It is
therefore present continuously through owner start \(1\), and absent from
start \(2\) onward.  If its next new-stream occurrence is at least \(2L\)
positions after position \(1\), its negative owner gap has length at least
\(L\); that next singleton occurrence then gives a positive run of length
\(L\).

### Theorem 7.1 (biresident core-swap splice)

Under the \(2L\)-spacing hypothesis, the punctured segment and the two
ambient rails satisfy the run/gap residence floor \(L\) for every
coordinate.  Thus (4.5) is a literal resident transition, not merely an
owner-set identity.

## 8. The core-swap transition graph

Ignoring the auxiliary ticket labels, the local transition graph has

\[
 \mathcal G_L=\binom{[n]}{m-L}
\tag{8.1}
\]

as its vertex set and a directed arc

\[
 G\longrightarrow G-z+a
\tag{8.2}
\]

for every \(z\in G\) and \(a\notin G\).  Hence its underlying graph is
the Johnson graph

\[
 J(n,m-L).
\tag{8.3}
\]

To realize a directed arc, set \(a_0=a\), choose a \(d\)-set
\(C\subseteq G\) containing \(z\), put \(K=G\setminus C\), and choose
the remaining labels

\[
 a_1,\ldots,a_{d-1},u,b^-,b
\tag{8.4}
\]

outside \(G+a_0\).  The available-label count is ample in the stated
range.  Additional owner, palette, flag-target, and compiler tickets
restrict this ideal Johnson graph but do not change the local normal form.

## 9. Exact global scope

One core-swap splice is **length-neutral**: it replaces \(L+1=d+3\)
source letters inside one ambient word and inserts no new position.  A
finite sequence of pairwise compatible splices therefore still lives in
one word of the globally chosen length \(W+d+2\); there is no formal
start/end position appended for each splice.

This statement must not be confused with a positive-density packing
theorem.  The proved template prescribes an \(L+1\)-position support.  If
splices are required to be disjoint, it yields only \(O(W/L)\) of them.
Obtaining \(H=\Theta(W)\) transitions requires overlapping/interlaced
supports whose prescriptions agree on every shared source position.
Equivalently, one needs a dynamic-core trace

\[
 G_0\to G_1\to\cdots
\tag{9.1}
\]

in \(J(n,m-L)\), together with occurrence labels, such that:

1. every required local block is the punctured pattern above;
2. overlapping blocks prescribe the same literal source letters;
3. toggle reuse and every core entry/exit obey the \(2L\) residence
   spacing;
4. all owner, q1, upper, and compiler values remain globally admissible,
   including a simultaneous realization of every exported
   \(Y_{\rm forced}\) ticket.

No per-splice *length charge* appears if such an interlacing exists, but
the present local theorem does not prove that it exists.  This
overlap-consistency problem is the exact remaining mass-scale gate for the
shifted \(B+2\) route.

## 10. Conclusion

The unpunctured shifted hinge is locally attractive but globally
mass-dead:

\[
 H\le d+2.
\]

The one-coordinate puncture (4.2) removes that endpoint hole and yields an
exact, resident, zero-immediate-edge-sidecar Johnson core swap

\[
 \boxed{G\to G-z+a_0.}
\]

The additive-\(2\) route is therefore not blocked at the owner, immediate
q1, upper, or residence rows.  Its remaining problem is a
positive-density compatible walk of these core swaps in one literal source
chronology together with a common compiler realization of the exported
forced successor coatoms \(Y_{\rm forced}\).
