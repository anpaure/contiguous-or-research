# Gate C correction: reverse first-UHD two-seam hybrids are not phase packets

**Status (2026-08-23).** The proposed reverse asymmetric splice has an
excellent abstract occurrence ledger: after matching almost all Catalan
roots, it creates only one duplicate and one hole per matched pair. It does
**not**, however, create phase packets. Each output flips its repeated
coordinate on two consecutive transitions and contains a Johnson triangle.
A phase-packet support has distance-one graph equal to a simple path, so no
reordering repairs the defect.

Thus the splice gives \(C_b-o(C_b)\) legal Johnson paths with \(o(W)\)
middle collisions and holes, not \(C_b-o(C_b)\) phase packets. It does not
close the middle-packet part of Gate \(C_{\rm Q}\). Section 5 proves the
still-valid collision-tolerant direct-hole compiler and records exactly why
it cannot be applied here.

## 1. Canonical paths and phase packets

Let \(b\ge4\), \(\Omega=[2b]\), and

\[
 C_b={1\over b+1}{2b\choose b},\qquad
 W={2b\choose b}=(b+1)C_b.                         \tag{1.1}
\]

A Dyck root is a balanced bit word \(w\) of length \(2b\) whose prefix
heights are nonnegative. If \(w=1\alpha0\beta\) at its first return, put
\(d=|\alpha|+2\), let \(\mu\) be reverse-complement, and define

\[
 \rho(\varnothing)=(),\qquad
 \rho(w)=(d,\ d-\rho(\mu\alpha),\ 1,\ d+\rho(\beta)). \tag{1.2}
\]

Arithmetic in (1.2) is entrywise. The list \(\rho(w)\) is a permutation
of \([2b]\); its odd entries are zero positions of \(w\), and its even
entries are one positions. Toggle its first \(2t\) entries and call the
resulting \(b\)-set \(F_t(w)\), \(0\le t\le b\). The transition
\(F_{t-1}(w)\to F_t(w)\) adds \(\rho_{2t-1}(w)\) and removes
\(\rho_{2t}(w)\).

The recursive Chung--Feller inverse to (1.2) gives a bijection

\[
 (w,t)\longmapsto F_t(w):
 \mathcal D_b\times\{0,\ldots,b\}\longrightarrow{[2b]\choose b}.
                                                               \tag{1.3}
\]

For reference, classify a balanced word by the number \(t\) of up-steps
starting below height zero. Recursion at the first return sends \(F_t(w)\)
to that class and gives a unique inverse: cut off the initial negative
primitive component if the word starts with zero, and otherwise cut at the
last up-step from height \(-1\) to zero. Each recursive call has smaller
semilength. Hence every class has \(C_b\) elements, proving (1.3). In
particular, all canonical path occurrences \(F_t(w)\) are globally
distinct.

A labelled phase packet is determined by distinct \(a,z\in\Omega\) and
ordered tuples

\[
 X=(x_1,\ldots,x_{b-1}),\qquad
 Y=(y_1,\ldots,y_{b-1})                              \tag{1.4}
\]

partitioning \(\Omega-\{a,z\}\). Its middle targets are

\[
 \begin{aligned}
 D_0&=\{a\}\cup X,\\
 D_i&=\{x_i,\ldots,x_{b-1}\}\cup\{y_1,\ldots,y_i\}
       &&(1\le i\le b-1),\\
 D_b&=\{a\}\cup Y.
 \end{aligned}                                      \tag{1.5}
\]

The pivot \(a\) is removed on the first transition and restored on the
last. Every other non-omitted coordinate is flipped once.

### Lemma 1.1 (phase-packet support graph)

For \(b\ge3\), the graph on the \(b+1\) targets in (1.5), joining two sets
at Johnson distance one, is exactly

\[
                         D_0-D_1-\cdots-D_b.          \tag{1.6}
\]

#### Proof

For \(1\le i<j\le b-1\), the distance between \(D_i,D_j\) is \(j-i\).
For \(1\le j\le b-1\), the distance between \(D_0,D_j\) is \(j\), and
for \(1\le i\le b-1\), the distance between \(D_i,D_b\) is \(b-i\).
Finally \(D_0,D_b\) have distance \(b-1>1\). Hence precisely consecutive
indices have distance one. \(\square\)

Lemma 1.1 is order-independent: a family containing a Johnson triangle
cannot be the support of a phase packet under any reordering.

## 2. The first-UHD local square

Write a Dyck root uniquely in two-bit macro blocks

\[
 w=1Z_1\cdots Z_{b-1}0,\qquad
 U=11,\quad D=00,\quad A=10,\quad B=01.              \tag{2.1}
\]

Match at the first factor \(UHD\), \(H\in\{A,B\}\), by toggling the colour
of \(H\). Orient a pair as \(P:UAD\), \(Q:UBD\), and let
\(u<v=u+1\) be the two binary coordinates of the toggled horizontal block.

### Lemma 2.1 (exact local-list normal form)

There are distinct \(c,d,u,v\), even-length common lists
\(\Gamma,\Delta\), and

\[
                         s={|\Gamma|\over2}+1         \tag{2.2}
\]

such that

\[
 \boxed{
 \rho(P)=\Gamma,c,u,v,d,\Delta,\qquad
 \rho(Q)=\Gamma,u,d,c,v,\Delta.}                     \tag{2.3}
\]

#### Proof

Here is the recursion-closed induction. Call an \(A\to B\) move two-sided
good if its predecessor, when present, ends in one and its successor, when
present, begins in zero. Prove simultaneously

\[
 \begin{array}{ll}
 \mathsf L:&
 \rho(P)=\Gamma,c,u,v,d,\Delta,\quad
 \rho(Q)=\Gamma,u,d,c,v,\Delta,\quad
 |\Gamma|,|\Delta|\equiv0\pmod2,\\[1mm]
 \mathsf R:&
 \rho(R)=\Gamma',c',y,x,d',\Delta',\quad
 \rho(S)=\Gamma',y,d',c',x,\Delta',\quad
 |\Gamma'|,|\Delta'|\equiv1\pmod2,
 \end{array}                                         \tag{2.4}
\]

where \(\mathsf R\) is the reflected boundary move \(UD\to AA\), with
\(x<y=x+1\).

If the marked move lies after a common first primitive factor \(V\), then

\[
                         \rho(VZ)=\rho(V)\Vert(|V|+\rho(Z))       \tag{2.5}
\]

inserts a common even prefix, so the relevant template is inherited. If
the mark lies inside the first primitive factor \(1\alpha0\), set
\(\delta=|\alpha|+2\) and \(f(j)=\delta-j\). Formula (1.2) prepends
\(\delta\), applies \(f\) entrywise to the reflected child list, and
appends \(1\). It therefore interchanges \(\mathsf L\) and \(\mathsf R\),
preserves the four-entry order in (2.4), and toggles both prefix and suffix
parities. Reverse-complement also sends the neighbouring delimiter bits
\(1,0\) to the boundary blocks \(11,00\), so it interchanges the local
side conditions.

The only case in which an \(A\to B\) move changes the first return is

\[
 P=1C10E0Z,\qquad Q=1C0\,1E0Z                        \tag{2.6}
\]

with \(C,E,Z\) Dyck. Two-sided goodness forces \(C=E=\varnothing\): a
nonempty Dyck word ends in zero and begins in one. Direct substitution in
(1.2) gives

\[
 \rho(1100Z)=(4,2,3,1,4+\rho(Z)),\qquad
 \rho(1010Z)=(2,1,4,3,4+\rho(Z)),                   \tag{2.7}
\]

which is \(\mathsf L\). A boundary \(UD\to AA\) move starts at an odd
coordinate, cannot create a zero-height prefix after its first changed
bit, and returns to the same height after its second, so it cannot split
the first return. These cases exhaust the induction. The middle move in
\(UAD\to UBD\) is two-sided good, proving (2.3). \(\square\)

Put \(P_t=F_t(P)\), \(Q_t=F_t(Q)\). From (2.3), immediately before the
active flips there is a common \((b-2)\)-set \(T\) such that

\[
 \begin{array}{lll}
 P_{s-1}=T\cup\{u,d\},&P_s=T\cup\{c,d\},
   &P_{s+1}=T\cup\{c,v\},\\
 Q_{s-1}=T\cup\{v,d\},&Q_s=T\cup\{u,v\},
   &Q_{s+1}=T\cup\{u,c\}.
 \end{array}                                         \tag{2.8}
\]

## 3. Exact audit of the reverse asymmetric seams

Consider

\[
 \begin{aligned}
 X'&=(Q_0,\ldots,Q_{s-1},P_s,\ldots,P_b),\\
 Y'&=(P_0,\ldots,P_s,Q_{s+1},\ldots,Q_b).
 \end{aligned}                                       \tag{3.1}
\]

### Theorem 3.1 (reverse-splice no-go)

Both sequences in (3.1) are legal Johnson paths, and their transition flip
streams, written as alternating added and removed labels, are

\[
 \boxed{
 \operatorname{flip}(X')=\Gamma,c,v,v,d,\Delta,\qquad
 \operatorname{flip}(Y')=\Gamma,c,u,u,d,\Delta.}     \tag{3.2}
\]

Neither sequence is a phase packet, even after arbitrarily reordering its
targets.

#### Proof

The cross step of \(X'\) is

\[
 Q_{s-1}=T\cup\{v,d\}\longrightarrow P_s=T\cup\{c,d\},           \tag{3.3}
\]

so it adds \(c\) and removes \(v\). Its next canonical \(P\)-step adds
\(v\) and removes \(d\). This proves the first stream in (3.2). Similarly,
\(Y'\) reaches \(P_s\) by the canonical \(P\)-step adding \(c\) and
removing \(u\); its cross step to \(Q_{s+1}\) adds \(u\) and removes \(d\).
This proves the second stream.

Thus the repeated labels \(v,u\) occur on adjacent transitions \(s,s+1\),
whereas a phase-packet pivot is removed on transition \(1\) and restored
on transition \(b\). More invariantly, the three \(X'\)-targets

\[
 T\cup\{v,d\},\qquad T\cup\{c,d\},\qquad T\cup\{c,v\}             \tag{3.4}
\]

are pairwise at Johnson distance one. The three \(Y'\)-targets

\[
 T\cup\{u,d\},\qquad T\cup\{c,d\},\qquad T\cup\{u,c\}             \tag{3.5}
\]

also form a Johnson triangle. Lemma 1.1 rules out a phase-packet ordering
of either support. \(\square\)

The smallest example is \(b=4\):

\[
 \begin{aligned}
 P&=11110000,&\rho(P)&=(8,2,6,4,5,3,7,1),\\
 Q&=11101000,&\rho(Q)&=(8,2,4,3,6,5,7,1).
 \end{aligned}                                       \tag{3.6}
\]

Here \(s=2\), and \(X'\) contains the triangle

\[
 \{1,3,5,8\},\quad\{1,3,6,8\},\quad\{1,5,6,8\}.      \tag{3.7}
\]

## 4. What survives: an \(o(W)\) abstract occurrence ledger

At every phase other than \(s\), the unordered pair in (3.1) is the
canonical pair. At phase \(s\), \(P_s\) occurs twice and \(Q_s\) is absent:

\[
 [X']+[Y']-[P]-[Q]=[P_s]-[Q_s]                      \tag{4.1}
\]

as multisets of middle targets.

Let \(L_b\) be the number of unmatched roots, namely Motzkin excursions of
length \(n=b-1\) avoiding \(UAD,UBD\). If \(n=3q+\ell\),
\(0\le\ell<3\), partitioning into disjoint triples gives

\[
 L_b\le62^q4^\ell\le16\,62^{(b-1)/3}=o(C_b),        \tag{4.2}
\]

because \(62^{1/3}<4\) and \(C_b\sim4^b/(\sqrt\pi b^{3/2})\). Toggling
the first \(UHD\) colour is an involution, so the number of matched pairs is

\[
                         N_b={C_b-L_b\over2}.         \tag{4.3}
\]

Discard the \(L_b\) residual canonical paths and retain both reverse paths
from every matched pair. Since (1.3) makes all canonical occurrences
globally unique, (4.1) gives

\[
 \begin{aligned}
 M_b&=(b+1)(C_b-L_b),\\
 e_b&=N_b,\\
 h_b&=N_b+(b+1)L_b,
 \end{aligned}                                       \tag{4.4}
\]

where \(M_b\) is the number of retained occurrences, \(e_b\) is collision
excess, and \(h_b\) is the number of uncovered middle targets. Therefore

\[
 e_b=O(C_b)=O(W/b)=o(W),\qquad h_b=O(C_b)+o(W)=o(W).  \tag{4.5}
\]

This is a near-perfect abstract middle-occurrence ledger. It is not a
near-perfect phase-packet matching: every retained path violates Theorem
3.1.

## 5. A collision-tolerant direct-hole compiler

The occurrence arithmetic motivates a useful generalization, valid for
genuinely physical fragments. Fix \(H\le b-2\), put \(g=b+H\), and let a
physical \(H\)-fragment be a singleton word with \(L\) consecutive core
starts such that every window of length \(b-H,\ldots,b+H\) at a core start
is present and has pairwise distinct letters. Consider \(t\) such fragments
of core lengths \(L_1,\ldots,L_t\), with no disjointness assumption, and put

\[
                         M=\sum_{j=1}^tL_j.           \tag{5.1}
\]

For each band rank \(r\), let \(\mathscr M_r\) be the multiset of
designated rank-\(r\) targets, let \(\mathcal I_r\) be its support, and set

\[
 h_r={2b\choose r}-|\mathcal I_r|,\qquad
 e_b=\sum_{A\in{\Omega\choose b}}
 [\operatorname{mult}_{\mathscr M_b}(A)-1]_+
 =M-|\mathcal I_b|.                                  \tag{5.2}
\]

### Theorem 5.1 (direct-hole compiler with middle collisions)

Every such physical family satisfies

\[
 \nu(2b)\le
 M+(g-1)t+\sum_{r=b-H}^{b+H}h_r
 +\sum_{\substack{1\le r\le2b\\|r-b|>H}}{2b\choose r}. \tag{5.3}
\]

Equivalently,

\[
 \boxed{
 \nu(2b)\le W+e_b+(g-1)t
 +\sum_{\substack{b-H\le r\le b+H\\r\ne b}}h_r
 +\sum_{\substack{1\le r\le2b\\|r-b|>H}}{2b\choose r}.} \tag{5.4}
\]

#### Proof

Linearize each fragment, retaining its \(L_j\) core starts and following
\(g-1\) singleton letters. This costs \(L_j+g-1\) letters and realizes
every target in \(\mathcal I_r\), irrespective of duplicates. Concatenate
the blocks and forbid witnesses from crossing a block boundary. Append one
letter equal to every absent band target and every nonempty target outside
the band. This proves (5.3).

At middle rank, (5.2) gives

\[
                         M+h_b=W+e_b.                \tag{5.5}
\]

Substitution in (5.3) proves (5.4). \(\square\)

For

\[
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,          \tag{5.6}
\]

the far-rank binomial tail is \(o(W)\). Hence a physical family with

\[
 e_b=o(W),\qquad gt=o(W),\qquad
 \sum_{\substack{b-H\le r\le b+H\\r\ne b}}h_r=o(W)   \tag{5.7}
\]

would imply \(\nu(2b)=(1+o(1))W\).

The word physical in Theorem 5.1 is essential. Each reverse hybrid is a
length-\(b\) sliding-window path: concatenate its removal stream and its
addition stream. But this realization is unique, and (3.2) places the
repeated label at word positions \(s\) and \(b+s+1\). Consequently the
length-\(b+2\) window beginning at position \(s\) repeats that label. Thus
the whole hybrid is not a physical \(H\)-fragment for any \(H\ge2\), in
particular not for (5.6), and it cannot enter (5.3) as one fragment.
Treating every bad seam separately by cutting there would produce
\(\Theta(C_b)\) pieces, whose boundary charge is
\(gt=\Theta(bC_b)=\Theta(W)\). A global reassembly might lower that charge,
but no such reassembly is supplied by this splice. Thus (4.5) supplies
neither the missing packet realization nor serialization and all-offset
control.

## 6. Exhaustive verification

The independent checker

    scratch/verify_gate_c_reverse_uhd_two_seam_no_go_20260823.py

enumerates every Dyck root in the requested dimensions. For each matched
pair it verifies (2.3), (2.8), both streams in (3.2), both Johnson
triangles, failure of the exact phase-packet predicate, and (4.1).
Globally it verifies the Chung--Feller partition and all counts in (4.4):

    python3 scratch/verify_gate_c_reverse_uhd_two_seam_no_go_20260823.py --max-b 10

The checker is evidence for the symbolic proof, not a substitute for it.
