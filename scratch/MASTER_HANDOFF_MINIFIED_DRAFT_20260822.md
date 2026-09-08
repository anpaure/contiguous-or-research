# Universal contiguous-subarray OR arrays: authoritative handoff

**Mathematical state:** 2026-08-22.

This file records the exact finite theorem and the shortest live route to

\[
\nu(k)=(1+o(1))W(k),\qquad
W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

It is a proof document, not a research diary. Every assertion used in a live
implication is proved here, either at its point of use or in an appendix.
Status tags mean:

- **[I]**: proved unconditionally in this file;
- **[C]**: the stated conclusion is proved in this file from every displayed
  hypothesis;
- **[O]**: open; and
- **[W]**: the sole exception to literal self-containment: a finite word body
  is external, while its length, hash, encoding, verifier, verifier proof, and
  matching internal lower bound are included here.

No source file, checker, hash, conjecture, or archived branch is a premise of
an [I] or [C] assertion. Section 2.1 records the decisive breakthrough for
every closed \(k=0,\ldots,16\).
Appendix letters and skipped internal numbers are stable historical labels;
omitted branches are not used.

The exact status is:

- **[I]+[W]** \(\nu(k)=B(k)\) for \(0\le k\le16\).
- **[I]+[W]/[O]** \(24313=B(17)\le\nu(17)\le25746\); equality is open.
- **[O]** \(\nu(k)=(1+o(1))W(k)\) is not proved.

There are three logically separate compiler branches:

\[
\begin{array}{c|c|c}
\text{punctured branch}&\text{independent fragment branch}&\text{cycle branch}\\ \hline
A\to\text{two-rank}\to B\to C_{\rm P}&C_{\rm F}&\text{DCC}\\
\downarrow&\downarrow&\downarrow\\
\text{Appendix I.1}&\text{Appendix I.1}&\text{Section 3.3}\\
\downarrow&\downarrow&\downarrow\\
\multicolumn{3}{c}{\nu(n)=(1+o(1))W(n)\ \text{on the respective base subsequences}}\\
\multicolumn{3}{c}{\downarrow\ \text{bounded top-bit splices}\ \downarrow}\\
\multicolumn{3}{c}{\nu(k)=(1+o(1))W(k)\quad[\mathrm C].}
\end{array}
\]

Here Gates \(A,B,C_{\rm P},C_{\rm F}\) are [O]; the Appendix I.1 and
DCC compiler implications are [C]. A DCC construction itself is [O].

The full Baranyai--Katona wreath conjecture is not a premise of any branch.
The independent coherent-tour fragment route in Sections 4.4--4.5 and
Appendix I bypasses Gates A and B; its cross-pairing selection gate is also
open.

## 1. Problem and exact state model

Identify a bit mask with a subset of `[k]`. All witnessing intervals are
nonempty: `1<=i<=j<=n`. For a word

\[
A=(A_1,\ldots,A_n),\qquad
U(i,j)=\bigcup_{p=i}^j A_p,
\]

let `N(k)` be the least `n` for which every subset of `[k]`, including the
empty set, occurs as an interval union `U(i,j)`; its letters may be empty.
Let `nu(k)` be the analogous minimum when every letter and every required
target is nonempty. We set `nu(0)=0`, witnessed by the empty word.

### 1.1 Zero theorem

\[
                         N(k)=\nu(k)+1.
\]

If a nonempty target is witnessed by an interval, deleting every zero letter
inside the word compresses the surviving positions of that interval to a
contiguous interval with the same union.  Thus deleting all zero letters
preserves all nonempty targets. Any nonempty interval with empty union
contains an empty letter, so a full word has at least one zero position;
deleting all such positions leaves at most `N(k)-1` letters and proves
`N(k)>=nu(k)+1`. Conversely, prepending one zero to a shortest nonzero word
realizes the empty target without changing any old witness, proving the
reverse inequality. This also gives `N(0)=1`.

### 1.2 Move-to-front theorem

At a right endpoint `j`, group the coordinates already seen by equal
last-occurrence time, most recent first:

\[
P_j=(B_1,\ldots,B_t).
\]

The distinct suffix unions ending at `j` are exactly the prefix unions of
this ordered partition: extending a suffix leftward crosses the last-occurrence
classes in recency order, and every nonempty prefix is reached. Appending a
nonempty letter `X` makes the exact
transition

\[
(B_1,\ldots,B_t)\longmapsto
(X,B_1\setminus X,\ldots,B_t\setminus X),
\]

after empty blocks are deleted.  Indeed every coordinate of `X` acquires the
new common last-occurrence time, while the other coordinates keep their old
relative recency; this proves both the update and its converse.  Hence `nu(k)`
is the shortest walk starting at the empty ordered partition, using one
nonempty move-to-front update per letter, whose prefix unions cover the
nonempty Boolean lattice.

For a set sequence `X`, define

\[
(DX)_i=X_i\cup X_{i+1},\qquad
(D^qX)_i=\bigcup_{p=i}^{i+q}X_p.
\]

Every interval union is an entry of the derivative triangle
`A,DA,D^2A,...`.

Throughout,

\[
W(k)=\binom{k}{\lfloor k/2\rfloor},\qquad
[x]_+=\max(x,0),\qquad
\operatorname{Cat}_r={1\over r+1}\binom{2r}{r}.
\]

## 2. Sharp lower bound, finite theorem, and unconditional upper bounds

For `1<=s<=k`, put

\[
M_s=\binom ks,\qquad
\Lambda_s=\sum_{j=1}^{s-1}\binom kj,
\]

and let

\[
\tau_s=\min\left\{t\in\mathbb Z_{\ge0}:
\Lambda_s\le tM_s+\binom{t+1}{2}\right\}.
\]

Then

\[
\boxed{\nu(k)\ge B(k):=\max_{1\le s\le k}(M_s+\tau_s).}
\]

Set `B(0)=0`.

For `k>=1`, the maximum is attained at `s=ceil(k/2)`. Writing
`W=binom(k,ceil(k/2))` and

\[
d(k)=\min\left\{d\in\mathbb Z_{\ge0}:dW+\binom{d+1}{2}\ge
\sum_{j=1}^{\lceil k/2\rceil-1}\binom kj\right\},
\]

one has

\[
B(k)=W+d(k),\qquad d(k)=\sqrt{\pi k/8}+O(1).
\]

Here is the complete proof.  Choose one witness interval for every rank-`s`
target and order the resulting `M_s` intervals by left endpoint.  Two
distinct equal-rank witnesses cannot contain one another: containment of
intervals implies containment of their unions, and equal finite cardinality
would then force equality.  Their right endpoints therefore occur in the
same strict order.  If the word has length `M_s+t`, the `i`-th interval has
endpoints

\[
 [i+\alpha_i,i+\beta_i],\qquad
 0\le\alpha_i\le\beta_i\le t;
\]

the upper bounds follow because `M_s-i` later distinct endpoints must still
fit to its right.  Any interval of length at least `t+1`, starting at `a`,
contains the `a`-th chosen interval (necessarily `a<=M_s`).  A witness for a
target of rank below `s` cannot contain a rank-`s` witness, so it has length
at most `t`.  The number of such intervals is exactly

\[
 \sum_{j=1}^t(M_s+t-j+1)=tM_s+\binom{t+1}{2}.
\]

This proves the displayed lower bound.

It remains to justify the asserted maximizing rank.  Put

\[
 F_s=M_s(M_s+1)+2\Lambda_s.
\]

Since `\Lambda_{s+1}=\Lambda_s+M_s`, direct subtraction gives

\[
 F_{s+1}-F_s=(M_s+M_{s+1})(M_{s+1}-M_s+1).
\]

The adjacent ratio
`M_{s+1}/M_s=(k-s)/(s+1)` proves binomial unimodality. Therefore `F_s` is
maximal at
`s=ceil(k/2)` (for `k=2` there is an irrelevant tie).  If `N=W+d`, the
central defining inequality is exactly `N(N+1)>=F_{ceil(k/2)}`.  For any
other `s`, put `t=N-M_s`; then

\[
 tM_s+\binom{t+1}{2}
 ={N(N+1)-M_s(M_s+1)\over2}\ge\Lambda_s.
\]

Thus `M_s+\tau_s<=N`, proving the maximizer claim.  Finally, for
`m=ceil(k/2)`, symmetry gives

\[
 {\Lambda_m\over W}=
 \begin{cases}
 2^{k-1}/W-1/2+O(W^{-1}),&k\text{ even},\\
 2^{k-1}/W+O(W^{-1}),&k\text{ odd}.
 \end{cases}
\]

The internally proved estimate (A.2),
`W=2^k\sqrt{2/(\pi k)}(1+O(1/k))`, makes this
`\sqrt{\pi k/8}+O(1)`.  The quadratic term
is controlled noncircularly as follows: `d=ceil(\Lambda_m/W)` is admissible,
so the least `d` is `O(sqrt(k))`. Hence
`\binom{d+1}{2}=O(k)=o(W)` and it changes the least admissible integer by only
`O(1)`, proving `d(k)=\sqrt{\pi k/8}+O(1)`.

### 2.1 Exact finite values [I]+[W]

The lower bound is attained for every `0<=k<=16`:

| `k` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `nu(k)` | 0 | 1 | 2 | 4 | 7 | 12 | 21 | 37 | 72 |

| `k` | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `nu(k)` | 128 | 254 | 465 | 926 | 1719 | 3434 | 6438 | 12873 |

The historically decisive breakthrough for each closed dimension was:

| `k` | `nu(k)` | breakthrough that first closed the case |
|---:|---:|---|
| 0 | 0 | the empty word |
| 1 | 1 | the singleton word and the one-target bound |
| 2 | 2 | a direct two-letter construction and endpoint count |
| 3 | 4 | three singleton positions cannot realize all three two-sets |
| 4 | 7 | Sperner-equality rigidity forces one position beyond width |
| 5 | 12 | the odd two-middle-layer obstruction forces `W+2` |
| 6 | 21 | general Sperner-equality rigidity plus an attaining word |
| 7 | 37 | the odd two-middle-layer obstruction plus a graded word |
| 8 | 72 | the rank-count bound plus a graded fixed-window construction inspired by the `k=7` pattern |
| 9 | 128 | short-cell saturation forces `D^2A` to enumerate rank five; a compatible middle-level factor exists |
| 10 | 254 | a Johnson chronology with complete two-sided shadows and exact delay-two factor labeling |
| 11 | 465 | quotient SAT found a resident all-shadow voltage-two carrier; a safe cut and exact compiler completed it |
| 12 | 926 | one-hole recovery completed the 924-state central path and its natural factor |
| 13 | 1719 | two perfect carrier cycles were cut and joined by one Johnson seam; the compiler absorbed the lost boundary colour |
| 14 | 3434 | a six-piece odd-to-even `A/B` braid supplied exact depth-two residence and compilation |
| 15 | 6438 | resident cycles of lengths `6390+45`, an upper-safe nonrecycling seam, two boundary colours, and the generalized compiler |
| 16 | 12873 | after one singleton was pre-pinned, one common-cap SAT model assigned the remaining 26,331 lower targets injectively to short cells while enforcing a shared nonempty source letter at every position |

This table is historical provenance, not an extra lemma; optimality in every
row follows only from the analytic lower bound and the [W] literal word
certificate described in Appendix B. Historically, `k=12` closed before
`k=11`.

Appendix B identifies the literal external word bodies by hash and contains
their exact recurrence verifier together with its proof. The words themselves
are the sole permitted self-containment exception [W]; all lower bounds and
all reasoning about them are internal.

For `k=17`,

\[
\boxed{24313=B(17)\le\nu(17)\le25746.}
\]

The upper bound is the internally proved top-bit splice applied to the
external [W] `k=16` witness.
No word of length `24313` and no equality proof is known.

### 2.2 Architecture-free constraints and upper bounds

For every coordinate set `Q`, deleting all letters meeting `Q` leaves a
universal word on `[k]\Q`. Indeed, a witness for a target disjoint from
`Q` contains no letter meeting `Q`; after all other letters are deleted, its
surviving positions remain consecutive and have the same union. Thus

\[
\#\{i:A_i\cap Q=\varnothing\}\ge\nu(k-|Q|),
\]

Summing over all `t`-sets `Q` counts position `i` exactly
`binom(k-|A_i|,t)` times and gives

\[
\sum_i\binom{k-|A_i|}{t}\ge\binom kt\nu(k-t).
\]

For `k>=2`, the simple top-bit splice gives `nu(k)<=2nu(k-1)`: if
`X=(X_1,...,X_n)` is universal on `k-1` coordinates and `z` is new, use

\[
X_1,\ldots,X_n,\{z\},X_1\cup\{z\},\ldots,X_{n-1}\cup\{z\}.
\]

A target not containing `z` is witnessed in the first copy. If `T` is
witnessed by `X_i,...,X_j`, then `T\cup\{z\}` is witnessed in the lifted
copy when `j<n`, and by `X_i,...,X_n,{z}` when `j=n`; `{z}` is the bridge
itself. The length is `2n`.

The strongest retained unconditional full-cube asymptotic construction is

\[
\boxed{\nu(k)\le(\sqrt2+o(1))W(k).}
\]

The proof is reproduced in Appendix A.

## 3. Exact compiler facts and the asymptotic reduction

### 3.1 Unrestricted interval normal form

Choose one interval `I_S=[ell_S,r_S]` for every nonempty target. The sets
with common left endpoint and those with common right endpoint form two
ordered inclusion-chain partitions. They are orthogonal and triangular.
Indeed, intervals with a common left endpoint are nested, so their unions
form an inclusion chain; the same holds at a common right endpoint. Two
distinct targets cannot have both endpoints equal, because one interval has
only one union, proving orthogonality. Along a left chain, larger targets have
larger right endpoints; along a right chain they have smaller left endpoints;
and every occupied pair satisfies `ell_S<=r_S`, proving the order and
triangularity assertions.

Conversely, index the two chain partitions by positions `p,q`, and give a
target belonging to their unique intersection the interval `[p,q]`.
Orthogonality makes these intervals distinct and triangularity makes them
nonempty. This prescribes witnesses, but realization has one additional exact
condition.  Put

\[
Z_x=[n]\setminus\bigcup_{S:x\notin S}I_S.
\]

The assignment is realized exactly when

\[
                 I_S\cap Z_x\ne\varnothing
                 \quad(S\ne\varnothing,\ x\in S).       \tag{3.1}
\]

Necessity is immediate: every occurrence of `x` must avoid every interval
whose target omits `x`, hence lies in `Z_x`, while a positive interval must
contain such an occurrence. For sufficiency set
`A_j={x:j\in Z_x}`. An interval whose target omits `x` contains no legal
position for it, while (3.1) supplies `x` to every interval requiring it.
Thus `\bigcup_{j\in I_S}A_j=S` for every target. Finally
`\bigcup_xZ_x=[n]` is exactly the condition that every letter be nonempty;
otherwise empty positions may be deleted without changing nonempty unions.

### 3.2 Flat central compiler

Fix a rank-`s` chronology `T=(T_1,...,T_W)` and depth `d`. A possibly empty
letter factor `A` with `D^dA=T` exists exactly when every internal run of
ones in every coordinate-incidence word of `T` has length at least `d+1`.
The maximal factor is

\[
A_j^{\max}=\bigcap_{\max(1,j-d)\le i\le\min(W,j)}T_i.
\]

To prove the criterion, work one coordinate at a time. Any occurrence at
position `j` lies in every `d+1` window whose union is one, so every factor
satisfies `A_j\subseteq A_j^{max}`. Conversely, a one in `T_i` is recovered
from the maximal factor precisely when some `j\in[i,i+d]` is contained in no
zero window. For an internal one-run `[p,q]` this requires and is implied by
`p+d<=q`, i.e. length at least `d+1`; prefix and suffix runs use the truncated
intersections and impose no length condition. Thus the maximal factor works
exactly under the stated run condition. Under that run condition, a factor
with no empty letters and the same length exists exactly when every
`A_j^{max}` is nonempty.

The exact lower-target compiler can also be stated without shorthand. Give
each desired lower target `S` a short interval `J_S\subseteq[W+d]`, and for
each coordinate `x` put

\[
E_x=[W+d]\setminus\bigcup_{i:x\notin T_i}[i,i+d],\qquad
Q_x=E_x\setminus\bigcup_{S:x\notin S}J_S.             \tag{3.2}
\]

The owner windows and assigned lower intervals are simultaneously realized
by a nonzero factor if and only if

\[
\begin{aligned}
J_S\cap Q_x&\ne\varnothing &&(x\in S),\\
[i,i+d]\cap Q_x&\ne\varnothing &&(x\in T_i),\\
\bigcup_xQ_x&=[W+d].
\end{aligned}                                        \tag{3.3}
\]

Necessity follows because a negative window or interval forbids `x`, whereas
each positive one must contain it. For sufficiency take
`A_j={x:j\in Q_x}`; (3.2) forbids every unwanted coordinate and (3.3)
supplies every required one. This is why an SDR ignoring the legal-position
sets `Q_x` is insufficient.

Upper targets have the following equally exact oracle. For a starting owner
`T_i`, define the first-arrival time

\[
\delta_i(x)=\min\{0\le q\le W-i:x\in T_{i+q}\},
\]

with value infinity when the set is empty. For a nonempty `S`, a consecutive
owner union is exactly `S` for some endpoint if and only if, for some `i`,

\[
       \max_{x\in S}\delta_i(x)
       <\min_{y\notin S}\delta_i(y).                 \tag{3.4}
\]

The minimum over an empty outside set is infinity.

Indeed, stop at the last first arrival among coordinates of `S`; (3.4) says
that every coordinate of `S` and no outside coordinate has appeared. The
converse is immediate from any witnessing run.

### 3.3 Defective central covering

Let `n=2m+1`, `W=binom(n,m)`, and

\[
H=\lceil\sqrt{n\log n}\rceil.
\]

A `DCC(n,H,delta)`, where `delta>=0`, is a cyclic singleton word of length at most
`(1+delta)W` such that

1. equal letters have cyclic distance at least `m+H+2`; and
2. the total number of rank-band targets not cleanly realized over ranks
   `m-H,...,m+1+H` is at most `delta W`.

A cyclic distance is the smaller number of index steps in the two directions
around the cycle between two occurrences.
A rank-`ell` target is *cleanly realized* when it is the union of a cyclic
window of exactly `ell` singleton positions whose labels are pairwise
distinct.

Linearize the cycle by writing one period followed by its first `m+H`
letters. This costs `O(n)` and retains every cyclic window of band length.
The gap condition makes each such window clean. Append one letter equal to
each missing band target (at most `delta W` letters), and then one letter per
nonempty far-rank target. Their exact number is one less than, and hence at
most,

\[
2\sum_{j=0}^{m-H-1}\binom nj
 \le 2^{n+1}e^{-2(H+1)^2/n}=o(W).
\]

For completeness, the tail inequality is elementary. If
`X~Bin(n,1/2)`, then

\[
\mathbb E e^{\lambda(X-n/2)}=
\bigl(\cosh(\lambda/2)\bigr)^n\le e^{n\lambda^2/8}.
\]

The last inequality follows because
`d(log cosh u)/du=tanh u<=u` for `u>=0` and both functions are even.

For `lambda<0`, on the event `X-n/2<=-a` one has
`exp(lambda(X-n/2))>=exp(-lambda a)`. Markov's inequality and
`lambda=-4a/n` therefore give
`Pr(X<=n/2-a)<=e^{-2a^2/n}`; take `a=H+1`. Also
`W>=2^n/(n+1)` because the largest of the `n+1` binomial coefficients is
at least their average. With `H=ceil(sqrt(n log n))`, the displayed tail
is therefore `o(W)`, and `O(n)=o(W)` as well. The final length is
`(1+2delta)W+o(W)`.

Therefore, if such a `DCC(n,H_n,delta_n)` exists for every sufficiently
large odd `n`, with `H_n=ceil(sqrt(n log n))` and `delta_n->0`, then

\[
\boxed{\nu(k)=(1+o(1))W(k).}
\]

Even dimensions follow from the internally proved top-bit splice and the
identity

\[
\binom{2m+2}{m+1}=2\binom{2m+1}{m};
\]

the lower bound gives the matching coefficient-one lower estimate. This
proves the boxed implication without any prime-gap input.

## 4. Live coefficient-one architecture

For the punctured two-rank problem put

\[
b=2r+1,\qquad
\mathcal M=\binom{[b]}r,\qquad
\mathcal L=\binom{[b]}{r-1},\qquad
A=|\mathcal M|,\qquad A/b=\operatorname{Cat}_r.
\]

For the product compiler and coherent tours, \(b\) is odd,
\(|\Omega|=2b\), and \(W=\binom{2b}b\). Context determines which notation is
in force.

### 4.1 The punctured two-rank hypergraph [I]

For a permutation \(w=(w_0,\ldots,w_{b-1})\), with subscripts modulo \(b\),
write

\[
I_k^w(s)=\{w_s,\ldots,w_{s+k-1}\}
\]

and define

\[
E(w)=\{(\mathcal M,I_r^w(s)):s\ne0\}
\;\dot\cup\;
\{(\mathcal L,I_{r-1}^w(s)):s\ne0\}.
\]

It has \(4r\) vertices, \(2r\) on each shore. Its containment graph is a
canonically oriented alternating path, so \(w\mapsto E(w)\) is injective
and there are \(b!\) configurations. Every middle and lower target has
degree

\[
D_M=2r\,r!(r+1)!,\qquad D_L={r+2\over r}D_M.
\]

Weight \(1/D_L\) on every configuration is an optimal fractional matching:
it saturates the lower shore, loads each middle target by \(r/(r+2)\), and
has mass \(|\mathcal L|/(2r)\).

For fixed \(e\), let \(q(T)\) be the number of distinct cyclic boundary cuts
used by \(T\subseteq e\). The boundary graph is
\(\operatorname{Cay}(\mathbb Z_b,\{\pm1,\pm3\})\) with two edges deleted;
every subgraph with \(m\) edges and \(v\) nonisolated vertices has
\(m\le2(v-1)\). Consequently, for an absolute \(C\) and \(|T|\ge2\),

\[
{\deg(T)\over D_M}\le C^{|T|}r^{\,2-q(T)}.             \tag{4.1}
\]

The exact pair inventory also gives

\[
{1\over D_M}\sum_F\binom{|e\cap F|}{2}
=12+{32\over r}+{99\over2r^2}+O(r^{-3}).              \tag{4.2}
\]

Thus the local enumeration, fractional optimum, and all-order boundary
codegrees are closed. They do not constitute a matching theorem.

### 4.2 Product-law control and stopped descent [I]/[C]

Independently retain lower targets with density \(x\) and middle targets
with density

\[
y={rx+2\over r+2}.
\]

Put \(d_x=D_Mx^{2r}y^{2r-1}\). Conditional on a fixed configuration \(e\)
surviving, let

\[
\mathcal E_x(e)=
\mathbb E\!\left[\sum_{F\ {\rm surviving}}(|e\cap F|-1)_+
\,\middle|\,e\ {\rm survives}\right].
\]

Then

\[
{\mathcal E_x(e)\over r d_x}
=O\!\left({1\over rx^3}\right),                         \tag{4.3}
\]

uniformly for \(x\ge r^{-\alpha}\), every fixed \(\alpha<1/3\). For a fixed
retained target \(v\), the rooted estimate gives

\[
{\operatorname {Var}X_v\over(\mathbb EX_v)^2}
\le {1\over\mathbb EX_v}+O\!\left({1\over rx^3}\right). \tag{4.4}
\]

For each fixed integer \(s\ge1\) and \(\alpha<1/(6s)\),

\[
{\mathbb E(X_v-\mathbb EX_v)^{2s}\over(\mathbb EX_v)^{2s}}
=O_s((rx^3)^{-s}).                                      \tag{4.5}
\]

The moment estimates remain valid after conditioning on both exact shore
sizes, with exponentially small comparison error. They are annealed or
fixed-slice results, not estimates for the adaptive residual law.

For the actual isolated-edge process, after round \(j\) let \(H_j\) be the
residual hypergraph, \(Z_j=|E(H_j)|\), and \(M_j,L_j\) its shores. Put

\[
x_j={|L_j|\over|L_0|},\qquad
\bar d_j^M={2rZ_j\over|M_j|},\qquad
\bar d_j^L={2rZ_j\over|L_j|}.
\]

Fix \(K\ge1\), set \(\gamma=1/(96K)\), and take
\(0<\alpha\le1/(256K)\). In every good round, mark each residual
configuration with probability

\[
p_j={\gamma\over r\bar d_j^M}.                         \tag{4.6}
\]

Assume, until \(x_j\le r^{-\alpha}\), only

\[
\max_{v\in M_j}d_j(v)\le K\bar d_j^M,\qquad
\max_{v\in L_j}d_j(v)\le K\bar d_j^L.                  \tag{4.7}
\]

The internal covariance and drift proof gives

\[
\Pr\!\left(
\begin{array}{c}
\text{the cap persists to the threshold, but a bite estimate}\\
\text{or the resulting two-shore descent fails}
\end{array}\right)
\le e^{-\Omega(r)}.                                    \tag{4.8}
\]

On success, the accepted configurations form a matching leaving
\(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and \(o(1)\) of the middle
shore. The cap also preserves an \(\exp(r\log r)\) average-degree floor
through the required \(O_K(r\log r)\) rounds. Equation (4.8) is a
stopped-event statement; it is not a conditional probability given the
future event that the cap persists.

### 4.3 The all-depth capacity boundary [I]/[C]

For a matching \(\mathcal P\) of punctured configurations, retain its starts
\((w,s)\) with \(s\ne0\), and for \(1\le q\le H\) define

\[
h_q^-(\mathcal P)=\binom b{r-q}
-\left|\{I_{r-q}^w(s):(w,s)\text{ is retained}\}\right|,
\]

\[
h_q^+(\mathcal P)=\binom b{r+1+q}
-\left|\{I_{r+1+q}^w(s):(w,s)\text{ is retained}\}\right|. \tag{4.9}
\]

If the unmatched lower-shore density is \(x\), then whenever
\(H\ge\lfloor\sqrt{rx}/4\rfloor\) and \(rx\ge64\),

\[
\sum_{q\le H}(h_q^-+h_q^+)
\ge {7\over32}|\mathcal L|\sqrt r\,x^{3/2}.            \tag{4.10}
\]

Therefore aggregate \(o(A)\) Gaussian-band holes require

\[
x=o(r^{-1/3}).                                         \tag{4.11}
\]

The stopped descent in Section 4.2 ends earlier, so Gate A alone cannot give
all-depth coverage. There are two exact continuations:

1. continue the same literal bank below (4.11) and prove distinct coverage
   at every depth \(q\le H\); or
2. prove a positive fractional cover of mass
   \(O(x\operatorname{Cat}_r)\); C.10 then rounds it to
   \(O(x\log r\,\operatorname{Cat}_r)\) compatible rows while leaving only
   \(o(A)\) holes.

For the second route, the logarithmic rounding overhead is harmless because
\(x\log r=o(1)\) in the live fixed-power range. The missing input is the
fractional cover itself, equivalently a capacity-sized hole-aligned
external-window degree tail. Uniform use of the complete survivor catalogue
does not supply it. Appendices H.11, H.15, and H.16 prove a local affine identity and
remote shore-difference and Venn-gap estimates. They do not convert those
estimates into one positive cover on the stopped residual at every depth;
that conversion remains open.

### 4.4 A direct literal fragment compiler [C]

Put \(|\Omega|=2b\), with odd \(b\), and
\(H=\lceil\sqrt{2b\log(2b)}\rceil\), \(g=b+H\). For all sufficiently large
\(b\), \(H\le b-2\). A physical fragment of core length \(L\) is a
singleton word with \(L\) consecutive designated starts such that, for
every \(s\in[b-H,b+H]\), all \(L\) length-\(s\) windows at those starts
exist and contain distinct letters.  Linearize the fragment by retaining
the core and its following \(g-1\) letters, at cost \(L+g-1\).

Take fragments whose middle cores are pairwise target-disjoint. Let \(M\)
be the total core size, \(t\) the number of fragments, and \(h_s\) the
number of rank-\(s\) targets absent from all designated windows. Then

\[
\boxed{
\nu(2b)\le M+(g-1)t
+\sum_{s=b-H}^{b+H}h_s
+\sum_{|s-b|>H}\binom{2b}s.}                           \tag{4.12}
\]

Every designated witness lies inside its own block, so overlaps outside
the disjoint middle cores cause no serialization conflict. Appending one
set-valued letter per absent target proves (4.12). The binomial tail in
(4.12) is \(o(W)\). Hence

\[
M=(1-o(1))W,\qquad (g-1)t=o(W),\qquad
\sum_{s=b-H}^{b+H}h_s=o(W)                              \tag{4.13}
\]

imply \(\nu(2b)=(1+o(1))W\).

An explicit sufficient schedule chooses any
\(a_b\to\infty\), \(a_b=o(\log b)\), constants \(0<c<2\), \(0<\theta<1\),
and

\[
L_b=\left\lfloor{cb\log b\over a_b}\right\rfloor.
\]

If \(O(a_b)\) residual-disjoint fragment matchings, each covering at least a
\(\theta\)-fraction of the current middle residual, leave at most
\(e^{-a_b}W\) middle targets and have aggregate off-middle band holes
\(o(W)\), then \(t\le W/L_b\) and

\[
(g-1)t=O\!\left({a_b\over\log b}W\right)=o(W),
\]

so (4.13) holds. This is a complete compiler theorem. The correlated
fragment matchings and their literal band coverage are open.

### 4.5 Coherent-tour banks [I]

Fix a perfect pairing \(\mathcal Q=\{P_0,\ldots,P_{b-1}\}\) of \(\Omega\)
and a directed cyclic order of its pairs. A coherent tour \(T(x)\), indexed
by \(x\in\mathbb F_2^b\), consists of \(b\) FIFO packets and has

\[
q=b(b-1)
\]

distinct internal middle targets. Each such target is defect one relative
to \(\mathcal Q\): one pair is empty, a different pair is doubled, and all
other pairs are split. The stratum has exactly

\[
q2^{b-2}                                                \tag{4.14}
\]

targets. Thus one pairing supports at most
\(2^{b-2}/(1-\varepsilon)\) rankwise-disjoint tours after retaining
\((1-\varepsilon)q\) targets from each. A near-factor consequently needs

\[
\Omega(2^b/b^{5/2})                                     \tag{4.15}
\]

different pairings. Conversely, for every \(a_b\to\infty\), a menu of

\[
(a_b+o(1)){4\over\sqrt\pi}{2^b\over b^{5/2}}            \tag{4.16}
\]

pairings misses at most \(e^{-a_b}W\) middle targets.

For one pairing and order, equality of targets from \(T(x)\) and \(T(x')\)
at ranks \(b-1,b,b+1\) depends only on \(x+x'\). The forbidden set
\(\mathcal B\subseteq\mathbb F_2^b\setminus\{0\}\) satisfies

\[
|\mathcal B|\le M_b:=2b^3+8b^2-16b.                    \tag{4.17}
\]

For every integer \(1\le H=o(b/\log b)\), there is, for all sufficiently
large \(b\), a full-rank map

\[
A:\mathbb F_2^b\longrightarrow\mathbb F_2^d,\qquad
d=\lceil\log_2(4M_b)\rceil,
\]

such that, for \(C=\ker A\),

\[
C\cap\mathcal B=\varnothing,\qquad d(C^\perp)>H.        \tag{4.18}
\]

Every coset of \(C\) is therefore a jointly three-rank-disjoint bank of
\(2^{b-d}=2^b/\operatorname{poly}(b)\) tours. The cosets exactly fourfold
resolve the fixed-pairing middle stratum. Dual distance makes each coset
exactly \(H\)-wise uniform in the state bits, so within a fixed pairing and
order all cosets have identical target-incidence profiles of order at most
\(H\). In particular every ground coordinate belongs to exactly half of the
middle targets in every bank, independently of the pairing; any
target-disjoint union of whole banks preserves this half-star balance.

This is local, not Gate C. Banks from different pairings can collide;
higher-order profiles can depend on the pairing; the selected tours have not
been placed with \(q-o(q)\) flags in one common extendable symmetric-chain
factor; and ranks outside \(b-1,b,b+1\) remain uncontrolled.

## 5. Exact remaining gates

### Gate A [O]: quenched cap preservation

For one fixed \(K>1\), and \(0<\alpha\le1/(256K)\), run the actual
isolated-edge process of Section 4.2 and stop at the first round when either
\(x_j\le r^{-\alpha}\) or one inequality in (4.7) fails. Prove

\[
\Pr(\text{the degree cap fails before the density threshold})=o(1). \tag{5.1}
\]

Together with (4.8), this yields the punctured two-rank near-factor. The
boundary codegrees, annealed and exact-slice moments, bite concentration,
empirical degree floor, and stopped descent are already proved. A maximum
degree cap does not generically propagate itself; the proof must exploit the
punctured interval geometry. The shortest current product-law target is the
tail-relative signed connected-carrier hierarchy under the appropriate Palm
law: its first unresolved member is the connected two-star, and the signed
higher-star remainder must be controlled with it. Stopped slice, center,
erosion, and purge transfer are then still required.

### Gate B [O]: critical all-depth cover-down

On the same literal bank produced after Gate A, prove one of:

- continuation to \(x=o(r^{-1/3})\) together with
  \(\sum_{q\le H}(h_q^-+h_q^+)=o(A)\); or
- a compatible positive fractional cover of the holes of mass
  \(O(x\operatorname{Cat}_r)\), followed by the proved rounding theorem,
  which uses \(O(x\log r\,\operatorname{Cat}_r)\) physical rows.

The rows must cover all depths \(q\le H=\lceil\sqrt{b\log b}\rceil\) in one
common occurrence state. Raw capacity, conservation, complete-catalogue
averaging, or a two-rank matching does not prove this gate. The
zero-avoidance lemmas in Appendix H are only partial estimates: the missing
output is still a compatible positive cover, on this stopped bank, at all
displayed depths simultaneously.

### Gate C [O]: either product lift or independent fragment selection

There are two distinct interfaces; they must not be conflated.

- **Gate \(C_{\rm P}\).** From the same literal \(b\)-coordinate row bank
  produced by Gate B, construct on
  \(\Omega=[b]\mathbin{\dot\cup}[b]'\) a family of physical fragments
  satisfying the three conditions in (4.13), equivalently (I.41).
  This includes the presently missing product lift, all-offset coverage,
  and serialization.
- **Gate \(C_{\rm F}\).** Independently select repaired coherent-tour
  fragments from the balanced coset banks of Section 4.5 so that (I.41)
  holds.  This requires cross-pairing target-disjoint selection and
  all-band literal repair, but does not use Gates A or B.

Either output is already a literal compiler antecedent; no common
symmetric-chain factor or odd DCC is silently assumed.

### Gate D [O]: finite \(k=17\)

Independently close \(24313\le\nu(17)\le25746\). Witnesses constructed in
different occurrence states cannot be composed without a literal common
replay.

## 6. Completion implications

If Gates A, B, and \(C_{\rm P}\) are proved with their common-object
requirements, the resulting literal fragment family satisfies (4.13),
equivalently Appendix I.1's finite compiler hypothesis. That
compiler gives

\[
\nu(k)=(1+o(1))W(k).
\]

This would be a genuine construction: deterministic if the gates are
constructive, or a probabilistic existence construction with a finite
positive-probability sample space otherwise. It would not imply the literal
equality \(\nu(k)=W(k)\); the proved lower bound is
\(B(k)=W(k)+\Theta(\sqrt k)\).

Independently, \(C_{\rm F}\) gives the same fragment hypothesis and hence
the same conclusion without Gates A or B. If an odd singleton cycle is
instead constructed, the DCC criterion of Section 3.3 is a third,
logically separate compiler. In either fragment route the base dimensions
are \(2b\) with odd \(b\); the top-bit splice, used at most three times,
covers every sufficiently large dimension with asymptotic ratio one.

## 7. Scope walls

1. The Baranyai--Katona wreath conjecture is not required by either
   fragment branch.
2. A two-rank matching controls only the vertices in its hypergraph; it says
   nothing by itself about deeper windows.
3. Annealed or exact-slice estimates do not imply their adaptive quenched
   analogues.
4. Exact regularity, small pair codegree, and bounded local statistics do
   not generically force a near-matching; Appendix C.6 gives a counterexample.
5. Nominal product degrees are not tangent-invariant under an isolated-edge
   bite. The stopped descent correctly uses empirical shore averages.
6. Separately constructed factors, retirement assignments, banks, and
   compilers cannot be composed unless they use one common literal
   occurrence state.
7. A fixed-pairing coset resolution is not a cross-pairing near-factor.
   Low-order balance does not control every residual obstruction.
8. Overlap between fragment domains is harmless only because each fragment
   is linearized in its own block. Middle-core disjointness, \(W+o(W)\)
   total mass, \(o(W)\) holes, and \(o(W)\) seams remain mandatory.

## 8. Completion ledger and audit contract

| item | status | exact boundary |
|---|---|---|
| rank-witness lower bound and central maximizer | [I] | closed |
| exact values \(0\le k\le16\) | [I]+[W] | only literal word bodies are external |
| \(k=17\) | [I]+[W]/[O] | \(24313\le\nu(17)\le25746\) |
| DCC implies coefficient one | [C] | closed |
| punctured local profile and fractional optimum | [I] | closed |
| all-order boundary codegrees and boundary polymers | [I] | closed |
| fixed-target product/exact-slice moments | [I] | closed in the stated ranges |
| cap-preserving stopped descent | [C] | succeeds unless the cap fails first |
| Gate A | [O] | quenched cap preservation |
| all-depth capacity bound and fractional-cover rounding | [I]/[C] | positive hole-aligned cover is open |
| zero-avoidance local affine gap, remote shore-difference bound, and Venn-gap localization | [I] | closed partial Gate-B lemmas |
| conversion of zero-avoidance estimates into one all-depth positive cover | [O] | no such stopped-bank cover is proved |
| Gate B | [O] | critical cover-down on one literal bank |
| physical-fragment literal compiler | [C] | fragment selection and band holes are open |
| pairing menus and balanced three-rank coset banks | [I] | local; cross-pairing selection is open |
| Gate \(C_{\rm P}\) | [O] | product lift from the Gate-B bank to (I.41) |
| Gate \(C_{\rm F}\) | [O] | cross-pairing selection and all-band repair to (I.41) |
| coefficient-one theorem | [O] | no assembled construction |

Every refresh must:

1. retain a complete proof for every [I] and [C] assertion;
2. retain the full \(k=0,\ldots,16\) breakthrough table;
3. recompute every [W] hash and run the included finite-word verifier;
4. keep the word bodies as the only exception to literal self-containment;
5. repeat every hypothesis when invoking a conditional theorem;
6. preserve the stopped-event form (4.8), not conditioning on future cap
   persistence;
7. distinguish two-rank, all-depth, and serialization conclusions; and
8. never mark coefficient one proved until one literal construction passes
   the analytic interval-union verification.

The finite theorem through \(k=16\) is closed. The coefficient-one
asymptotic remains open at punctured Gates A, B, and \(C_{\rm P}\), at
independent Gate \(C_{\rm F}\), and at the separate DCC construction.

# Appendix A: Elementary asymptotics and the `sqrt(2)` construction

## Appendix A.1: Central-binomial estimate

For completeness, the only asymptotic estimate used in Sections 2 and 2.2
is proved here. Put

\[
I_n=\int_0^{\pi/2}\sin^n x\,dx.
\]

Integration by parts gives `I_n=(n-1)I_{n-2}/n`, whence

\[
I_{2m}={\pi\over2}{\binom{2m}m\over4^m},\qquad
I_{2m+1}={4^m\over(2m+1)\binom{2m}m}.
\]

Since `I_{2m}>=I_{2m+1}>=I_{2m+2}` and
`I_{2m}/I_{2m+2}=(2m+2)/(2m+1)`, the ratio
`I_{2m}/I_{2m+1}` lies between `1` and `1+1/(2m+1)`. Substituting the two
product formulas therefore gives

\[
\binom{2m}m={4^m\over\sqrt{\pi m}}(1+O(1/m)).       \tag{A.1}
\]

The same formula and the adjacent-binomial ratio imply, uniformly as
`t->infinity`,

\[
W(t)=\binom t{\lfloor t/2\rfloor}
     =2^t\sqrt{2\over\pi t}\,(1+O(1/t)).             \tag{A.2}
\]

## Appendix A.2: Symmetric chains and bridge words

The Boolean lattice on a `t`-set partitions into saturated chains whose
bottom and top ranks sum to `t`. This follows by induction: from a chain
`C_0 subset ... subset C_s`, after adjoining a new element `x`, use the long
chain

\[
C_0\subset\cdots\subset C_s\subset C_s\cup\{x\}
\]

and, when nonempty, the short chain

\[
C_0\cup\{x\}\subset\cdots\subset C_{s-1}\cup\{x\}.
\]

These chains are disjoint, cover both copies of the old lattice, and remain
symmetric. Every symmetric chain meets rank `floor(t/2)` exactly once, so
every such decomposition has `W(t)` chains.

For a saturated chain `C=(C_0 subset ... subset C_s)` in universe `U`, define
its bridge word

\[
\beta_U(C)=(C_0,C_1\setminus C_0,\ldots,
            C_s\setminus C_{s-1},U\setminus C_s),
\]

omitting empty blocks. Its blocks are nonempty and disjoint. Prefix unions,
including the empty prefix, contain every `C_i`; suffix unions, including the
empty suffix, contain every `U\setminus C_i`.

## Appendix A.3: The construction

Split `[k]=P dotcup Q`, where `|P|=p`, `|Q|=q`, `p,q>=1`, and distinguish
`z in P`. Take a symmetric-chain decomposition of `2^{P\setminus\{z\}}`.
Replace each chain by its long lifted chain ending with the old top together
with `z`; call the resulting family `mathcal C`. It has
`a=W(p-1)` chains, and every subset of `P\setminus\{z\}` occurs in exactly
one member. Take a symmetric-chain decomposition `mathcal D` of `2^Q`, of
size `b=W(q)`.

Form the directed complete bipartite graph on
`mathcal C dotcup mathcal D`, with both directed arcs between every left and
right vertex. It is strongly connected and every indegree equals the
corresponding outdegree, so the following elementary Euler argument applies:
follow unused outgoing arcs until stuck. A nonstarting endpoint would have
used one more incoming than outgoing arc, impossible because its total
indegree equals its total outdegree, so the trail closes at its start. If an
arc remains, strong connectivity supplies a visited vertex with an unused
outgoing arc; form another closed trail there and splice it into the first.
Iteration terminates in a circuit using every arc once.

Start the Euler circuit at a right vertex, concatenate the bridges of the
tails of its `2ab` directed arcs in traversal order, and then append one more
copy of the starting right bridge. Let a nonempty target be `S=X\cup Y`, with `X subseteq P` and
`Y subseteq Q`. If `z in X`, then `P\setminus X` lies on a unique lifted
chain `C`, while `Y` lies on a unique `D`; across the occurrence of the arc
`C->D`, take the suffix of `beta_P(C)` with union `X` and the following prefix
of `beta_Q(D)` with union `Y`. If `z notin X`, use the unique chains containing
`Q\setminus Y` and `X` across the reverse arc `D->C`. One part may be empty,
but not both, so this is a nonempty interval with union exactly `S`.

In an SCD of `2^t`, the sum of bridge lengths is `2^t+W(t)-2`: the unique
chain containing the empty set contributes one less than its membership,
and every other chain one more. The lifted left chains have total membership
`2^{p-1}+a`, hence total bridge length `2^{p-1}+2a-2`; the right total is
`2^q+b-2`. In the first `2ab` visits of the circuit each left vertex occurs
as a tail `b` times and each right vertex `a` times. Cutting at a right vertex
adds at most `q+2` symbols. Thus

\[
L\le b(2^{p-1}+2a-2)+a(2^q+b-2)+q+2.              \tag{A.3}
\]

Choose `p=ceil(k/2)` and `q=floor(k/2)`. Formula (A.2) gives

\[
b2^{p-1}+a2^q=(\sqrt2+o(1))W(k),
\]

whereas `ab=O(2^k/k)=o(W(k))` and `q=o(W(k))`. Therefore

\[
                     \nu(k)\le(\sqrt2+o(1))W(k),
\]

with no external construction theorem.


# Appendix B: The sole self-containment exception—finite word bodies

The only mathematical data not printed in this handoff are the literal
whitespace-separated mask words answers/k01.word through
answers/k16.word. This exception is denoted **[W]**. The currently stored
byte bodies have the following SHA-256 integrity digests. These hashes are
provenance only; mathematical validity comes from applying the displayed
recurrence verifier to the supplied word bodies.

The lower-bound arithmetic from Section 2 is entirely internal:

| `k` | central `r` | `W` | `Lambda_r` | `d` | `B(k)` |
|---:|---:|---:|---:|---:|---:|
| 0 | - | - | - | - | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 1 | 2 | 0 | 0 | 2 |
| 3 | 2 | 3 | 3 | 1 | 4 |
| 4 | 2 | 6 | 4 | 1 | 7 |
| 5 | 3 | 10 | 15 | 2 | 12 |
| 6 | 3 | 20 | 21 | 1 | 21 |
| 7 | 4 | 35 | 63 | 2 | 37 |
| 8 | 4 | 70 | 92 | 2 | 72 |
| 9 | 5 | 126 | 255 | 2 | 128 |
| 10 | 5 | 252 | 385 | 2 | 254 |
| 11 | 6 | 462 | 1023 | 3 | 465 |
| 12 | 6 | 924 | 1585 | 2 | 926 |
| 13 | 7 | 1716 | 4095 | 3 | 1719 |
| 14 | 7 | 3432 | 6475 | 2 | 3434 |
| 15 | 8 | 6435 | 16383 | 3 | 6438 |
| 16 | 8 | 12870 | 26332 | 3 | 12873 |
| 17 | 9 | 24310 | 65535 | 3 | 24313 |

For every `d>0`, the two integer inequalities

\[
(d-1)W+\binom d2<\Lambda_r\le dW+\binom{d+1}2
\]

are immediate from the displayed entries; when `d=0`, `Lambda_r=0`.

| \(k\) | length | SHA-256 |
|---:|---:|---|
| 1 | 1 | 4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865 |
| 2 | 2 | f251ddc12234e0da8d3b778bd0f7463fb477f16f47757f5617dc8b4ff4d4f14a |
| 3 | 4 | aafa934d13be209cc39a9b5cb0b140af652fc0eebd127c42c6c982422964a790 |
| 4 | 7 | efe145ebc697686a2e3bf53a36362b5025835f2eb0ba16a1a0e64e2abd4ec1ca |
| 5 | 12 | 72195450d0361b37fbf58442203014eff475b3f59222c907fab99743106eee06 |
| 6 | 21 | 7d30e058f98e6c09d65515e3f3971ae8bd7637f711670fa06a8a1dc536852d6d |
| 7 | 37 | dda4b06c2e35bda3ea8a876a90807172adee166567d84b587ef5ae68cae9bec7 |
| 8 | 72 | df6d76b468bd816fd014d9b6f5259ba60e5f1ea06e4c4313901fe6155c8780eb |
| 9 | 128 | c7e8cbfbe1a3531ffae4c9a01bd4b3b51dad0856b38486bacc56dbcaa73e3221 |
| 10 | 254 | 24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd |
| 11 | 465 | 746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850 |
| 12 | 926 | 6d598c62f5925d1d2dfce8279eea82069318bd93ff66d0b204c639cf06297851 |
| 13 | 1719 | 8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0 |
| 14 | 3434 | 7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17 |
| 15 | 6438 | f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b |
| 16 | 12873 | 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe |

Everything needed to interpret and verify those words is internal. Each file
is a whitespace-separated list of ordinary decimal integers. The following
recurrence is the complete verifier:

~~~python
def check(k, expected_length, masks):
    a = [int(x) for x in masks.split()]
    assert len(a) == expected_length
    assert all(0 < x < (1 << k) for x in a)
    ending, seen = set(), set()
    for x in a:
        ending = {x} | {y | x for y in ending}
        seen |= ending
    assert seen == set(range(1, 1 << k))
~~~

After processing position \(j\), induction shows that ending is exactly the
set of unions of nonempty intervals ending at \(j\): an interval is either
the singleton last letter or a previous ending interval extended by that
letter. Thus acceptance proves universality. Section 2 proves the matching
lower bounds analytically. The \(k=17\) upper bound needs no additional word:
the internally proved top-bit splice applied to the \(k=16\) certificate has
length \(2\cdot12873=25746\).

# Appendix C: Complete proofs for the direct punctured route

This appendix contains the retained proofs for the direct punctured route. No computation or external file is a premise of an argument below.

## Appendix C.1: Boundary-polymer estimate

Let \(B_r\) be the punctured boundary graph whose vertices are the \(b\)
boundary cuts and whose \(4r\) edges are the tagged targets of one
configuration:
\[
 B_r=\operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})
       \setminus\{\{0,1\},\{0,3\}\}.
\]
For an edge set \(T\subseteq E(B_r)\), let
\(q(T)=|V(T)|\) be its number of incident boundary cuts.  Define

\[
 \mathcal P_2(z)=
 \sum_{\substack{T\subseteq E(B_r)\\|T|\ge2}}
 |T|^2z^{|T|}r^{-q(T)}.
\]

There are absolute constants \(c_0,c_1>0\) such that, uniformly for
\(0\le z\le c_0\sqrt r\),

\[
 \boxed{\mathcal P_2(z)\le
 c_1\left({z^2\over r^2}+{z^4\over r^2}\right).}
\]

### Proof of the polymer estimate

Write a nonempty edge subgraph of \(B_r\) as the disjoint union of its
connected components.  In a graph of maximum degree four, an exploration
from a prescribed root vertex encodes every connected \(m\)-edge subgraph
by one of at most \(A_0^m\) bounded-choice exploration words, for an absolute
constant \(A_0\).  Thus the total activity \(z^m r^{-v}\) of connected
\(m\)-edge subgraphs is at most
\[
        bA_0^m z^m r^{-v}.
\]
For \(m=1,2,3\), simplicity and triangle-freeness give
\(v\ge2,3,4\), respectively.  The graph is triangle-free for \(b\ge11\):
three signed steps from \(\{1,3\}\) have odd integer sum of absolute value
at most nine and hence cannot vanish modulo \(b\).  The finitely many
smaller \(b\) are absorbed into the constants.  For \(m\ge4\), the density
bound \(m\le2(v-1)\) gives \(v\ge m/2+1\).  Consequently, if \(\eta_j\)
denotes the sum of \(m^j\) times the activities of connected polymers, and
\(\eta_2^{\ge2}\) omits the one-edge polymers, then for
\(z\le c_0\sqrt r\), after decreasing \(c_0\),
\[
\eta_0=O(z/r+z^4/r^2),\quad
\eta_1=O(z/r+z^4/r^2),\quad
\eta_2^{\ge2}=O(z^2/r^2+z^4/r^2).
\]
Dropping mutual vertex-disjointness between components only enlarges the
sum.  For \(|T|\ge2\),
\(|T|^2\le2|T|(|T|-1)\).  Marking the ordered pair of distinguished
edges either inside one nontrivial component or in two components, and
then applying the exponential formula, gives
\[
\mathcal P_2(z)
 \le2e^{\eta_0}\bigl(\eta_2^{\ge2}+\eta_1^2\bigr)
 =O(z^2/r^2+z^4/r^2).
\]
This proves the asserted estimate.

## Appendix C.2: Annealed regeneration


### Proof of annealed regeneration

Let \(t_F=|e\cap F|\) and put \(a=x^{-1}-1\).  If \(F\) overlaps \(e\) in
\(\ell\) lower and \(m\) middle targets, then, conditional on retaining
all targets of \(e\), its additional retention probability is
\(x^{2r-\ell}y^{2r-m}\).  Because \(y\ge x\), after division by
\(d_x=D_Mx^{2r}y^{2r-1}\) this is at most
\(yx^{-t_F}/D_M\).  Also
\((t-1)_+\le\binom t2\), and
\[
\binom t2x^{-t}
=x^{-2}\sum_{s=2}^t\binom ts\binom s2a^{s-2}.
\]
Double-counting pairs \((F,T)\) with
\(T\in\binom{e\cap F}{s}\) therefore gives
\[
\frac{\mathcal E_x(e)}{rd_x}
\le {y\over rD_Mx^2}
\sum_{s=2}^{4r}\binom s2a^{s-2}
\sum_{T\in\binom es}\deg(T).
\]
Apply the boundary-codegree theorem, set \(z=Ca\), and use
\(\binom s2\le s^2/2\).  For \(a>0\), the last double sum divided by
\(D_M\) is at most
\[
 {r^2\over2a^2}\mathcal P_2(Ca)=O_C(1+a^2).
\]
For \(a=0\) the same statement is the continuous limit, or follows
directly from the \(s=2\) term.  Since
\(\alpha<1/3\) gives \(Ca=o(\sqrt r)\), and
\(y/x=1+O(1/(rx))\), it follows that
\[
\frac{\mathcal E_x(e)}{rd_x}
=O_C\!\left({1+a^2\over rx}\right)
=O_C\!\left({1\over rx^3}\right)=o(1)
\]
uniformly for \(x\ge r^{-\alpha}\).

## Appendix C.3: Fixed-target residual variance

### Proof of the fixed-target variance bound

Condition on retaining \(v\), and write
\[
 X_v=\sum_{F\ni v}I_F,
\]
where \(I_F\) says that every target of \(F-\{v\}\) is retained.
All \(I_F\) have the same mean \(w_v\), so
\(\mu_v=\mathbb EX_v=d(v)w_v\).  If
\(t=|F\cap G|\), every common target other than \(v\) has retention
probability at least \(x\), whence
\[
 {\mathbb E(I_FI_G)\over\mathbb EI_F\,\mathbb EI_G}
 \le x^{-(t-1)}.
\]
With \(a=x^{-1}-1\),
\[
x^{-(t-1)}-1
=\sum_{\varnothing\ne S\subseteq(F\cap G)-\{v\}}a^{|S|}.
\]
Summing over ordered `F,G`, separating diagonal variances, and
double-counting `G` containing `\{v\}\cup S` gives
 \[
 {\operatorname{Var}X_v\over\mu_v^2}
 \le {1\over\mu_v}+
 {1\over d(v)^2}\sum_{F\ni v}
 \sum_{\varnothing\ne S\subseteq F-\{v\}}
 a^{|S|}\deg(\{v\}\cup S)
 \le {1\over\mu_v}+{1\over d(v)}
 \max_{F\ni v}\sum_{\varnothing\ne S\subseteq F-\{v\}}
 a^{|S|}\deg(\{v\}\cup S).
\]

Here `d(v)` is the degree in the full punctured-configuration hypergraph, so
it is `D_M` or `D_L`. Choose a maximizing `F`, identify the canonical
boundary graph of the targets of `F` with `B_r`, and let \(R\) be the
boundary edge representing \(v\). Set
\(z=Ca\).  The boundary-codegree theorem and \(d(v)\ge D_M\) bound the last
term, up to one absolute factor, by
\[
\sum_{\varnothing\ne S\subseteq E(B_r)-\{R\}}
 z^{|S|}r^{2-|V(R\cup S)|}.
\]
To estimate this rooted sum, decompose \(R\cup S\) into its component
containing \(R\) and its other components.  The unrooted component
activity from the preceding polymer proof is
\(\eta_0=O(z/r+z^4/r^2)\).  A root component with one added edge costs
\(O(z/r)\); with two added edges it costs \(O(z^2/r^2)\), by
triangle-freeness; and with at least three added edges the density bound
gives the geometric tail
\[
\sum_{m\ge4}A_0^m z^{m-1}r^{1-m/2}=O(z^3/r).
\]
Dropping disjointness of the other components multiplies this by at most
\(e^{\eta_0}\), while the possibility of no added root edge and at least
one remote component contributes \(e^{\eta_0}-1\).  Hence the rooted sum
is
\[
O(z/r+z^3/r+z^4/r^2).
\]
For \(x\ge r^{-\alpha}\), \(\alpha<1/3\), one has
\(z=O_C(x^{-1})=o(\sqrt r)\); substitution yields
 \[
 {\operatorname{Var}X_v\over\mu_v^2}
 \le {1\over\mu_v}+
O_C(a/r+a^3/r+a^4/r^2)
\le {1\over\mu_v}+O_C(1/(rx^3)).
\]
The mean \(\mu_v\) is exponential in this range, proving the final
\(o(1)\): indeed `D_M=exp((2+o(1))r log r)`, while each indicator `I_F`
requires exactly `4r-1` further targets, each retained with probability at
least `x`, so
`mu_v>=D_M x^{4r-1}=exp((2-4alpha+o(1))r log r)`.

## Appendix C.3bis: Rooted overlap kernels

Use the directed punctured-configuration hypergraph with parameter `r`.
Fix one target `v` and condition on retaining it.  Every other lower target
is retained independently with probability `x`, every other middle target
with probability `y>=x`, and

\[
                         x\ge r^{-\alpha}.           \tag{C.3bis.1}
\]

Let `mathcal F_v` be the `D=d(v)` configurations containing `v`.  Put

\[
 X_v=\sum_{F\in\mathcal F_v}I_F,
 \qquad \mu=\mathbb EX_v=Dw,                       \tag{C.3bis.2}
\]

where `I_F` says that all targets of `F-{v}` survive.  The mean `w` is the
same for every `F in mathcal F_v`, since every configuration has the same
two shore sizes.  For distinct `F,G in mathcal F_v`, write

\[
                   t(F,G)=|(F\cap G)-\{v\}|.        \tag{C.3bis.3}
\]

For each fixed real `c>=1`, define

\[
 R_c=\max_F {1\over D}\sum_{G\ne F}
                 (x^{-c t(F,G)}-1),                 \tag{C.3bis.4}
\]

and

\[
 Q_c=\max_F {1\over D}\sum_{\substack{G\ne F\\t(F,G)>0}}
                 x^{-c t(F,G)}.                     \tag{C.3bis.5}
\]

### Lemma C.3bis.1 (rooted kernel bounds)

For every fixed `c`, uniformly under (C.3bis.1), provided `c alpha<1/2`,

\[
 R_c=O_c\left({1\over r x^{3c}}+{1\over r^2x^{4c}}\right),
 \qquad
 Q_c=O_c\left({1\over r x^{3c}}+{1\over r^2x^{4c}}\right).   \tag{C.3bis.6}
\]

In particular

\[
                         R_1=O((rx^3)^{-1}).         \tag{C.3bis.7}
\]

#### Proof

The rooted-polymer proof for the variance applies with retention floor
`x^c`.  With

\[
                         a_c=x^{-c}-1,
\]

its nonnegative overlap expansion gives

\[
 R_c=O_c\left({a_c\over r}+{a_c^3\over r}
                         +{a_c^4\over r^2}\right)
       +e^{-\Omega_c(r\log r)}.                     \tag{C.3bis.8}
\]

The exponentially small term is the excluded diagonal `G=F`; it is
negligible because `c alpha<1/2`.  The activity condition in the polymer
estimate is also valid, since `a_c=O(r^(c alpha))=o(sqrt r)`.

To pass from `R_c` to `Q_c`, first note

\[
 {1\over D}\sum_{G\ne F}\mathbf1_{t(F,G)>0}
 \le {1\over D}\sum_{G\ne F}t(F,G)=O(1/r).         \tag{C.3bis.9}
\]

The last estimate is the coefficient of the linear activity in the same
rooted overlap polynomial: divide its bound
`O(a/r+a^3/r+a^4/r^2)` by `a` and let `a` decrease to zero.  All
coefficients are nonnegative, so the passage to the limit is valid.
Finally

\[
 \mathbf1_{t>0}x^{-ct}
 \le \mathbf1_{t>0}+(x^{-ct}-1),                   \tag{C.3bis.10}
\]

and (C.3bis.8)--(C.3bis.10), together with `a_c<=x^{-c}`, prove (C.3bis.6).
\(\square\)

### Lemma C.3bis.2 (unrooted surviving-row moments)

Let \(\mathcal N=b!\) be the number of configurations, let
\(\mathsf Z=\sum_FI_F\) count those surviving the independent product
retention, and put \(w_0=x^{2r}y^{2r}\). For every fixed \(s\ge1\), if
\(0<\alpha<1/(6s)\), \(x\ge r^{-\alpha}\), and \(y\ge x\), then
\[
 \boxed{{\mathbb E(\mathsf Z-\mathbb E\mathsf Z)^{2s}
       \over(\mathbb E\mathsf Z)^{2s}}
       =O_s((rx)^{-s}).}                                  \tag{C.3bis.11}
\]

#### Proof

For configurations \(F,G\), put \(t_0(F,G)=|F\cap G|\), and define
\[
\begin{aligned}
 \widehat R_c&={1\over\mathcal N}\max_F\sum_{G\ne F}
                    (x^{-ct_0(F,G)}-1),\\
 \widehat Q_c&={1\over\mathcal N}\max_F
        \sum_{\substack{G\ne F\\t_0(F,G)>0}}x^{-ct_0(F,G)}.
\end{aligned}                                             \tag{C.3bis.12}
\]
For every \(1\le c\le s\),
\(a_c=O(r^{c\alpha})=o(\sqrt r)\), so the polymer estimate applies. Let
\(A=\binom br\) and
\(\vartheta=D_M/\mathcal N=2r/A=e^{-\Theta(r)}\). With
\(a_c=x^{-c}-1\), expand \((1+a_c)^t-1\) and double-count
\(T\subseteq F\cap G\). Singleton \(T\)'s contribute
\(O(\vartheta r a_c)\), since \(F\) has \(4r\) targets and both target
degrees are \(\Theta(D_M)\). For \(|T|\ge2\), C.7 and C.1 give
\[
 {1\over\mathcal N}\sum_{\substack{T\subseteq F\\|T|\ge2}}
 a_c^{|T|}\deg(T)
 \le C\vartheta r^2\mathcal P_2(Ca_c)
 =O_c(\vartheta(a_c^2+a_c^4)).                            \tag{C.3bis.13}
\]
Also
\[
 {1\over\mathcal N}\sum_{G\ne F}\mathbf1_{t_0(F,G)>0}
 \le {1\over\mathcal N}\sum_{G\ne F}t_0(F,G)
 =O(\vartheta r).                                         \tag{C.3bis.14}
\]
Consequently
\[
\begin{aligned}
 \widehat R_c&=O_c(\vartheta(ra_c+a_c^2+a_c^4)),\\
 \widehat Q_c&=O_c(\vartheta(r+ra_c+a_c^2+a_c^4)).
\end{aligned}                                             \tag{C.3bis.15}
\]

Expand the \(2s\)-th centered moment. For distinct rows, join two indices
when their configurations overlap. A singleton dependency component has
zero expectation. After summation, a two-row component costs
\((\mathcal Nw_0)^2\widehat R_1\). For a component of \(j\ge3\) rows,
put \(t_{ab}=t_0(F_a,F_b)\). A uniformly random spanning tree of the
complete graph on \([j]\) contains each pair with probability \(2/j\).
Thus a maximum-weight spanning tree \(T\) satisfies
\[
 \sum_{a<b}t_{ab}\le {j\over2}\sum_{ab\in T}t_{ab}.
\]
The positive-overlap graph is connected, so \(T\) may use only positive
edges. Since \(0<x\le1\),
\[
 x^{-\sum_{a<b}t_{ab}}
 \le\prod_{ab\in T}\mathbf1_{\{t_{ab}>0\}}
                         x^{-(j/2)t_{ab}}.
\]
There are \(j^{j-2}\) labelled trees. Root one and sum its leaves
successively with \(\widehat Q_{j/2}\). The component sum is at most
\[
 O_j((\mathcal Nw_0)^j\widehat Q_{j/2}^{\,j-1}).
\]
Because \(\vartheta=e^{-\Theta(r)}\) while
\(a_c\le r^{c\alpha}\), (C.3bis.15) is smaller than every required fixed
power of \((rx)^{-1}\). Thus a \(j\)-row component costs
\(O_s((\mathcal Nw_0)^j(rx)^{-j/2})\); multiplying components gives the
right side of (C.3bis.11).

For repeated rows use
\((I-w_0)^h=A_h(I-w_0)+B_h\), where
\(|A_h|\le1\) and \(|B_h|\le w_0\), and group equal indicators.
The resulting terms have fewer distinct rows and an extra \(w_0\) for
each constant group. They are negligible because
\(\mathcal Nw_0\ge\exp((2-4\alpha+o(1))r\log r)\).
\(\square\)

## Appendix C.3ter: Fixed slices and the stopped Palm reduction

We first remove exact shore cardinalities as a possible obstruction.  Let
`R` be a uniformly random `m`-subset of an `N`-set and put `p=m/N`.  For a
fixed `a`-set `U`,

\[
 \Pr(U\subseteq R)={(m)_a\over(N)_a}.              \tag{C.3t.1}
\]

If `a<=q<=m/2`, then

\[
 \left|\log{{(m)_a/(N)_a}\over p^a}\right|
 \le {2q^2\over m}.                                \tag{C.3t.2}
\]

Indeed, the logarithm is

\[
 \sum_{i=0}^{a-1}\{\log(1-i/m)-\log(1-i/N)\},
\]

and the derivative of `log(1-z)` has absolute value at most two on
`[0,1/2]`.  Thus two independent uniform shore slices, of densities at
least `x` and minimum population `N_*`, reproduce every query using at most
`q` coordinates on either shore with relative error

\[
                              O(q^2/(xN_*)).         \tag{C.3t.3}
\]

The error remains relative to the rare survival scale after centering.
Fix a root target \(v\) and distinct configurations `F_1,...,F_j` containing \(v\). Let `I_F` be its survival
indicator, let `w` and `tilde w` be its product and slice means, and write

\[
                         t(F,G)=|(F\cap G)-\{v\}|.
\]

For each shore \(\sigma\), let \(p_\sigma\) be its product retention probability, let \(a_\sigma\) be the number of nonroot shore-\(\sigma\) targets in one \(F_i\), and for \(S\subseteq[j]\) put
\[
 u_\sigma(S)=\left|\bigcup_{i\in S}((F_i\cap V_\sigma)-\{v\})\right|.
\]
Thus \(w=\prod_\sigma p_\sigma^{a_\sigma}\). When the union queries at most `q` coordinates per shore, expansion over
subsets of `[j]` and (C.3t.3) give

\[
 \left|
 \mathbb E_{\rm sl}\prod_i(I_{F_i}-\widetilde w)
 -\mathbb E_{\rm prod}\prod_i(I_{F_i}-w)
 \right|
 \le C_j{q^2\over xN_*}
 w^j x^{-\sum_{a<b}t(F_a,F_b)}.                   \tag{C.3t.4}
\]

To verify the scale explicitly, for every subset `S` in the centered
expansion the product probability divided by `w^|S|` is

\[
 \prod_\sigma p_\sigma^{-(|S|a_\sigma-u_\sigma(S))}
 \le x^{-\sum_{a<b\in S}t(F_a,F_b)},              \tag{C.3t.5}
\]

because a coordinate of multiplicity `c` satisfies
`c-1<=binom(c,2)`.  Also `tilde w/w=1+O_j(q^2/(xN_*))`.
Equations (C.3t.3)--(C.3t.5), term by term over the `2^j` subsets, prove
(C.3t.4).

Now condition on a fixed root target and let `X_v` be its residual degree.
For a fixed `2s`th moment, a tuple queries `q=O_s(r)` coordinates per shore.
The punctured target populations satisfy `N_*=exp(Omega(r))`, so the error
in (C.3t.4) is exponentially small.  It remains to sum its overlap weight.
If `R_c` is the rooted kernel from C.3bis, insertion of `F_i` after
`F_1,...,F_(i-1)` uses

\[
 x^{-\sum_{a<i}t(F_a,F_i)}
 \le {1\over i-1}\sum_{a<i}x^{-(i-1)t(F_a,F_i)}   \tag{C.3t.6}
\]

by arithmetic--geometric mean.  Successive row sums therefore give

\[
 \sum_{F_1,\ldots,F_j\ {\rm distinct}}
 x^{-\sum_{a<b}t(F_a,F_b)}
 \le D^j\prod_{i=2}^j(1+R_{i-1})=O_s(D^j).        \tag{C.3t.7}
\]

Repeated configurations cause no larger error.  Group equal indicators
and use, for every fixed power,

\[
 (I-u)^a=A_a(I-u)+B_a,\qquad |A_a|\le1,\quad |B_a|\le u.       \tag{C.3t.8}
\]

Every resulting constant group removes at least one distinct configuration
and contributes a factor at most `w`; after summation these terms are
`O_s(mu^(2s-1))`, exponentially smaller than the main scale.  Combining (C.3t.4)--(C.3t.8) with the product dependency-component estimate (G.21)--(G.22) gives, uniformly on every exact two-shore slice, where \(\widetilde\mu=\mathbb E_{\rm sl}X_v\),

\[
 \boxed{
 {\mathbb E_{\rm sl}(X_v-\widetilde\mu)^{2s}
       \over\widetilde\mu^{2s}}
 =O_s((rx^3)^{-s})+O_s(r^2/(xN_*))}               \tag{C.3t.9}
\]

for `alpha<1/(6s)`.  The identical slice comparison applied to Lemma C.3bis.2 gives

\[
 {\mathbb E_{\rm sl}(\mathsf Z-\mathbb E_{\rm sl}\mathsf Z)^{2s}
       \over(\mathbb E_{\rm sl}\mathsf Z)^{2s}}
 =O_s((rx)^{-s})+O_s(r^2/(xN_*)).                 \tag{C.3t.10}
\]

## Appendix C.4: Cluster drift and its scale

In the initial full hypergraph, let \(s_e(p)\) be the probability that no
target of a fixed configuration \(e\) is deleted by an accepted
isolated-edge bite, and define \(s_v(p)\) analogously for one target.  Put

\[
 \mathfrak E(e)=\sum_{F:|F\cap e|>0}(|F\cap e|-1).
\]

Then

\[
 \boxed{\left.{d\over dp}\log
 {s_e(p)\over\prod_{v\in e}s_v(p)}\right|_{p=0}
 =\mathfrak E(e),\qquad
 {\mathfrak E(e)\over D_M}=12+O(1/r).}
\]

### Proof of the drift identity and its scale

Write \(t_F=|F\cap e|\) and
\(S(e)=\sum_F\binom{t_F}{2}\).

In the initial full hypergraph, let
\(\Gamma(e)=\{F:F\cap e\ne\varnothing\}\), and let \(d(v)\) be the full
target degree. At \(p=0\), to first order exactly one edge is
marked, and it is automatically isolated.  Therefore
\[
s_e'(0)=-|\Gamma(e)|,\qquad s_v'(0)=-d(v).
\]
Moreover
\[
\sum_{v\in e}d(v)-|\Gamma(e)|
=\sum_{F:t_F>0}(t_F-1)=\mathfrak E(e).
\]
Taking the logarithmic derivative proves the displayed identity.

For every integer \(t\ge0\),
\[
0\le\binom t2-(t-1)\mathbf1_{t>0}
={ (t-1)(t-2)\over2}\mathbf1_{t\ge3}
\le\binom t3.
\]
Thus
\[
0\le S(e)-\mathfrak E(e)\le M_3(e),
\qquad
M_3(e)=\sum_{T\in\binom e3}\deg(T).
\]
The boundary graph has bounded degree and is triangle-free for all
sufficiently large \(r\).  Its connected three-edge subgraphs number
\(O(r)\) and have at least four vertices; a two-edge component plus an
isolated edge gives \(O(r^2)\) choices and five vertices; and three
isolated edges give \(O(r^3)\) choices and six vertices.  The
boundary-codegree theorem consequently gives
\[
{M_3(e)\over D_M}
\le C^3\{O(r)r^{-2}+O(r^2)r^{-3}+O(r^3)r^{-4}\}
=O(1/r).
\]
The finitely many smaller \(r\) are absorbed into the constant.  Combining
this with the exact pair expansion proves
\(\mathfrak E(e)/D_M=12+O(1/r)\).

## Appendix C.5: Isolated-count covariance and one-cap descent

Use the process and averages of Section 4.2.  Fix \(K\ge1\), put
\(\gamma=1/(96K)\), \(p_j=\gamma/(r\bar d_j^M)\), and assume the two
maximum-degree caps (4.7) while \(x_j\ge r^{-\alpha}\), where
\(0<\alpha\le1/(256K)\).  Then

\[
 \Pr(\text{the caps persist to the threshold but a bite estimate or
 the descent fails})\le e^{-\Omega(r)}.
\]

On the complementary stopped event the accepted configurations form a
matching leaving \(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and
\(o(1)\) of the middle shore, and the average-degree floor remains at
least \(\exp(r\log r)\).

### Proof

Let \(G_j\) be the conflict graph on the \(Z_j\) surviving
configurations, let \(g_e\) be its degrees, and let
\(\Delta=\max_e g_e\).  For a general graph with \(Z\) vertices, mark
vertices independently with probability \(p\), and let \(A\) count marked
vertices having no marked neighbour.  Put
\[
q_e=p(1-p)^{g_e},\qquad \mu=\mathbb EA.
\]
Adjacent vertices have nonpositive covariance.  If \(e,f\) are
nonadjacent and \(c_{ef}=|N(e)\cap N(f)|\), then exactly
\[
\operatorname{Cov}(I_e,I_f)
=q_eq_f\{(1-p)^{-c_{ef}}-1\}.
\]
When \(p\le1/2\) and \(p\Delta\le B\), the braces are at most
\(2e^{2B}pc_{ef}\): indeed
`-log(1-p)<=2p`, so the braces are at most
`exp(2p c_(ef))-1`, and `exp(u)-1<=u exp(u)` for `u>=0`.
Finally,
\[
\sum_{e,f}c_{ef}=\sum_h|N(h)|^2\le Z\Delta^2,
\qquad
\mu\ge Zp(1-p)^\Delta\ge Zpe^{-2B}.
\]
Consequently
\[
{\operatorname{Var}A\over\mu^2}
\le C_B\left({1\over Zp}+{p\Delta^2\over Z}\right).
\tag{*}
\]

Each accepted configuration removes exactly `2r` targets from both shores.
Consequently
`|M_j|-|L_j|=|M_0|-|L_0|=2|L_0|/r`. Since
`|L_j|=x_j|L_0|`, under the displayed maximum-degree cap and while
\(x_j\ge r^{-\alpha}\), the exact shore relation is
\[
{ |M_j|\over|L_j|}
={\bar d_j^L\over\bar d_j^M}
=1+{2\over rx_j}\le2
\]
for all sufficiently large \(r\).  Hence
\[
\Delta(G_j)\le
2rK\bar d_j^M+2rK\bar d_j^L
\le6Kr\bar d_j^M.
\]
Also
\[
{1\over Z_j}\sum_e g_e
\le{1\over Z_j}\sum_vd_j(v)(d_j(v)-1)
\le2Kr(\bar d_j^M+\bar d_j^L)
\le6Kr\bar d_j^M.
\]
Since \(u\mapsto(1-p_j)^u\) has nonnegative second derivative, the finite
chord-induction proof of Jensen gives
\[
{\mathbb E(A_j\mid H_j)\over Z_jp_j}
\ge(1-p_j)^{6Kr\bar d_j^M}.
\]

Now take \(\gamma=1/(96K)\).  Once
\(\bar d_j^M\ge e^{r\log r}\), the last display is at least
\(e^{-12K\gamma}=e^{-1/8}\); here
`log(1-p)>=-2p` for `0<=p<=1/2`, as follows by differentiating the two
sides. In (*) one has
\(p_j\Delta\le1/16\), and the exact identity
\[
Z_jp_j={\gamma|M_j|\over2r^2}
\]
shows that the relative variance is
\(O_K(r^2/|M_j|)=e^{-\Omega(r)}\): indeed
`|M_j|>=|L_j|=x_j|L_0|>=r^(-alpha)|L_0|=e^(Omega(r))`;
the last fact follows from the binomial-average lower bound on `|M_0|` and
`|L_0|=r|M_0|/(r+2)`. Moreover `e^(-1/8)>=1-1/8=7/8`, so
`E(A_j|H_j)>=7Z_jp_j/8`; the event `A_j<Z_jp_j/2` has a fixed positive
relative deviation from this mean. Chebyshev's inequality in the form
`Pr(|A-EA|>=t)<=Var(A)/t^2` now gives the required lower bound below.
For the upper bound, if `Y` is the total number marked, then
`E(2^Y)=(1+p_j)^(Z_j)<=exp(Z_jp_j)`; the elementary Markov inequality
`E(2^Y)>=2^(2Z_jp_j)Pr(Y>=2Z_jp_j)` makes the failure probability at most
`exp(-(2 log 2-1)Z_jp_j)`. Since `A_j<=Y`, these two estimates give
\[
{1\over2}Z_jp_j\le A_j\le2Z_jp_j
\tag{**}
\]
with conditional failure \(e^{-\Omega(r)}\).

It remains only to justify the degree floor used in this argument.  Start
from
\[
Z_0={|M_0|D_M\over2r}=(2r+1)!,
\qquad \log Z_0=(2+o(1))r\log r.
\]
Every accepted configuration has \(2r\) targets on each shore, so its
closed conflict neighbourhood has size at most
\[
2rK\bar d_j^M+2rK\bar d_j^L\le6Kr\bar d_j^M.
\]
By the upper bound in (**),
\[
Z_j-Z_{j+1}
\le A_j\,6Kr\bar d_j^M
\le12K\gamma Z_j=Z_j/8.
\]
The lower bound in (**) removes at least \(\gamma/(2r)\) of each
residual shore per round.  Thus the lower density reaches
\(r^{-\alpha}\) within
\[
J_*=\left\lceil{2\alpha r\log r\over\gamma}\right\rceil
\]
rounds.  For \(\alpha\le1/(256K)\),
\[
\log Z_j\ge\log Z_0+j\log(7/8)
\ge(2-o(1))r\log r-{J_*\over7},
\qquad
{J_*\over7}\le{3\over28}r\log r+O(1).
\]
Since \(|M_j|\le\binom{2r+1}r=e^{O(r)}\), this implies
\(\bar d_j^M\ge e^{r\log r}\), closing the induction.  The conditional
failure probabilities union-bound over the
\(O_K(r\log r)\) stopped rounds.  Accepted configurations are disjoint
within a round, and deletion of their targets makes different rounds
disjoint.  The one-round overshoot is \(1+O_K(1/r)\), and
\[
{|M_j|\over|M_0|}={rx_j+2\over r+2}=o(1).
\]
Therefore
\[
\Pr(\text{the cap persists to the threshold but a bite estimate or the
descent fails})\le e^{-\Omega(r)}.
\]
Equivalently, outside an event of that probability, either the cap fails
first or the union of accepted configurations is a matching leaving
\(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and \(o(1)\) of the middle
shore. If a separate theorem makes cap failure `o(1)`, the two bad events
combine by a union bound.

## Appendix C.6: Generic local statistics do not imply a near-matching


Fix integers \(k,D\) with `D>=2` and
\(k\ge64\log(2eDk)\), and let \(L\) tend to infinity.  On a set \(X\) of
size \(LD\), choose \(k\) independent uniform equipartitions into \(L\)
blocks of size \(D\).  With probability \(1-o(1)\), every two blocks from
different partitions meet in at most two points: for a fixed pair the
probability of an intersection of size at least three is at most
\[
{\binom D3^2\over\binom{LD}3},
\]
and a union bound over \(O(k^2L^2)\) pairs tends to zero.

Simultaneously, with probability \(1-o(1)\), no two points have the same vector of blocks across all \(k\) partitions. For fixed \(x\ne y\), independence of the partitions gives probability
\[
 \left({D-1\over LD-1}\right)^k=O_{D,k}(L^{-k}).
\]
There are \(O_D(L^2)\) point pairs, and the displayed hypothesis implies \(k>2\), so another union bound is \(o(1)\).

Put \(Q=\log(2eDk)\), \(c=16Q/k\), and
\(s=\lceil cL\rceil\).  For a fixed \(s\)-set \(S\), the probability that
one equipartition puts its points in distinct blocks is
\[
p_s={(L)_sD^s\over(LD)_s}
\le\exp\{-s(s-1)/(4L)\}.
\]
Indeed, writing `x=i/L`, the logarithm of the `i`th product factor is
`f_D(x)=log(1-x)-log(1-x/D)`. For `0<=x<1` and `D>=2`,
\[
 f_D'(x)=-{D-1\over(1-x)(D-x)}\le-{D-1\over D}\le-{1\over2},
\]
so `f_D(x)<=-x/2`; summing `i=0,...,s-1` proves the bound.
The partitions are independent, and hence the expected number of
\(s\)-sets meeting every block in at most one point is at most
\[
\binom{LD}s p_s^k
\le\left({eLD\over s}\right)^s
   \exp\{-ks(s-1)/(4L)\}
\le e^{-sQ}=o(1).
\]
Here `c<=1/4` by the hypothesis on `k`. For all sufficiently large `L`,
`k(s-1)/(4L)>=2Q`, while
`log(eLD/s)<=log(eD/c)<=Q`; these give the last inequality. The binomial
estimate in the first inequality is internal too:
`log(s!)=sum_(i=1)^s log i >= integral_1^s log x dx`, hence
`s!>=(s/e)^s` and `binom(N,s)<=(eN/s)^s`.
Thus deterministic partitions exist with all three properties.

Make one hypergraph vertex for every block, one part for every partition,
and, for each \(x\in X\), one \(k\)-edge consisting of the \(k\) blocks
containing \(x\). The block-vector event makes these edges distinct, so the hypergraph is simple. It is \(D\)-regular, and pair codegrees are at most two.
The labels of pairwise disjoint hyperedges form a common partial
transversal, so every matching has fewer than \(cL\) edges and covers at
most \(c=O(\log(Dk)/k)\) of the vertices. Since `D` may be chosen
arbitrarily large and then `k` chosen to satisfy the displayed hypothesis,
this already gives arbitrarily large absolute degree while retaining
absolute pair codegree at most two. This proves the claimed generic no-go
without using an external source.

## Appendix C.7: Global boundary-codegree theorem

For targets \(T\) inside one fixed directed punctured configuration, let
\(q(T)\) be the number of distinct boundary cuts used by those targets.
For every \(|T|\ge2\), an absolute constant \(C\) satisfies

\[
 \boxed{{\deg(T)\over D_M}\le C^{|T|}r^{2-q(T)}.}
\]

The boundary graph is
\(\operatorname {Cay}(\mathbb Z_{2r+1},\{\pm1,\pm3\})\) with the two
start-zero edges deleted, and every subgraph with \(m\) edges and \(v\)
nonisolated vertices satisfies \(m\le2(v-1)\).

### Proof of the punctured-circulant density bound

Before the linear relabelling, a retained middle window starting at \(i\)
has boundary edge \(\{i,i+r\}\), and a retained lower window has boundary
edge \(\{i,i+r-1\}\).  Multiplication by \(-2\) modulo
\(b=2r+1\) sends these differences to \(1\) and \(3\), respectively.
The two dirty starts remove \(\{0,1\}\) and \(\{0,3\}\).

For a proper nonempty \(U\subset\mathbb Z_b\), let
\(\partial_d(U)\) be the number of step-\(d\) edges crossing its cut in
the full circulant.  The number of full-circulant edges induced by \(U\)
is
\[
2|U|-{\partial_1(U)+\partial_3(U)\over2}.
\]
The step-one cycle is connected, so \(\partial_1(U)\ge2\).  If
\(\partial_3(U)>0\), parity gives \(\partial_3(U)\ge2\).  If it is zero,
then \(3\mid b\) and \(U\) is a nontrivial union of complete step-three
cycles; its step-one cut has at least \(2b/3\) edges.  Thus every proper
\(U\) induces at most \(2(|U|-1)\) edges.  Deleting the two dirty edges
cannot increase this number, while the full punctured graph has
\(2b-2=2(b-1)\) edges.  Therefore every subgraph with \(m\) edges and
\(v\) nonisolated vertices satisfies \(m\le2(v-1)\).

### Proof of the boundary-codegree inequality

Fix \(T\subseteq e\), put \(t=|T|\), and list its \(q\) distinct boundary
cuts cyclically.  For target lengths \(k,h\in\{r,r-1\}\), fixing one
cyclic start and the intersection size leaves at most four possible
relative starts: the exact numbers are \(b-k-h+1\) in the disjoint case,
two in a proper overlap, and \(|k-h|+1\) in a containment.  Hence, after
choosing an anchor target, the number \(P(T)\) of retained positional
tuples having the prescribed labelled Venn signature satisfies
\[
                         P(T)\le(b-1)4^{t-1}.          \tag{B1}
\]

Let \(n_\sigma\) be the sizes of the labelled Venn cells and set
\[
V(T)=\prod_\sigma n_\sigma!.
\]
For a fixed positional tuple, labels may be assigned independently inside
corresponding cells in exactly \(V(T)\) ways.  Conversely, a proper
nonempty target has a unique cyclic start in a fixed word, so no word is
counted twice.  Thus
\[
                         \deg(T)=P(T)V(T).             \tag{B2}
\]

The \(q\) cuts divide the circle into positive elementary gaps
\(g_1,\ldots,g_q\), with sum \(b\); put \(G(T)=\prod_i g_i!\).
We claim
\[
                         V(T)\le8^{t-1}G(T).           \tag{B3}
\]
For one target, its arc and complement are exactly the two elementary gaps,
so `V=G` and the initial ratio `R=V/G` is one. Expose the remaining target
arcs one at a time. Splitting an
old Venn cell of size \(n\) into sizes \(p,n-p\) multiplies \(V\) by
\(\binom np^{-1}\), while splitting an elementary gap of size \(g\) into
\(a,g-a\) multiplies \(G\) by \(\binom ga^{-1}\).
If the two new cuts lie in distinct old gaps, independently selecting the
prescribed labels from those split gaps injects into the prescribed
subset of the containing Venn cell.  Therefore the product of the gap
binomials is at most the corresponding cell binomial, even when the two
gaps belong to the same cell, and \(R\) does not increase.  With one new
cut the same injection applies.  With two old cuts, \(G\) is unchanged
and every Venn-cell factorial can only decrease, so again \(R\) does not
increase.

If both new cuts lie in one old gap of size \(g\), write the three pieces
as \(x,y,z\), where \(y\) lies between the new cuts.  The gap refinement
factor is
\[
\binom gy\binom{g-y}x.
\]
The middle segment is either the new arc or its complement, so
\(y\in\{k,b-k\}\).  Fix the selected labels outside the old gap.
Adjoining a \(y\)-subset of the gap injects into the prescribed selected
subsets of the old Venn cell; if the middle segment is the complement,
apply the same injection to unselected labels and use binomial symmetry.
Thus the Venn-cell split cancels the first binomial.
After the first target has been exposed, every old gap has size at most
\(r+2\); hence \(g-y\le3\) if \(y=k\), and \(g-y\le1\) if
\(y=b-k\).  The uncancelled factor is at most
\(2^{g-y}\le8\).  This proves (B3) by induction.

Every gap is at most \(r+2\).  Factorial log-convexity says that moving one
unit from a smaller positive gap to a larger nonsaturated gap cannot
decrease the product of factorials.  Repeating this transfer yields
\[
G(T)\le
\begin{cases}
(r+2)!(r-q+1)!,&2\le q\le r,\\
(2r-q+2)!,&r+1\le q\le2r+1.
\end{cases}                                            \tag{B4}
\]
For completeness, for `1<=m<=n` the falling-factorial estimate used next is
internal:
\[
 \binom nm=\prod_{i=0}^{m-1}{n-i\over m-i}\ge(n/m)^m,
 \qquad
 \log(m!)\ge\int_1^m\log x\,dx\ge m\log m-m.
\]
Multiplication gives \((n)_m=m!\binom nm\ge(n/e)^m\). Using this, the
case `m=0` is immediate. The first case gives
\[
{G(T)\over r!(r+1)!}
\le {r+2\over(r)_{q-1}}
\le3e^{q-1}r^{2-q},
\]
and the second gives
\[
{G(T)\over r!(r+1)!}
\le e^{q-1}r^{1-q}\le e^q r^{2-q}.
\]
Thus, uniformly,
\[
{G(T)\over r!(r+1)!}\le(3e)^q r^{2-q}.                \tag{B5}
\]

Finally \(D_M=(b-1)r!(r+1)!\), and \(q\le2t\).
Combining (B1)--(B5) gives
\[
{\deg(T)\over D_M}
\le4^{t-1}8^{t-1}(3e)^q r^{2-q}
\le\{32(3e)^2\}^{t}r^{2-q}.
\]
This proves the displayed theorem with the explicit absolute constant
\(C=32(3e)^2\).

## Appendix C.8: Directed punctured-configuration profile

### Deck reconstruction, degrees, and the fractional optimum

In the unpunctured deck, containment between its \((r-1)\)- and
\(r\)-windows is the alternating cycle.  A cyclic \((r-1)\)-interval is
contained in exactly its two one-point end extensions, so there are no
other containment edges.  Deleting \(L_0,M_0\) leaves the path
\[
L_1,M_1,L_2,M_2,\ldots,L_{2r},M_{2r}.
\]
Its endpoint layers orient it canonically.  The recovered same-start
pairs satisfy
\[
M_i\setminus L_i=\{w_{i+r-1}\},\qquad1\le i\le2r.
\]
These give every word position except \(r-1\); the unique unused label
gives that final position.  Hence \(w\mapsto E(w)\) is injective and there
are \(b!\) configurations.

For a fixed \(k\)-set, prescribing any of its \(b-1\) retained starts
gives \(k!(b-k)!\) words, with no overcount because a proper cyclic
interval has a unique start.  Therefore
\[
D_M=(b-1)r!(r+1)!=2r\,r!(r+1)!,
\]
\[
D_L=(b-1)(r-1)!(r+2)!={r+2\over r}D_M.
\]
Weighting every configuration by \(1/D_L\) loads each lower target by
one and each middle target by \(D_M/D_L=r/(r+2)\).  Its total mass is
\[
{b!\over D_L}={|\mathcal L|\over2r},
\]
using the lower incidence identity
\(b!\,2r=|\mathcal L|D_L\).  No fractional matching can have larger mass:
each edge consumes \(2r\) units of the total lower capacity
\(|\mathcal L|\).  This proves optimality.

### Complete pair calculation

For target sizes \(k,h\in\{r,r-1\}\) and intersection \(a\), set
\[
\Phi_{k,h}(a)=a!(k-a)!(h-a)!(b-k-h+a)!
\]
and
\[
m_{k,h}(a)=
\begin{cases}
b-k-h+1,&a=0,\\
2,&0<a<\min(k,h),\\
|k-h|+1,&a=\min(k,h).
\end{cases}
\]
For distinct layer-tagged targets \(A,B\),
\[
d(A,B)=
\bigl((b-2)m_{k,h}(a)+\mathbf1_{a=\min(k,h)}\bigr)
\Phi_{k,h}(a).                                        \tag{P1}
\]
Indeed, after fixing the first cyclic start, the three cases have exactly
the displayed numbers of relative starts.  A positional pair has
\(\Phi_{k,h}(a)\) labelings of its four Venn cells.  Of the
\(bm_{k,h}(a)\) ordered start pairs, \(2m_{k,h}(a)\) have a dirty start;
\((0,0)\) was removed twice and is restored exactly in the same-start
containment case.  This proves (P1).

Inside one fixed configuration, the complete unordered inventory is
\[
\begin{array}{c|c|c|c}
XY&a&N&d\\ \hline
MM&0\le a\le r-1&2r-1&
(4r-2)a!(r-a)!^2(a+1)!\\
LL&0&4r-2&(8r-4)(r-1)!^2\,3!\\
LL&1\le a\le r-2&2r-1&
(4r-2)a!(r-1-a)!^2(a+3)!\\
ML&0&6r-3&(6r-3)r!(r-1)!\,2!\\
ML&1\le a\le r-2&4r-2&
(4r-2)a!(r-a)!(r-1-a)!(a+2)!\\
ML&r-1&4r-1&(4r-1)(r-1)!(r+1)!.
\end{array}                                            \tag{P2}
\]
The \(N\)-column is the retained ordered-start count from (P1), divided
by two only for equal-layer pairs.  Thus (P2) is an analytic inventory,
not a finite census.

Let \(S_{XY}\) be the pair-codegree mass from the indicated layer pair.
Multiplying the last two columns of (P2) and using factorial cancellation
gives the exact sums
\[
{S_{MM}\over D_M}
={(2r-1)^2\over r}
\sum_{a=0}^{r-1}
{1\over\binom ra\binom{r+1}{a+1}},                    \tag{P3}
\]
\[
{S_{ML}\over D_M}
={1\over2r}\sum_{a=0}^{r-1}
{n_{ML}(a)^2\over\binom ra\binom{r+1}{a+2}},           \tag{P4}
\]
\[
{S_{LL}\over D_M}
={r+2\over4r^2}\sum_{a=0}^{r-2}
{n_{LL}(a)^2\over\binom{r-1}a\binom{r+2}{a+3}},        \tag{P5}
\]
where
\[
n_{ML}(a)=
\begin{cases}
3(2r-1),&a=0,\\
2(2r-1),&1\le a\le r-2,\\
4r-1,&a=r-1,
\end{cases}
\quad
n_{LL}(a)=
\begin{cases}
4(2r-1),&a=0,\\
2(2r-1),&1\le a\le r-2.
\end{cases}
\]
For example, the cancellation behind (P3) is
\[
{a!(r-a)!^2(a+1)!\over r!(r+1)!}
={1\over\binom ra\binom{r+1}{a+1}},
\]
and the other two are identical.

Isolating the endpoint terms in these reciprocal-binomial sums gives
\[
\sum_{a=0}^{r-1}
{1\over\binom ra\binom{r+1}{a+1}}
={1\over r}+{2\over r^3}+O(r^{-4}).
\]
In (P4), the containment, disjoint, and \(a=r-2\) terms are respectively
\[
8-{4\over r}+{1\over2r^2},\qquad
{36\over r}-{72\over r^2}+O(r^{-3}),\qquad
{16\over r^2}+O(r^{-3});
\]
all other terms total \(O(r^{-3})\).  In (P5), the \(a=r-2\) and
\(a=0\) terms are
\[
{4\over r}+O(r^{-3}),\qquad
{96\over r^2}+O(r^{-3}),
\]
and the rest total \(O(r^{-3})\).  Here are uniform remainder bounds.
In (P3), the omitted \(a=2\) and \(a=r-2\) terms are respectively
\(O(r^{-5})\) and \(O(r^{-4})\); for
\(3\le a\le r-3\), both binomial factors are \(\Omega(r^3)\), so all
middle terms total \(O(r^{-5})\).  In (P4), the common proper-overlap
prefactor is \(O(r)\): the \(a=1\) term is \(O(r^{-3})\), and after it
is removed the two binomial factors have product \(\Omega(r^5)\), apart
from the already displayed right endpoint layers, so the remaining
\(O(r)\) terms total \(O(r^{-3})\).  The same argument applies to (P5):
its prefactor is \(O(r)\), its \(a=r-3\) term is \(O(r^{-3})\), and all
other undisplayed terms have binomial product \(\Omega(r^5)\).  The
finitely many small \(r\) are absorbed by the constants.  This proves the
stated remainder bounds.
Substitution proves
\[
{S_{MM}\over D_M}=4-{4\over r}+{9\over r^2}+O(r^{-3}),
\]
\[
{S_{ML}\over D_M}=8+{32\over r}-{111\over2r^2}
+O(r^{-3}),
\qquad
{S_{LL}\over D_M}={4\over r}+{96\over r^2}+O(r^{-3}),
\]
and hence the displayed expansion for \(S(e)\).

### Path localization, maximum codegree, and the first bite

The containment pairs in (P2) form the reconstructed alternating path and
number \(4r-1\).  In the full middle cyclic deck, disjointness joins
successive windows in the odd-graph cyclic order; deleting \(M_0\) leaves
a path of \(2r-1\) edges.  The two skeleton masses, obtained from the
\(ML,a=r-1\) and \(MM,a=0\) rows of (P2), sum to
\[
{(2r-1)^2\over r(r+1)}
+{(4r-1)^2\over2r^2}
=12-{12\over r}+{19\over2r^2}+O(r^{-3}).
\]
Subtracting from (P3)--(P5) leaves
\[
{44\over r}+{40\over r^2}+O(r^{-3})
\]
of normalized off-skeleton mass.  The successive factorial ratios in the
MM, LL, and proper-ML rows are, respectively,
\[
{(a+1)(a+2)\over(r-a)^2},\qquad
{(a+1)(a+4)\over(r-1-a)^2},\qquad
{(a+1)(a+3)\over(r-a)(r-1-a)}.
\]
Each is increasing in \(a\), so every row maximum occurs at an endpoint.
Substitution shows that every off-skeleton pair has codegree
\(O(D_M/r^2)\).  For \(r\ge3\), the largest pair codegree is the
containment value
\[
\Delta_2=(4r-1)(r-1)!(r+1)!,
\qquad
{\Delta_2\over D_L}={4r-1\over2r(r+2)},
\]
so \(4r\Delta_2/D_L\to8\).
For \(r=2\), the disjoint LL pair is the finite exceptional maximum; it
does not affect the asymptotic statement.

For the bite calculation, let \(C(e)\) be the number of other
configurations meeting \(e\), and put
\[
A(e)=\sum_{v\in e}(d(v)-1)=2r(D_M+D_L)-4r.
\]
For \(F\ne e\), \(t_F-1\le\binom{t_F}2\), so
\[
A(e)-\left(S(e)-\binom{4r}2\right)
\le C(e)\le A(e).
\]
Thus
\[
C(e)=4(r+1)D_M(1+O(1/r)).
\]
If configurations are marked independently with
\(p=\gamma/(rD_M)\), a fixed marked configuration is isolated with
probability
\[
(1-p)^{C(e)}=\exp(-4\gamma+o(1)).
\]
Isolated marked configurations form a matching.  Multiplying their
retention probability by \(D_M\) or \(D_L\) gives expected covered
fractions
\[
{\gamma e^{-4\gamma}+o(1)\over r},
\qquad
{r+2\over r}{\gamma e^{-4\gamma}+o(1)\over r},
\]
which proves the claimed calibrated first bite.

## Appendix C.9: Exact all-depth occurrence-capacity threshold

Put `b=2r+1`,

\[
 \mathcal M={ [b]\choose r},\qquad
 \mathcal L={ [b]\choose {r-1}},\qquad
 A=|\mathcal M|,\qquad B=A/b=\operatorname{Cat}_r,\qquad
 L=|\mathcal L|={r\over r+2}A.                    \tag{C.9.1}
\]

Let `P` be any matching of directed punctured configurations and write
`p=|P|`.  Since each configuration contains exactly `2r` lower targets,
there is a unique `x in [0,1]` such that

\[
                         2rp=(1-x)L.               \tag{C.9.2}
\]

For `1<=q<=r-1`, retain the same `2r` nonzero starts and form the indexed
occurrence multisets

\[
 \mathcal S_q^-(P)=\{I_{r-q}^w(s):E(w)\in P, s\ne0\},
\]
\[
 \mathcal S_q^+(P)=\{I_{r+1+q}^w(s):E(w)\in P, s\ne0\}.       \tag{C.9.3}
\]

Let \(\mathcal H_q^-\) and \(\mathcal H_q^+\) be the complements of those two supports in their full layers, put \(h_q^\pm=|\mathcal H_q^\pm|\), and set

\[
 B_q={b\choose {r-q}}={b\choose {r+1+q}}.          \tag{C.9.4}
\]

Every multiset in (C.9.3) has exactly `2rp=(1-x)L` indexed occurrences.
Its support can only be smaller.  Therefore, without any probabilistic or
order hypothesis,

\[
 \boxed{h_q^-,h_q^+\ge[B_q-(1-x)L]_+},             \tag{C.9.5}
\]

and hence

\[
 \boxed{
 \sum_{q=1}^H(h_q^-+h_q^+)
 \ge2\sum_{q=1}^H[B_q-(1-x)L]_+.}                 \tag{C.9.6}
\]

We now locate the exact scale of this rank-volume obstruction.  The ratio
has the product form

\[
 {B_q\over L}=\prod_{j=1}^{q-1}{r-j\over r+j+2}. \tag{C.9.7}
\]

Since

\[
 {r-j\over r+j+2}
 =1-{2j+2\over r+j+2}\ge1-{2j+2\over r},
\]

and `prod_j(1-u_j)>=1-sum_j u_j` for `0<=u_j<=1`,

\[
 \boxed{{B_q\over L}\ge1-{(q-1)(q+2)\over r}.}    \tag{C.9.8}
\]

Indeed, if the right side is nonpositive this is trivial; otherwise the
sum of the displayed `u_j` is below one, so every `u_j` lies in `[0,1]`
and the product inequality applies.

Assume `rx>=64` and set

\[
 Q=\min\left\{H,\left\lfloor{\sqrt{rx}\over4}\right\rfloor\right\}.
\]

For `q<=Q`,

\[
 {(q-1)(q+2)\over r}
 \le{x\over16}+{1\over2}\sqrt{x\over r}
 \le{x\over8},                                    \tag{C.9.9}
\]

where the last inequality uses `sqrt(x/r)=x/sqrt(rx)<=x/8`.
Equations (C.9.6)--(C.9.9) give

\[
 \sum_{q=1}^H(h_q^-+h_q^+)\ge {7\over4}xLQ.       \tag{C.9.10}
\]

If `H>=floor(sqrt(rx)/4)`, then `floor(sqrt(rx)/4)>=sqrt(rx)/8`, so

\[
 \boxed{
 \sum_{q=1}^H(h_q^-+h_q^+)
 \ge {7\over32}L\sqrt r\,x^{3/2}.}               \tag{C.9.11}
\]

Because `L/A=1-o(1)`, Gaussian-band aggregate holes can be `o(A)` only if

\[
                              \boxed{x=o(r^{-1/3}).} \tag{C.9.12}
\]

In particular, `x=r^{-alpha}(1+o(1))` with any fixed
`alpha<=1/3` fails (C.9.12) for
`H=ceil(sqrt(b log b))`.  For `alpha<1/3`, the lower bound divided by `A`
grows as `Omega(r^((1-3alpha)/2))`; at `alpha=1/3` it stays bounded below.

The exponent is sharp for raw occurrence capacity.  From
`1-u<=e^{-u}` and `r+j+2<=2(r+1)`, (C.9.7) also gives

\[
 {B_q\over L}
 \le\exp\left\{-{(q-1)(q+2)\over2(r+1)}\right\}. \tag{C.9.13}
\]

If `x<=1/2` and `B_q>(1-x)L`, then
`-log(1-x)<=2x` implies

\[
                         (q-1)(q+2)<4(r+1)x.       \tag{C.9.14}
\]

Thus only `O(1+sqrt(rx))` summands in (C.9.6) are positive, and each is at
most `xL`.  Consequently its rank-volume right side is

\[
 O\bigl(Ax(1+\sqrt{rx})\bigr)=o(A)                \tag{C.9.15}
\]

when `x=o(r^{-1/3})`.  This removes only the numerical obstruction; it does
not make repeated windows distinct.

Restoring the omitted start in every selected row does not change the
threshold.  The full rows have

\[
 bp=\left(1+{1\over2r}\right)(1-x)L              \tag{C.9.16}
\]

occurrences at every rank.  Their effective deficit from `L` is

\[
 x-{1-x\over2r}\ge {3x\over4}                    \tag{C.9.17}
\]

when `x>=2/r`.  If `x<2/r`, then already `x=o(r^{-1/3})`; otherwise, on
any subsequence contradicting (C.9.12), the effective deficit times `r`
tends to infinity and the proof of (C.9.11) applies with changed constants.

Finally, when `x>>r^{-1/3}`, repairing even this occurrence deficit by
adjoining full rows needs

\[
 \Omega(xL/b)=\Omega(x\operatorname{Cat}_r)       \tag{C.9.18}
\]

additional rows, because each adds only `b` occurrences at a depth and
`L/b=(1-o(1))Cat_r`.  The same order supplies enough *counts*, but it says
nothing about distinct targets, common depths, or legality.  Thus the
current direct route requires either descent below (C.9.12) or a separate
integral cover-down of the order (C.9.18).

## Appendix C.10: Exact positive cover-down and cheap rounding

Continue with Appendix C.9, put \(B=A/b=\operatorname{Cat}_r\), and let `Q` be its shallow cutoff.  Restoring the
one omitted start in every selected configuration changes the aggregate
hole count by at most `2Hp<=2HB=o(A)` when `H=o(b)`.  For the enrichment
estimate retain the punctured hole sets of Appendix C.9.  For a row `C`,
define its shallow score against those sets by

\[
 S_Q(C)=\sum_{q=1}^Q\sum_{s\in\mathbb Z_b}
 \left({\bf1}_{I_{r-q}^C(s)\in\mathcal H_q^-}
       +{\bf1}_{I_{r+1+q}^C(s)\in\mathcal H_q^+}\right).       \tag{C.10.1}
\]

If `s` added rows leave at most `epsilon A` aggregate shallow holes, every
repaired target is counted at least once on the right, so (C.9.10) gives

\[
 \boxed{\sum_CS_Q(C)\ge {7\over4}xLQ-\epsilon A.}              \tag{C.10.2}
\]

For `x=r^{-alpha}(1+o(1))`, `alpha<1/3`,
`Q=floor(sqrt(rx)/4)`, `epsilon=o(1)`, and `s<=KxB`, division by `s`, using
`xQ->infinity`, yields average score at least
`(7/(4K)+o(1))bQ`.  A uniform random row instead has exact mean

\[
 b\sum_{q\le Q}\left({h_q^-\over\binom b{r-q}}+
 {h_q^+\over\binom b{r+1+q}}\right)=O(xbQ)          \tag{C.10.3}
\]

when every displayed hole count is `O(xA)`.  Thus a minimal cover-down
requires a genuine `Omega(1/x)` enrichment in the joint nested hole flag;
a one-rank packing alone does not certify it.

For the positive-cover question, now let `mathcal H` be the restored,
shore-tagged hole universe and exclude base rows from the set `Omega` of
candidate cyclic rows.  For `T in mathcal H,C in Omega`, let `M_(T,C)` be
the tagged window incidence.  The exact fractional physical-row cover number is

\[
 \tau^*(\mathcal H)=\min\left\{\sum_Cy_C:y_C\ge0,
                  \ \sum_CM_{T,C}y_C\ge1\ (T\in\mathcal H)\right\}. \tag{C.10.4}
\]

Finite covering duality gives

\[
 \boxed{\tau^*(\mathcal H)=\max\left\{\sum_Tz_T:z_T\ge0,
                \ \sum_TM_{T,C}z_T\le1\ (C\in\Omega)\right\}.} \tag{C.10.5}
\]

For self-containment, weak duality follows by reversing the two finite
sums.  If a number below the primal optimum were larger than every dual
value, separate the vector `(1,t)` from the closed nonnegative cone
generated by the columns `(M_C,1)`, `(-e_T,0)`, and `(0,1)`.  The separating
vector can be written `(-z,lambda)` with `z>=0`, `lambda>=0`,
`M^Tz<=lambda 1`, and `sum z>lambda t`.  Every target lies in a row, so
`lambda=0` is impossible; division by `lambda` gives a dual value above
`t`, a contradiction.  This proves (C.10.5).

The positive fractional gate has a cheap integral rounding.  More generally,
let `mathcal H' subseteq mathcal H` omit at most `o(A)` exceptional holes,
and suppose (C.10.4) on `mathcal H'` has a feasible vector of mass `t`.
Select each distinct row independently with probability
`min(1,lambda y_C)`.  The expected selected count is at most `lambda t`.
For every `T in mathcal H'`, either an incident row is certain or

\[
 \Pr(T\hbox{ uncovered})\le
 \exp\{-\lambda\sum_CM_{T,C}y_C\}\le e^{-\lambda}.             \tag{C.10.6}
\]

Two applications of Markov give one outcome with at most `4lambda t` rows
and at most `4|mathcal H'|e^{-lambda}` uncovered members.  Consequently,

\[
 \boxed{\tau^*(\mathcal H')=O(xB)}                              \tag{C.10.7}
\]

is sufficient: with `lambda=3 log r` it produces
`O(x log r B)=o(B)` physical rows, adds `O(x log r A)=o(A)` occurrences at
each rank, and leaves only `o(A)` aggregate holes, including the exceptional
set.  Hence no Baranyai--Katona factor or disjoint integral rounding theorem
is needed after (C.10.7).

Equivalently, (C.10.7) asks for a distribution on rows which contains every
nonexceptional hole with probability `Omega(1/(xB))`.  A concrete sufficient
condition is a (possibly labelled) candidate family `mathcal C` with

\[
 d_{\mathcal C}(T):=|\{C\in\mathcal C:M_{T,C}=1\}|\ge D_0,
 \qquad {|\mathcal C|\over D_0}=O(xB),              \tag{C.10.8}
\]

outside `o(A)` holes: weight every candidate by `1/D_0` and apply the
preceding rounding to that nonexceptional universe.  Labelled duplicate
copies may be sampled independently and then coalesced; coverage is
unchanged and the number of physical rows can only decrease.  For the stopped
catalogue this is an all-depth external-window degree floor; Gate A's
maximum-degree cap does not imply it.

There is also a weaker long-arc interface.  For a cyclic interval `J` of
`L_0` starts, charge all tagged depth-`H` windows of a row `C` beginning in
`J`.  If `M=O(xA/L_0)` such arcs cover all but `o(A)` holes and their
underlying rows are distinct, promoting the arcs to their full rows leaves
the same holes and costs `Mb` occurrences per rank.  Thus

\[
 xb\ll L_0\le b                                      \tag{C.10.9}
\]

makes the promotion cost `o(A)`.  In particular `L_0=ceil(b sqrt x)` needs
only `O(sqrt x B)=o(B)` rows.  Gate B may therefore be closed either by the
positive fractional bound (C.10.7), by the external degree floor (C.10.8),
or by a covering long-flag-arc theorem; none is currently proved for the
actual stopped residual.

## Appendix C.11: Shallow external regularity and the survivor-catalogue no-go

Continue with \(b=2r+1\), \(A={b\choose r}\), \(B=A/b\), and \(L={b\choose r-1}\) from C.9. Put `k_q=r-q`, `B_q=binom(b,k_q)`, and, for a tagged lower `k_q`-set `T`
or complementary upper target, let `Omega_q(T)` be the directed punctured
configurations whose full cyclic row contains `T`.  A proper target has one
start in a fixed row, so

\[
 D_q=|\Omega_q(T)|=b\,k_q!(b-k_q)!={b\,b!\over B_q}.           \tag{C.11.1}
\]

Independently retain lower and middle targets with probabilities `x` and
`y>=x`.  If `C` is the surviving labelled catalogue, set
`Z=|C|`, `X_(q,T)=|C cap Omega_q(T)|`, and
`rho=x^(2r)y^(2r)`.  Exact counting gives

\[
 \mathbb EZ=b!\rho,\quad \mu_q:=\mathbb EX_{q,T}=D_q\rho,\quad
 {\mathbb EZ\over\mu_q}={B_q\over b},\quad
 \sum_TX_{q,T}=bZ.                                      \tag{C.11.2}
\]

We first prove the mixed-root estimate underlying concentration.  Fix a
configuration `F`, suppose `T` is its length-`k_q` full window, and let `S`
be a nonempty subfamily of the punctured central/lower targets of `F`.  On
the cut circle let `v_q(S)` be the number of distinct endpoints used by `T`
and `S`, and let `d_q(T,S)` count configurations containing `T` as a full
window and every member of `S` as a retained target.  Uniformly for
`2<=q<=sqrt(r)/4`,

\[
                  {d_q(T,S)\over D_q}\le C^{|S|}r^{2-v_q(S)}.  \tag{C.11.3}
\]

Here is the gap proof, including the growing-root point.  Anchor `T`; its
two gaps have sizes `r-q,r+1+q`.  After all boundaries of `S` are inserted,
let the positive elementary gaps be `g_1,...,g_v`, so `sum g_i=b` and
`g_i<=r+1+q`.  If `V` is the product of labelled Venn-cell factorials and
`G=prod g_i!`, the Venn-refinement injection used in Appendix C.7 remains
valid even when one Venn cell is a union of noncontiguous gaps:

\[
 \sum_{\sum p_H=p_C}\prod_{H\subset C}{|H|\choose p_H}
 ={n_C\choose p_C}.                                    \tag{C.11.4}
\]

Thus distinct-gap positional children are paid by their Venn choices.  If
both new cuts lie in an ordinary gap, the interval or its complement has
length in `{r-1,r,r+1,r+2}`, leaving at most three outside positions and
cost at most eight.  In a root-descended gap `g>=r-1`, write its three
pieces as `u,m,w` and `d=u+w<=q+2`.  Summing all `d+1` positional splits,
including coincident endpoints, leaves the exact factor

\[
 {d+1\over{g\choose d}}\le
 \begin{cases}1,&d=0,\\4/r,&d=1,\\16/r^2,&d\ge2.
 \end{cases}                                           \tag{C.11.5}
\]

After the first central interval is fixed, every further one has at most
four starts with its prescribed intersection with that anchor.  Induction
over the exposure tree using (C.11.4)--(C.11.5) therefore pays one factor
`r^-1` for every new boundary cut.  Finally factorial log-convexity gives

\[
 {G\over(r-q)!(r+1+q)!}\le C^v r^{2-v}:               \tag{C.11.6}
\]

for `v<=r-q+1` the maximizing product is at most
`(r+1+q)!(r-q-v+2)!`, and beyond that point it is at most
`(b-v+1)!`; `(n)_j>=(n/e)^j` proves both bounds.  There are at most four
orientation/layer choices per exposed interval, absorbed into `C^|S|`.
Multiplying by the `b` possible starts of `T` and dividing by (C.11.1)
proves (C.11.3).

The punctured boundary graph has maximum degree four, is triangle-free for
large `r`, and every `m`-edge subgraph with `v` nonisolated vertices obeys
`m<=2(v-1)`.  Connected-subgraph exploration, separating components which
meet the two endpoints of the external root, consequently gives, for
`0<=z<=c sqrt(r)`,

\[
 \sum_{\varnothing\ne S\subseteq F}z^{|S|}r^{2-v_q(S)}
 =O\left({z\over r}+{z^3\over r}+{z^4\over r^2}\right).       \tag{C.11.7}
\]

Indeed unrooted components have total activity
`O(z/r+z^4/r^2)`; a component meeting a prescribed root endpoint has
activity `O(z/r+z^2/r^2+z^3/r+z^4/r^2)`, and dropping mutual disjointness
multiplies by the exponential of the unrooted activity.

Put `a=x^-1-1`.  The covariance ratio is at most
\[
 x^{-|F\cap G|}-1=\sum_{\varnothing\ne S\subseteq F\cap G}a^{|S|}.
\]
Using (C.11.3)--(C.11.7) therefore proves uniformly for
`x>=r^-alpha`, `alpha<1/3`, and `2<=q<=sqrt(r)/4`,

\[
 {\operatorname {Var}X_{q,T}\over\mu_q^2}
 \le{1\over\mu_q}+O\left({1\over rx^3}\right)=o(1).          \tag{C.11.8}
\]

If instead each shore is a uniform subset of its prescribed size, every
union of two configurations has at most `4r` variables per shore and
`(m)_u/(N)_u=(m/N)^u exp(O(u^2/m)+O(u^2/N))`.  Since the shore sizes are
exponential, the normalized variance in (C.11.8) changes by only
`e^-Omega(r)`.  Exact shore sizes therefore do not create positive external
bias.

This implies the promised no-go.  Assume `x=o(1)`, `x>=r^-alpha` for one fixed `alpha<1/6`, put
`Q=floor(sqrt(rx)/4)`, and let possibly residual-dependent tagged hole sets
satisfy

\[
 \sum_{q=2}^Q(|\mathcal H_q^-|+|\mathcal H_q^+|)\ge c_0xAQ.  \tag{C.11.9}
\]

With high probability there are no `D_0>0` and exceptional `o(A)` targets
for which all remaining holes have `X_(q,T)>=D_0` and

\[
                              {Z\over D_0}=O(xB).               \tag{C.11.10}
\]

To prove it, the product-law unrooted concentration (C.3bis.11) with \(s=1\) first gives
\(Z\ge\mathbb EZ/4\) with high probability.  Since
`B_q/L>=1-(q-1)(q+2)/r>=1-x/8`, (C.11.10) would make every
nonexceptional hole satisfy `X_(q,T)>=c mu_q/x`.  Chebyshev and (C.11.8)
show that a fixed target has this enrichment with probability
`O(1/(rx))`.  Among at most `2QA` tagged targets the expected enriched
count is `O(QA/(rx))`; because `rx^2->infinity`, Markov makes this
`o(xAQ)`.  Also `xQ->infinity`, so an `o(A)` exception removes only
`o(xAQ)` holes, contradicting (C.11.9).

Finally, ordinary external regularity is incompatible even with the actual
stopped descent.  At a good round `j`, let `Z_j` be the current catalogue,
`M_j` its middle shore, and mark with
`p_j=gamma|M_j|/(2r^2Z_j)`.  If for one depth `q`, throughout every good
trajectory,

\[
 X_{q,j}(T)\le K_E{bZ_j\over B_q},\quad B_q\ge c_BA,\quad
 p_j\le\tfrac12,\quad \sum_{j<\tau}{|M_j|\over A}\le C_0r,  \tag{C.11.11}
\]

then each tagged `T` has a constant probability of either seeing a declared
failure or remaining a full-bank hole at the threshold.  Indeed

\[
 \sum_{j<\tau}p_jX_{q,j}(T)\le{\gamma K_EC_0b\over2c_Br}=O(1). \tag{C.11.12}
\]

Conditionally, no member of the external star is marked with probability
`(1-p_j)^(X_(q,j)(T))>=exp(-2p_jX_(q,j)(T))`.  Formally, if `A_j` is the
event of no earlier external mark and
`Lambda_j=sum_(i<j)p_iX_(q,i)(T)`, then
`1_(A_j)exp(2Lambda_j)` stopped at `tau` is a nonnegative submartingale.
Equation (C.11.12) therefore gives `Pr(A_tau)>=exp(-O(1))` without
conditioning on future cap persistence.
On that event either failure occurs or no accepted row covers `T`.  Hence,
if failures are `o(1)`, an all-target cap (C.11.11) forces
`mathbb E(h_q^++h_q^-)=Omega(A)`, far above `O(xA)`.  The exact positive Gate-B
input is therefore a history-induced alignment of `Omega(xAQ)` holes with
an external high-degree tail of factor `1/x`, a hole-biased subcatalogue,
or the separate constant-density long-flag-arc tail.

## Appendix C.13: Stopped external hits and relative protection

Let \(\mathcal C_j\) be the residual labelled configuration catalogue before
round \(j\), \(Z_j=|\mathcal C_j|\), and \(G_j\) its conflict graph.
Conditionally on \(\mathcal F_j\), mark each configuration with probability
\(p_j\), accept the isolated marks \(\mathcal A_j\), and delete their closed
conflict neighbourhoods.  All stopping times below are bounded by the deterministic round cap. Fix a positive terminal density scale \(x\), put \(Q=\lfloor\sqrt{rx}/4\rfloor\), and use this \(Q\) for the aggregate shallow-depth statements.

Fix a tagged shallow depth \(q\), put

\[
 b=2r+1,\quad A={b\choose r},\quad B=A/b,\quad
 k_q=r-q,\quad B_q={b\choose{k_q}},
\]

and use restored full rows.  For a target \(T\), define

\[
 \mathcal S_j(T)=\{F\in\mathcal C_j:T\hbox{ is a full-row window of }F\},
 \qquad X_j(T)=|\mathcal S_j(T)|.                  \tag{C.13.1}
\]

Every configuration has \(b\) such windows, so

\[
 \sum_TX_j(T)=bZ_j.                                \tag{C.13.2}
\]

Initially

\[
 Z_0=b!,\qquad X_0(T)=D_q=b\,k_q!(b-k_q)!,
 \qquad {X_0(T)\over Z_0}={b\over B_q}.            \tag{C.13.3}
\]

Let \(U_j(T)\) indicate that no earlier accepted full row contains \(T\), and put \(h_q(n)=\sum_TU_n(T)\) over the shore-tagged depth-\(q\) layer (rank \(r-q\) or \(r+1+q\)).
Thus \(U_\tau(T)=1\) precisely for a restored terminal hole.  Returning to
the punctured convention changes at most one occurrence per accepted row
and depth, hence \(O(QB)=o(A)\) aggregate targets when \(Q=o(b)\).

For one round put

\[
 K_j(T)=|\mathcal A_j\cap\mathcal S_j(T)|,\qquad
 a_j(T)=\Pr(K_j(T)>0\mid\mathcal F_j),\qquad
 u_j(T)=p_jX_j(T).                                 \tag{C.13.4}
\]

If \(p_j\le1/2\) and \(p_j\Delta(G_j)\le\beta\), then

\[
 \boxed{e^{-4\beta}{u_j(T)\over1+u_j(T)}
 \le a_j(T)\le\min\{1,u_j(T)\}.}                  \tag{C.13.5}
\]

Indeed, if \(I_F\) indicates that \(F\in\mathcal S_j(T)\) is an isolated
mark, then

\[
 \lambda=\mathbb E(K_j(T)\mid\mathcal F_j)
 =\sum_{F\in\mathcal S_j(T)}p_j(1-p_j)^{\deg_{G_j}(F)}
\]

lies between \(e^{-2\beta}u_j(T)\) and \(u_j(T)\).  Conflicting
configurations cannot both be isolated, while a nonconflicting pair is
simultaneously isolated with probability at most \(p_j^2\).  Hence
\(\mathbb EK_j(T)^2\le\lambda+u_j(T)^2\).  The second-moment inequality
gives the lower bound in (C.13.5), and the union bound gives the upper.

There are two exact stopped likelihoods.  For every fixed \(T\),

\[
 \boxed{U_n(T)+\sum_{j<n}U_j(T)a_j(T)}             \tag{C.13.6}
\]

is a martingale.  If \(p_j<1\) whenever \(Z_j>0\), then so is

\[
 \boxed{U_n(T)\exp\!\left\{\sum_{j<n}-\log(1-a_j(T))\right\}.} \tag{C.13.7}
\]

The condition ensures \(a_j(T)<1\): the event that nothing is marked has
positive probability.  On \(U_j(T)=1\), the next indicator is zero exactly
when \(K_j(T)>0\), which proves (C.13.6); multiplication by
\((1-a_j(T))^{-1}\) proves (C.13.7).  Optional stopping yields

\[
 \Pr\!\left(U_\tau(T)=1,\;
 \sum_{j<\tau}-\log(1-a_j(T))\ge s\right)\le e^{-s},            \tag{C.13.8}
\]

and, after summing (C.13.6) over \(T\),

\[
 \mathbb Eh_q(\tau)
 =B_q-\mathbb E\sum_{j<\tau}\sum_TU_j(T)a_j(T).    \tag{C.13.9}
\]

Thus (C.13.5) applies to targets unhit at the current time; replacing
\(U_j\) by the future event \(U_\tau\) would be invalid conditioning.

There is also an exact no-mark likelihood.  Let \(V_j(T)\) indicate that
no member of any successive external star of \(T\) has yet been marked, and
put

\[
 L_n(T)=\sum_{j<n}-X_j(T)\log(1-p_j).
\]

Then

\[
 \boxed{V_n(T)e^{L_n(T)}}                          \tag{C.13.10}
\]

is a nonnegative martingale: conditional on \(V_j(T)=1\), the next
no-mark probability is exactly \((1-p_j)^{X_j(T)}\).  Consequently

\[
 \Pr(V_\tau(T)=1,\ L_\tau(T)\ge s)\le e^{-s},\qquad
 V_\tau(T)\le U_\tau(T).                           \tag{C.13.11}
\]

In particular a pathwise bound \(L_\tau(T)\le\Lambda\) on all no-mark
paths implies \(\Pr(U_\tau(T)=1)\ge e^{-\Lambda}\).  An average bound
selected only after the final holes are known does not imply this.

Assume now that \(Z_j>0\) through \(\tau\), as on every good stopped
trajectory.  Define

\[
 d_j=1-{Z_{j+1}\over Z_j},\qquad
 d_j(T)=1-{X_{j+1}(T)\over X_j(T)}                 \tag{C.13.12}
\]

when \(X_j(T)>0\).  If a star becomes empty, assign all later protection
values \(-\infty\).  Otherwise put

\[
 \mathscr P_\tau(T)=\sum_{j<\tau}
 \log{1-d_j(T)\over1-d_j},\qquad
 \pi_j(T)={X_j(T)\over bZ_j}.                      \tag{C.13.13}
\]

Equation (C.13.2) makes \(\pi_j\) a probability law.  Direct substitution
and a second use of (C.13.2) give the exact replicator identities

\[
 \boxed{\pi_{j+1}(T)=\pi_j(T){1-d_j(T)\over1-d_j},\qquad
 \sum_T\pi_j(T)(d_j-d_j(T))=0.}                   \tag{C.13.14}
\]

The second equality is linear.  The logarithmic increment instead has
nonpositive Palm mean by Jensen:

\[
 \sum_T\pi_j(T)\log{1-d_j(T)\over1-d_j}\le0.       \tag{C.13.15}
\]

Telescoping (C.13.12)--(C.13.13) and using (C.13.3) proves

\[
 \boxed{{X_\tau(T)\over Z_\tau}
 ={b\over B_q}e^{\mathscr P_\tau(T)}}              \tag{C.13.16}
\]

for every nonempty terminal star.  Give each terminal survivor the common
weight \(KxB/Z_\tau\).  Its total mass is \(KxB\), and it covers \(T\) to
level one exactly when

\[
 \boxed{\mathscr P_\tau(T)\ge
 \log{B_q\over Kx\,bB}=\log{B_q\over KxA}.}        \tag{C.13.17}
\]

For \(q\le\sqrt{rx}/4\), (C.9.8) gives \(B_q/A=1-O(x)\), so the threshold
is \(\log(1/x)-O_K(1)\).

The full-catalogue Gate-B criterion is therefore pathwise:

\[
 \left|\left\{T\in\mathcal H:
 \mathscr P_\tau(T)<\log{B_{\operatorname{depth}(T)}\over KxA}\right\}\right|=o(A),
                                                               \tag{C.13.18}
\]

where \(\mathcal H\) is the restored tagged hole universe and \(\operatorname{depth}(T)\) is the unique \(q\) for which \(T\) belongs to its shore-tagged depth-\(q\) layer.  This is
equivalent to uniform terminal-survivor weight covering every other hole.
Moreover, iteration of (C.13.14) from
\(\pi_0(T)=1/B_q\) gives

\[
 \boxed{\sum_Te^{\mathscr P_\tau(T)}=B_q,\qquad
 |\{T:\mathscr P_\tau(T)\ge s\}|\le B_qe^{-s}.}    \tag{C.13.19}
\]

Empty stars contribute zero.  At the threshold (C.13.17), the upper tail
has size at most \(KxA\).  On the other hand, C.9.5 supplies
\(\Omega(xA)\) holes at every capacity-forcing shallow rank.  Thus a
successful theorem must align essentially the whole capacity-sized
protection tail with the holes; a marginal tail on arbitrary targets is
insufficient.

Finally, the protection has an exact first-blocker form.  In round \(j\),
order \(\mathcal A_j\) deterministically and assign every deleted
configuration to the first accepted configuration whose closed
neighbourhood deletes it.  Let \(\mathcal B_j(G)\) be the resulting cell.
The cells partition \(\mathcal C_j-\mathcal C_{j+1}\), so

\[
 Z_jd_j=\sum_{G\in\mathcal A_j}|\mathcal B_j(G)|,\qquad
 X_j(T)d_j(T)=\sum_{G\in\mathcal A_j}
 |\mathcal B_j(G)\cap\mathcal S_j(T)|.             \tag{C.13.20}
\]

For a terminal hole no accepted \(G\) belongs to \(\mathcal S_j(T)\).
Thus (C.13.18) is exactly the lower-tail assertion obtained by substituting
(C.13.20) into

\[
 \sum_{j<\tau}\log
 {1-\sum_G|\mathcal B_j(G)\cap\mathcal S_j(T)|/X_j(T)
  \over
  1-\sum_G|\mathcal B_j(G)|/Z_j}.                  \tag{C.13.21}
\]

On a good trajectory \(d_j\le1/8\).  Any target satisfying
(C.13.17) necessarily obeys the additive obstruction

\[
 \boxed{\sum_{j<\tau}(d_j-d_j(T))_+
 \ge {7\over8}\left(\log{B_q\over KxA}\right)_+.} \tag{C.13.22}
\]

Indeed, a round with \(d_j(T)\ge d_j\) contributes nonpositively, while
for \(d_j(T)<d_j\le1/8\),

\[
 \log{1-d_j(T)\over1-d_j}
 =\int_{d_j(T)}^{d_j}{du\over1-u}
 \le {8\over7}(d_j-d_j(T)).
\]

Equations (C.13.20)--(C.13.22) isolate the remaining positive theorem:
the actual terminal holes must cumulatively receive logarithmically less
outside-blocker loss than the whole catalogue while simultaneously avoiding
every accepted hit.  None of the identities above proves that alignment.

# Appendix G: Gate A—stopped tail transfer and connected carriers

Let a finite simple hypergraph have shores \(V_\sigma\), every edge meeting
shore \(\sigma\) in \(k_\sigma\) vertices.  Write

\[
 Z=|E|,\qquad n_\sigma=|V_\sigma|,\qquad
 z_\sigma={k_\sigma Z\over n_\sigma},\qquad d(v)=|\{F:v\in F\}|.
\]

For an edge \(F\), put

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad C_F=|\Gamma(F)|.
\]

For \(v\notin G\), also put

\[
 a_G(v)=|\{F:v\in F,\ F\cap G\ne\varnothing\}|,\qquad
 E_v={1\over d(v)}\sum_{F\ni v}(C_F-d(v)),\qquad
 \bar C={1\over Z}\sum_FC_F.
\]

Swapping the two finite sums gives
\(\sum_{G\not\ni v}a_G(v)=d(v)E_v\).  In the punctured application
\(k_M=k_L=2r\).  All laws below are stopped
before a displayed cap, shore-comparability condition, or degree floor
fails.  No assertion conditions on a future persistence event.

The cap alone cannot propagate itself in a general hypergraph.  Take the
disjoint union of the Fano plane and \(K_4^{(3)}\).  Initially every vertex
has degree three.  If exactly one Fano edge and no other edge is marked,
that edge is isolated; deleting its vertices destroys all seven Fano edges.
The residual has four zero-degree Fano vertices and four degree-three
\(K_4^{(3)}\) vertices, so its average degree is \(3/2\), its maximum is
three, and the maximum/average ratio jumps from one to two.  This event has
positive probability.  A Gate-A proof must therefore use punctured
interval geometry, not the degree cap alone.

## G.1 Exact Palm recursion, finite bites, and exact-slice mixtures

The purpose of this section is to connect the stopped target G.2 to the product-reference
objects in G.14, G.15, G.18, and G.19.  It contains no unproved mixing assertion.

Fix a shore `V` in a finite simple hypergraph state `H`, and fix an integer
`m>=2` (Gate A uses `m=12`).  A rooted ordered carrier is

\[
 \gamma=(v;F_1,\ldots,F_m),\qquad
 v\in V,\quad F_i\ne F_j,\quad v\in F_i.
\]

For a residual state `S`, write `d_S(v)` for the root degree and put

\[
 t(S)=\sum_{v\in V}(d_S(v))_m,
 \qquad F_c(S)=\sum_{v\in V}(d_S(v)-c)_+^m,
\]
\[
 \varphi_c(d)=
 \begin{cases}(d-c)_+^m/(d)_m,&d\ge m,\\0,&d<m,
 \end{cases}
 \qquad c\ge m-1.                                      \tag{G.1.1}
\]

For a nonzero finite measure `nu` on residual states with `nu(t)>0`, its
carrier Palm law is

\[
 \widehat\nu(S,\gamma)=
 {\nu(S){\bf1}_{\{\gamma\text{ alive in }S\}}\over\nu(t)}.
\]

Counting the `(d_S(v))_m` ordered carriers at each root gives the exact
identity

\[
 A_c(\nu):={\nu(F_c)\over\nu(t)}
           =\mathbb E_{\widehat\nu}\varphi_c(d_S(v)).       \tag{G.1.2}
\]

Let `P` be any deletion-only sub-Markov kernel, including a stopping
indicator.  For a current carrier state `x=(S,gamma)`, define

\[
 a(x)=\sum_{S'}P(S,S')\mathbf1_{\{\gamma\text{ alive in }S'\}},
\]
\[
 e_c(x)=\sum_{S'}P(S,S')\mathbf1_{\{\gamma\text{ alive in }S'\}}
       \{\varphi_c(d_S(v))-\varphi_c(d_{S'}(v))\}.          \tag{G.1.3}
\]

Whenever both carrier masses are positive,

\[
 \boxed{A_c(\nu P)=
 {\mathbb E_{\widehat\nu}[a\varphi_c-e_c]
       \over\mathbb E_{\widehat\nu}a}},                  \tag{G.1.4}
\]
and therefore

\[
 \boxed{A_c(\nu P)-A_c(\nu)=
 {\operatorname {Cov}_{\widehat\nu}(a,\varphi_c)
       -\mathbb E_{\widehat\nu}e_c
       \over\mathbb E_{\widehat\nu}a}.}                  \tag{G.1.5}
\]

Indeed, terminal alive carriers have unique labelled parents, so the
terminal carrier mass divided by the initial carrier mass is `E a`.
Summing the terminal test over those carriers gives
`E(a varphi_c-e_c)`, which proves (G.1.4); centering proves (G.1.5).

The erosion term is nonnegative.  For `d>c`,

\[
 {\varphi_c(d+1)\over\varphi_c(d)}
 =\left(1+{1\over d-c}\right)^m{d-m+1\over d+1}\ge1,       \tag{G.1.6}
\]

because Bernoulli's inequality and `c>=m-1` give
`(1+1/(d-c))^m >= 1+m/(d-m+1)=(d+1)/(d-m+1)`.
Deletion cannot increase `d`, hence `e_c>=0`.  Thus survival selection is
the only sign-indefinite term in (G.1.5).

For a reference pair `(lambda,U)`, define `Delta` and `Delta^0` to be the
right side of (G.1.5) for `(nu,P)` and `(lambda,U)`, respectively, before
adding `A_c` itself.  If the four adjacent scalars are positive, then

\[
 {A_c(\nu P)/A_c(\lambda U)\over A_c(\nu)/A_c(\lambda)}
 ={1+\Delta/A_c(\nu)\over1+\Delta^0/A_c(\lambda)}.          \tag{G.1.7}
\]

Consequently, for a fixed terminal cutoff `c`, put
\(A_{j,c}=A_c(\nu_j)\) and \(B_{j,c}=A_c(\lambda_j)\).  Iteration is
exact:

\[
 \log{A_c(\nu_J)\over A_c(\lambda_J)}
 =\log{A_c(\nu_0)\over A_c(\lambda_0)}
 +\sum_{j<J}\left[
  \log\!\left(1+{\Delta_{j,c}\over A_{j,c}}\right)
 -\log\!\left(1+{\Delta^0_{j,c}\over B_{j,c}}\right)
 \right].                                                  \tag{G.1.8}
\]

Zero reference tail is harmless: full support and nonnegativity make
`F_c` identically zero on that reference slice.  Formula (G.1.8), with one
fixed `c` while telescoping backward, is the exact stopped scalar
comparison; it neither assumes nor requires full-state likelihood
domination.

We next remove the infinitesimal-bite fiction.  In a deterministic state
put

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad
 B(\gamma)=\bigcup_{i=1}^m\Gamma(F_i),\qquad
 h(\gamma)=|B(\gamma)|,
\]
\[
 \Delta_C=\max_F|\Gamma(F)|.
\]

Mark every row independently with probability `p` and accept exactly the
isolated marks.  If `a_p(gamma)` is the probability that the carrier
survives, then

\[
 \boxed{a_p(\gamma)=1-ph(\gamma)+r_p(\gamma),\qquad
 0\le r_p(\gamma)\le\left({m^2\over2}+m\right)
                         (p\Delta_C)^2.}                    \tag{G.1.9}
\]

If no member of `B(gamma)` is marked, the carrier survives, and
`0<=(1-p)^h-(1-ph)<=binom(h,2)p^2`.  Any additional survival has a marked
row in `B(gamma)` that is rejected by a distinct marked conflict
neighbour.  The ordered-pair union bound is at most
`p^2 h Delta_C`; since `h<=m Delta_C`, (G.1.9) follows.

Let `Delta` bound `Delta_C` on the support of the current law and assume
`p Delta` is a sufficiently small constant.  Substitution of (G.1.9) in
(G.1.5), use of `e_c>=0`, and
`|Cov(r_p,varphi_c)|<=2||r_p||_infty A_c` give

\[
 \boxed{
 \log{A_c(\nu P_p)\over A_c(\nu)}
 \le -p{\operatorname {Cov}_{\widehat\nu}(h,\varphi_c)
             \over A_c(\nu)}+C_m(p\Delta)^2.}              \tag{G.1.10}
\]

If \(p_j\Delta_j\le C\varepsilon\) for every microbite and their number is
at most \(C r\log r/\varepsilon\), then

\[
 \sum_j(p_j\Delta_j)^2=O(\varepsilon r\log r)
                        =o(r^{-1-\alpha}).                  \tag{G.1.11}
\]

The last equality holds under
\(\varepsilon=o(r^{-2-\alpha}/\log r)\).  More generally the exact
finite-bite budget is \(\sum_j(p_j\Delta_j)^2\); no constant-rate or
stopped-mixing assertion is hidden here.

The actual clock may choose its marking probability predictably from the
current state.  If the state is \(S\), write \(p=p(S)\), put

\[
 \theta=\sup_Sp(S)\Delta_C(S),\qquad
 s(S,\gamma)=p(S)h(S,\gamma),                              \tag{G.1.11a}
\]

and assume \(\theta\) is a sufficiently small constant depending only on
\(m\).  Applying (G.1.9) conditionally on \(S\) gives
\(a=1-s+r\), \(0\le r\le C_m\theta^2\).  Repeating the proof of
(G.1.10), without taking \(p\) outside the Palm expectation, yields

\[
 \boxed{
 \log{A_c(\nu P_{p(\cdot)})\over A_c(\nu)}
 \le-{\operatorname {Cov}_{\widehat\nu}(s,\varphi_c)
              \over A_c(\nu)}+C_m\theta^2.}                 \tag{G.1.11b}
\]

Thus the live regression variable is the weighted hazard \(p(S)h\), not
the unweighted hazard with \(p\) replaced by a constant.  In particular,
conditioning first on the root degree gives the literal profile
\(\zeta_s(d)=\mathbb E_{\widehat\nu}[p(S)h\mid d_S(v)=d]\).
Along a varying schedule, its remainder is the sum of the corresponding
\(\theta_j^2\).

Finally, exact shore sizes introduce no fibre-probability penalty.  Let
`N_j` be the vector of actual shore sizes with law `w_j`, let
`lambda_n` be uniform on the slice of size vector `n`, and put

\[
 \Lambda_j=\sum_nw_j(n)\lambda_n.
\]

If `kappa_j(n,n')` is the actual joint law of successive size vectors and
`K_j(n,n')=kappa_j(n,n')/w_j(n)`, define, for `S` in the `n`-slice,

\[
 U_j(S,S')=\sum_{n'\le n}K_j(n,n')
 {\mathbf1_{\{S'\subseteq S,\ |S'|=n'\}}
       \over\prod_\sigma {n_\sigma\choose n'_\sigma}}.     \tag{G.1.12}
\]

Double counting nested pairs proves

\[
                         \boxed{\Lambda_jU_j=\Lambda_{j+1}.} \tag{G.1.13}
\]

Moreover, for nonnegative observables `F,t`, with `F=0` on every
positive-mass zero-`t` fibre,

\[
 {\mathbb E_{\Lambda_j}F\over\mathbb E_{\Lambda_j}t}
 \le\sup_{n:w_j(n)\mathbb E_{\lambda_n}t>0}
 {\mathbb E_{\lambda_n}F\over\mathbb E_{\lambda_n}t}.     \tag{G.1.14}
\]

This is just a weighted average of the fibrewise ratios with weights
`w_j(n) E_(lambda_n)t`.  Hence every uniform exact-slice estimate in a
density bin passes to the random-size reference mixture without division
by a small size probability.

For completeness, let \(r_\sigma\in\{0,1\}\) indicate whether the carrier
root lies on shore \(\sigma\).  If a carrier footprint uses
\(b_{\gamma,\sigma}\) nonroot targets on that shore, then, conditional on
retaining the root target, the exact nested-slice survival factor is

\[
 \prod_\sigma{(n'_\sigma-r_\sigma)_{b_{\gamma,\sigma}}
                   \over(n_\sigma-r_\sigma)_{b_{\gamma,\sigma}}}.
                                                                  \tag{G.1.15}
\]

Without conditioning on the root, multiply (G.1.15) by the common factor
\(\prod_\sigma(n'_\sigma/n_\sigma)^{r_\sigma}\).  For a fixed root shore
this factor is independent of the carrier label and cancels from every
Palm ratio used here.

Put \(N_\sigma=n_\sigma-r_\sigma\) and
\(N'_\sigma=n'_\sigma-r_\sigma\).  When
\(\delta_\sigma=1-N'_\sigma/N_\sigma\le1/4\) and
\(b_{\gamma,\sigma}\le N_\sigma/2\), termwise expansion of
\(\log(1-z)\) gives

\[
 \log{(N'_\sigma)_{b_{\gamma,\sigma}}
             \over(N_\sigma)_{b_{\gamma,\sigma}}}
 =-b_{\gamma,\sigma}\delta_\sigma
 +O\!\left(b_{\gamma,\sigma}\delta_\sigma^2+
   {b_{\gamma,\sigma}^2\delta_\sigma\over N_\sigma}\right).
 \tag{G.1.16}
\]

The logarithm of (G.1.15) is the sum of (G.1.16) over the shores.

At the punctured scale \(b_{\gamma,\sigma}=O_m(r)\), shore sizes are
exponential, and \(\delta_\sigma=O(\varepsilon/r)\), so (G.1.16) is
\(O_m(\varepsilon)\), while its displayed remainder is
\(O_m(\varepsilon^2/r)+e^{-\Omega(r)}\). Accepted-count concentration is
the separate theorem in Appendix C.5.

Equations (G.1.2)--(G.1.16) are the exact finite-bite and slice bridge used by the stopped target G.2.  Under the
independent product reference, conditioning on a fixed labelled carrier
leaves independent target indicators.  Both its live conflict hazard `h`
and the degree-tail test are increasing, so Harris association makes the
within-carrier covariance favorable.  The only possible adverse reference
term is therefore the between-carrier covariance.  G.14 rewrites that
term as the tail tilt of the signed connected statistic
`q_0 Xi_gamma^circ`; G.15 decomposes it into carrier U-statistics; G.18
gives the exact two-shore cell determinant for `s=2`; and G.19 localizes
the factorial pair law.  What remains open is exactly:

1. cutoff-tail leakage and kernel-weighted uniform integrability outside
   the disjoint overlap cell;
2. the signed dominant-cell determinant and the signed `s=3,...,12`
   remainder;
3. the stopped twelfth-moment comparison (G.29), with
   \(\kappa<2-20\alpha\) for the present shore ledger; and
4. actual/reference survival-payoff and realized-center comparison, plus
   the purge/cemetery ledger, within the exponent budget of G.2.

## G.2 Product high moments and the exact stopped target

The following reference-law estimate is proved; its adaptive stopped
analogue is not.

For a fixed even \(m=2s\), the rooted component expansion from
C.3--C.3bis gives, at a product reference checkpoint,

\[
 {\mathbb E(X_v-\mu)^m\over\mu^m}
 \le C_m\!\!\sum_{\sum jn_j=m}R_1^{n_2}
       \prod_{j=3}^m Q_{j/2}^{(j-1)n_j}+e^{-\Omega(r)},       \tag{G.21}
\]

where
\(R_c,Q_c=O_c(r^{-1}x^{-3c}+r^{-2}x^{-4c})\).  To see (G.21), expand the
centered indicators of the incident configurations.  A dependency
component of size two costs \(R_1\); a component of size \(j\ge3\) is
controlled as follows. Give pair \(ab\) weight \(t_{ab}\). A uniform spanning tree contains each pair with probability \(2/j\), so a maximum-weight tree \(T\) satisfies \(\sum_{a<b}t_{ab}\le(j/2)\sum_{ab\in T}t_{ab}\). Connectedness lets \(T\) use only positive-overlap edges. Therefore \(x^{-\sum t_{ab}}\le\prod_{ab\in T}\mathbf1_{\{t_{ab}>0\}}x^{-(j/2)t_{ab}}\); rooting the tree and summing its leaves costs \(Q_{j/2}^{j-1}\).
Singleton components vanish.  Repeated Bernoulli powers reduce to fewer
distinct centered indicators.  There are only \(j^{j-2}\) labelled trees.

When \(\alpha<1/(3m)\), every component in (G.21) is at most its Gaussian
pairing scale.  Indeed, relative to
\(\varrho^{j/2}\), \(\varrho=r^{-1}x^{-3}\), the first kernel monomial is
\(r^{1-j/2}x^{-3j(j-2)/2}\le1\), and selecting its second monomial costs
at most \(r^{-1}x^{-j/2}\le1\).  Writing \(U_m^{\rm ref}\) for the normalized central moment on the left of (G.21), we obtain

\[
 U_m^{\rm ref}=O_m((rx^3)^{-m/2})+e^{-\Omega(r)}.     \tag{G.22}
\]

Appendix C.3ter transfers (G.22) to uniform two-shore slices.  For the
actual process, on shore \(\sigma\) define
\[
 U_{12,aw_j}(H_j)=
 {1\over n_{j,\sigma}z_{j,\sigma}^{12}}
 \sum_{v:d_j(v)>a w_{j,\sigma}}
       |d_j(v)-z_{j,\sigma}|^{12},
\]
where \(n_{j,\sigma}=|V_\sigma(H_j)|\), \(d_j(v)\) is the degree of
\(v\) in \(H_j\), \(z_{j,\sigma}=n_{j,\sigma}^{-1}
\sum_{v\in V_\sigma(H_j)}d_j(v)\),
\(w_{j,\sigma}\) is a predictable shadow center, and \(a>1\) is fixed.
Stop before any cap, shore-comparability, degree-floor, or fixed
shadow-ratio bound fails.  For a fixed-ratio density bin
\([\xi_\ell,2\xi_\ell)\), let \(\mathcal G_{j,\ell}\) be the event that
round \(j\) precedes every stop and lies in that bin.

The exact missing stopped-law input is [O]:
\[
 \boxed{\mathbb E[U_{12,aw_j}(H_j)\mid\mathcal G_{j,\ell}]
 \le r^{\kappa+o(1)}(r\xi_\ell^3)^{-6}+e^{-\Omega(r)},
 \qquad \kappa<2-20\alpha.}                              \tag{G.29}
\]
It must be accompanied by finite-bite, realized-center, purge, and
accepted-count errors whose total is \(o(r^{-\alpha}/r)\).  These are
premises of a possible Gate-A closure, not conclusions of this section.
The product and exact-slice estimates do not imply (G.29).

## G.14 The exact punctured connected-carrier correction


For the complete directed-punctured catalogue under independent target
retention, the one-carrier conditional mean hazard is exactly constant.
Consequently every between-carrier Simpson contribution comes from a
genuinely connected correction involving at least two carrier rows and one
further catalogue row.

In a retained target state let $E(H)$ be the surviving catalogue rows,
$d_v=|\{G\in E(H):v\in G\}|$, and
$\Gamma_H(F)=\{G\in E(H):G\cap F\ne\varnothing\}$. For an ordered
$m$-carrier $\gamma=(v;F_1,\ldots,F_m)$ put
$h_\gamma=|\bigcup_i\Gamma_H(F_i)|$ and define the signed connected
statistic $\Xi_\gamma$ in (G.14.3.3) below. If

\[
 H_\gamma=\mathbb E[h_\gamma\mid\gamma\text{ retained}],
 \qquad
 P_\gamma=\mathbb E[\psi(d_v/c)\mid\gamma\text{ retained}], \tag{G.14.0.1}
\]

where $c>0$ is deterministic and $\psi$ is increasing, then

\[
 \boxed{
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\psi(d_v/c))
 =\mathbb E_\pi\operatorname {Cov}(h_\gamma,\psi(d_v/c)
                    \mid\gamma)
  +q_0\operatorname {Cov}_\pi(\Xi_\gamma,P_\gamma).}       \tag{G.14.0.2}
\]

The first term is nonnegative by Harris/FKG.  Thus, if
$d\tau/d\pi=P_\gamma/\mathbb E_\pi P_\gamma$,

\[
 \boxed{
 \frac{[-\operatorname {Cov}_{\rm Palm}(h_\gamma,\psi)]_+}
      {\mathbb E_{\rm Palm}\psi}
 \le q_0[\mathbb E_\pi\Xi_\gamma
             -\mathbb E_\tau\Xi_\gamma]_+.}                \tag{G.14.0.3}
\]

This is the exact product-reference object.  A deterministic normalization
of the hazard divides both sides by that deterministic row-count scale.
The realized random row count is a separate shadow-denominator transfer.

The statistic $\Xi_\gamma$ retains the cancellation lost by separate
absolute bounds on companion exposure and carrier duplicates.  Its activity
expansion has only three kinds of terms:

1. a negative empty-set duplicate term;
2. positive target sets spanning more than one carrier row; and
3. negative target sets shared by at least two carrier rows.

The remaining theorem is a tail-mass-relative estimate for this signed
connected statistic at $m=12$, not a pointwise bound on
$|\Xi_\gamma|$.

#### G.14.1 Product reference and carrier Palm law

Let $\mathcal C_r$ be the complete directed-punctured catalogue.  Every
row has $2r$ middle and $2r$ lower targets.  Retain a target $u$
independently with probability

\[
 p_u=p_{\operatorname{sh}(u)},\qquad p_M=y,\quad p_L=x,
 \qquad 0<x\le y\le1,                                    \tag{G.14.1.1}
\]

and put

\[
                         q_0=x^{2r}y^{2r}.                  \tag{G.14.1.2}
\]

Thus every catalogue row has unconditional survival probability $q_0$.
Fix a root $v$ in one chosen shore, and let
$\gamma=(v;F_1,\ldots,F_m)$ be an ordered tuple of distinct catalogue
rows through $v$.  Write

\[
 S_\gamma=\bigcup_{i=1}^mF_i,\qquad
 m_\gamma(u)=|\{i:u\in F_i\}|.                             \tag{G.14.1.3}
\]

The carrier survival probability is

\[
 q_\gamma=\prod_{u\in S_\gamma}p_u
 =q_0^m\prod_{u\in S_\gamma}p_u^{-(m_\gamma(u)-1)}.         \tag{G.14.1.4}
\]

Hence the carrier-label Palm law is

\[
                         \pi_\gamma
 =\frac{q_\gamma}{\sum_{\gamma'}q_{\gamma'}}.              \tag{G.14.1.5}
\]

Equation (G.14.1.4) shows that its departure from the uniform label law is itself
an intersection polymer supported only on targets repeated among carrier
rows.

The formulas may instead mix all root labels in the chosen shore: regard
$(v;F_1,\ldots,F_m)$ as the carrier label and use the same survival weight
$q_\gamma$.  Every identity below is labelwise.  More importantly, the
one-body constant in (G.14.2.2) depends on the row but not on the designated
root, and is in fact the same for every row.  It therefore remains a
constant after this shore/root Palm averaging.  Gate A applies the argument
one shore at a time, so no cross-shore mixture is required.

#### G.14.2 The one-body profile is constant

For one catalogue row $F$, define

\[
 L(F)=\mathbb E[|\Gamma(F)\cap E(H)|\mid F\text{ retained}]
 =q_0\sum_{G:G\cap F\ne\varnothing}
       \prod_{u\in G\cap F}p_u^{-1}.                       \tag{G.14.2.1}
\]

The symmetric group on the $2r+1$ ground labels acts transitively on the
catalogue rows: if $F=E(w)$ and $F'=E(w')$, the coordinate permutation
sending $w_i$ to $w'_i$ maps $F$ to $F'$, preserves the two shores,
and permutes the complete catalogue.  The product probabilities in (G.14.1.1)
depend only on the shore.  Therefore

\[
                         \boxed{L(F)=L_r(x,y)}              \tag{G.14.2.2}
\]

for every catalogue row $F$.

This is exactly the one-body cancellation absent from a generic
hypergraph.  A root target may occupy different positions in the oriented
punctured path, so its conditional degree-tail profile $P_\gamma$ need
not be one-body constant.  That causes no Simpson term because the hazard
profile paired with it in (G.14.2.2) is constant.

#### G.14.3 Exact connected correction

For a further catalogue row $G$, put

\[
 A_i(G)=G\cap F_i,qquad
 J_G(\gamma)=\{i:A_i(G)\ne\varnothing\},\qquad
 U_G(\gamma)=G\cap S_\gamma=\bigcup_iA_i(G),               \tag{G.14.3.1}
\]

and write

\[
                         w(A)=\prod_{u\in A}p_u^{-1}.       \tag{G.14.3.2}
\]

Define

\[
 \boxed{
 \Xi_\gamma=\sum_{G\in\mathcal C_r}
 \left\{
  \mathbf1_{\{J_G\ne\varnothing\}}w(U_G)
  -\sum_{i\in J_G}w(A_i(G))
 \right\}.}                                                \tag{G.14.3.3}
\]

##### Theorem G.14.3.1 (exact hazard decomposition)

For every labelled carrier,

\[
                         \boxed{H_\gamma=mL_r(x,y)+q_0\Xi_\gamma.} \tag{G.14.3.4}
\]

#### Proof

Conditioning the carrier to survive fixes every target in $S_\gamma$.
Thus a further row $G$ survives conditionally with probability

\[
             q_0w(G\cap S_\gamma)=q_0w(U_G).               \tag{G.14.3.5}
\]

It belongs to the carrier hazard exactly when $J_G\ne\varnothing$.
Summing (G.14.3.5) proves

\[
 H_\gamma=q_0\sum_G
       \mathbf1_{\{J_G\ne\varnothing\}}w(U_G).             \tag{G.14.3.6}
\]

On the other hand, summing the one-carrier formula (G.14.2.1) over the $m$
carrier rows gives

\[
 mL_r(x,y)=q_0\sum_G\sum_{i\in J_G}w(A_i(G)).              \tag{G.14.3.7}
\]

Subtract (G.14.3.7) from (G.14.3.6).  This is (G.14.3.4).  $\square$

If $G$ meets zero or one carrier row, its summand in (G.14.3.3) is zero.
Consequently

\[
 \boxed{\Xi_\gamma\text{ is supported on }G
                 \text{ meeting at least two carrier rows}.} \tag{G.14.3.8}
\]

This is a literal carrier--carrier--row connectedness condition.

##### G.14.3.2 Removing the constant root-only cluster

There is a sharper form adapted to the rooted boundary polymer.  Put
$p_v=p_{\operatorname{sh}(v)}$, let $D_v$ be the complete-catalogue degree
of $v$, and define the off-root intersections

\[
 B_i(G)=(G\cap F_i)-\{v\},\qquad
 K_G=\{i:B_i(G)\ne\varnothing\},\qquad
 B_G=\bigcup_iB_i(G).                                     \tag{G.14.3.9}
\]

For a catalogue row $G$, set

\[
 \chi_\gamma^\circ(G)=
 \begin{cases}
 p_v^{-1}\left\{w(B_G)-\displaystyle\sum_{i=1}^mw(B_i(G))
                         +(m-1)\right\},&v\in G,\\
 \mathbf1_{\{K_G\ne\varnothing\}}w(B_G)
       -\displaystyle\sum_{i\in K_G}w(B_i(G)),&v\notin G,
 \end{cases}                                               \tag{G.14.3.10}
\]

and

\[
                         \Xi_\gamma^\circ
 =\sum_{G\in\mathcal C_r}\chi_\gamma^\circ(G).             \tag{G.14.3.11}
\]

If $v\in G$, then every $A_i(G)=\{v\}\cup B_i(G)$ and
$U_G=\{v\}\cup B_G$.  Its summand in (G.14.3.3) is therefore

\[
 p_v^{-1}\left\{w(B_G)-\sum_{i=1}^mw(B_i(G))\right\}
 =(1-m)p_v^{-1}+\chi_\gamma^\circ(G).                       \tag{G.14.3.12}
\]

There are exactly $D_v$ such rows.  The external-row summands in (G.14.3.3)
already equal the second line of (G.14.3.10).  Hence

\[
 \boxed{\Xi_\gamma=(1-m)p_v^{-1}D_v+\Xi_\gamma^\circ.}      \tag{G.14.3.13}
\]

The first term is independent of the carrier label and disappears from
every covariance.  Moreover,

\[
 \boxed{\chi_\gamma^\circ(G)=0\quad\text{whenever }|K_G|\le1.} \tag{G.14.3.14}
\]

For $v\notin G$, this is the one-carrier cancellation already noted after
(G.14.3.7).  For $v\in G$, if no $B_i$ is nonempty then the braces in (G.14.3.10)
are $1-m+(m-1)=0$; if exactly one is nonempty, its weight cancels and the
same constants cancel.  Thus every nonconstant term has an off-root
two-star

\[
                         F_i\;-\;G\;-\;F_j,\qquad i\ne j,   \tag{G.14.3.15}
\]

whose two links are witnessed by off-root shared targets.  This is the
precise connected support to be classified by the punctured boundary
polymer.

#### G.14.4 Signed activity expansion

Put

\[
                         a_u=p_u^{-1}-1\ge0,qquad
 a(T)=\prod_{u\in T}a_u.                                  \tag{G.14.4.1}
\]

For $J_G\ne\varnothing$ and $T\subseteq U_G$, define

\[
 c_\gamma(T;G)=|\{i\in J_G:T\subseteq A_i(G)\}|.          \tag{G.14.4.2}
\]

For $T=\varnothing$, this is $|J_G|$.  Expanding
$w(A)=\prod_{u\in A}(1+a_u)=\sum_{T\subseteq A}a(T)$ in
(G.14.3.3) gives the exact identity

\[
 \boxed{
 w(U_G)-\sum_{i\in J_G}w(A_i(G))
 =\sum_{T\subseteq U_G}
          (1-c_\gamma(T;G))a(T).}                           \tag{G.14.4.3}
\]

The sign structure is now explicit.

* $T=\varnothing$ contributes $1-|J_G|<0$ when the cluster is
  nontrivial.  This is the multiplicity-one duplicate correction.
* If $T\ne\varnothing$ lies in exactly one carrier row, then
  $c_\gamma(T;G)=1$ and it cancels exactly.
* If no one carrier row contains all of $T$, then
  $c_\gamma(T;G)=0$, necessarily $|T|\ge2$, and the term is positive.
  These are cross-carrier conditioning clusters.
* If at least two carrier rows contain $T$, then the term is negative.
  These are shared-target carrier clusters.

In particular, the positive and negative pieces that appear separately as
companion exposure and duplicate load are coefficients of one connected
activity polynomial.  They should not be bounded independently.

For a root row $G\ni v$, the constant subtraction in (G.14.3.10) removes the
empty activity exactly.  With

\[
 c_\gamma^\circ(T;G)
   =|\{i:T\subseteq B_i(G)\}|\qquad
       (\varnothing\ne T\subseteq B_G),
\]

one has

\[
 \boxed{\chi_\gamma^\circ(G)
 =p_v^{-1}\sum_{\varnothing\ne T\subseteq B_G}
       (1-c_\gamma^\circ(T;G))a(T).}                        \tag{G.14.4.4}
\]

Every nonzero term in (G.14.4.4) therefore contains an off-root target
activity.  Together with (G.14.3.14), it is supported on the two-link connected
shape (G.14.3.15).

For orientation only, the cancellation-free envelope

\[
 |\Xi_\gamma|
 \le (m+1)\sum_{1\le i<j\le m}
 \sum_{\substack{G:G\cap F_i\ne\varnothing\\
                    G\cap F_j\ne\varnothing}}
          w(G\cap S_\gamma)                                \tag{G.14.4.5}
\]

follows from $w(A_i)\le w(U_G)$.  It is generally too lossy for the
coefficient-one ledger; (G.14.4.3)--(G.14.4.4), not (G.14.4.5), are the intended polymer
input.

#### G.14.5 Exact covariance reduction

Conditioned on a fixed labelled carrier, the remaining target indicators
are independent.  Both $h_\gamma$ and $\psi(d_v/c)$ are increasing, so
Harris's inequality gives

\[
 \operatorname {Cov}(h_\gamma,\psi(d_v/c)
             \mid\gamma\text{ retained})\ge0.              \tag{G.14.5.1}
\]

For completeness, Harris's inequality here follows by induction on the
independent Bernoulli coordinates: condition on the last coordinate and
use total covariance; the two conditional means are increasing in that
coordinate. The law of total covariance under the Palm mixture is

\[
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\psi)
 =\mathbb E_\pi\operatorname {Cov}(h_\gamma,\psi\mid\gamma)
  +\operatorname {Cov}_\pi(H_\gamma,P_\gamma).             \tag{G.14.5.2}
\]

Substitute (G.14.3.4); the constant $mL_r(x,y)$ disappears.  This proves
(G.14.0.2).  Dividing the second covariance by
$\mathbb E_\pi P_\gamma=\mathbb E_{\rm Palm}\psi$ gives

\[
 \frac{\operatorname {Cov}_\pi(\Xi_\gamma,P_\gamma)}
      {\mathbb E_\pi P_\gamma}
 =\mathbb E_\tau\Xi_\gamma-\mathbb E_\pi\Xi_\gamma,       \tag{G.14.5.3}
\]

which proves (G.14.0.3).

By (G.14.3.13), both covariances and both expectation differences are unchanged
when $\Xi_\gamma$ is replaced by $\Xi_\gamma^\circ$.  Thus the exact
adverse term is already supported on the off-root connected shapes in
(G.14.3.14)--(G.14.3.15).

#### G.14.6 The exact remaining product-reference theorem

For $m=12$, $x\ge r^{-\alpha}$, and the relevant deterministic-center
normalized tail tests, it is enough to prove a tail-mass-relative bound on

\[
                 q_0[\mathbb E_\pi\Xi_\gamma^\circ
                         -\mathbb E_\tau\Xi_\gamma^\circ]_+.
                                                                    \tag{G.14.6.1}
\]

The complete one-row boundary polymer already controls every fixed
one-body sum in (G.14.2.1).  It does not by itself control (G.14.6.1): the carrier
law (G.14.1.4), the signed multi-carrier activity (G.14.4.3), and the tail tilt
$P_\gamma$ must be expanded together.  The all-order Newton obstruction
for the normalized tail test prevents replacement of that expansion by a
fixed list of carrier moments.

Thus (G.14.6.1) is a precise tail-decorated connected-polymer target.  This note
does not claim its asymptotic bound, its exact-slice transfer, or the later
stopped-law/realized-center/purge transfer.

## G.15 The connected-carrier Möbius and U-statistic hierarchy

This section proves an exact refinement of G.14.  It decomposes the connected
correction by the number of carrier rows genuinely joined by one further row,
then sums every unused carrier label out of the Palm law.  Only the resulting
tail-relative estimate remains open.

Fix the root \(v\), an ordered \(m\)-carrier
\(\gamma=(F_1,\ldots,F_m)\), and a further catalogue row \(G\).  With the
notation of G.14 put

\[
 B_i(G)=(G\cap F_i)-\{v\},\qquad
 B_I(G)=\bigcup_{i\in I}B_i(G).                         \tag{G.15.1}
\]

Define the root-reduced set function

\[
 g_{G,\gamma}^{\circ}(I)=
 \begin{cases}
  p_v^{-1}\{w(B_I(G))-1\},&v\in G,\\[2pt]
  \mathbf1_{\{B_I(G)\ne\varnothing\}}w(B_I(G)),&v\notin G.
 \end{cases}                                             \tag{G.15.2}
\]

Thus \(g_{G,\gamma}^{\circ}(\varnothing)=0\), and direct substitution in
(G.14.3.10)--(G.14.3.11) gives

\[
 \Xi_\gamma^\circ=\sum_{G\in\mathcal C_r}
 \left(g_{G,\gamma}^{\circ}([m])-
       \sum_{i=1}^m g_{G,\gamma}^{\circ}(\{i\})\right). \tag{G.15.3}
\]

Put \(\mathcal S_v=\{F\in\mathcal C_r:v\in F\}\). For an ordered
\(s\)-subcarrier \(\alpha=(F_1,\ldots,F_s)\) from
\(\mathcal S_v\), define

\[
 \widehat g_{G,\alpha}^{\circ}([s])
 =\sum_{I\subseteq[s]}(-1)^{s-|I|}g_{G,\alpha}^{\circ}(I), \tag{G.15.4}
\]

and the symmetric kernel

\[
 K_s^\circ(\alpha)=
 \sum_{G\in\mathcal C_r}\widehat g_{G,\alpha}^{\circ}([s]). \tag{G.15.5}
\]

#### G.15.1 Exact connected hierarchy

For \(A\subseteq[m]\), let \(\gamma_A=(F_i)_{i\in A}\) in increasing index order. For every ordered \(m\)-carrier,

\[
 \boxed{\Xi_\gamma^\circ=
   \sum_{\substack{A\subseteq[m]\\|A|\ge2}}
        K_{|A|}^\circ(\gamma_A).}                       \tag{G.15.6}
\]

Moreover a row \(G\) contributes to the \(s\)-body coefficient only if

\[
 \boxed{(G\cap F_i)-\{v\}\ne\varnothing
        \quad(1\le i\le s).}                           \tag{G.15.7}
\]

Indeed, Boolean Möbius inversion gives

\[
 g_{G,\gamma}^{\circ}([m])=
 \sum_{\varnothing\ne A\subseteq[m]}
       \widehat g_{G,\gamma_A}^{\circ}(A).              \tag{G.15.8}
\]

The singleton coefficients are exactly the singleton terms subtracted in
(G.15.3), proving (G.15.6) after summing over \(G\).  If \(B_i(G)\) is
empty, then for every \(I\subseteq[s]-\{i\}\),

\[
 g_{G,\alpha}^{\circ}(I\cup\{i\})=g_{G,\alpha}^{\circ}(I). \tag{G.15.9}
\]

Pairing these two terms in (G.15.4), whose signs are opposite, proves
(G.15.7).

The first kernel retains the cancellation which an absolute polymer bound
would lose.  For \(s=2\), write

\[
 A=(G\cap F_1)-\{v\},\qquad B=(G\cap F_2)-\{v\}.         \tag{G.15.10}
\]

If either set is empty the coefficient is zero; otherwise it is

\[
 \widehat g_{G,(F_1,F_2)}^\circ([2])=
 \begin{cases}
 p_v^{-1}\{w(A\cup B)-w(A)-w(B)+1\},&v\in G,\\[2pt]
 w(A\cup B)-w(A)-w(B),&v\notin G.
 \end{cases}                                             \tag{G.15.11}
\]

This follows immediately by expanding the four subsets in (G.15.4).
In particular (G.15.11), rather than its termwise absolute value, is the
connected off-root two-star which the tail estimate must control.

#### G.15.2 Exact removal of unused carrier labels

Let \(X\) be the product target-retention state, let \(F\preceq X\) mean
that every target of \(F\) survives, and let
\(d=d_v(X)\) be the number of live root rows.  For \(2\le s\le m\), put

\[
 Y_s(X)=\sum_{\alpha\in\mathcal S_v^{\underline s}}
   \mathbf1_{\{\alpha\preceq X\}}K_s^\circ(\alpha),\qquad
 \overline K_s(X)=\begin{cases}Y_s(X)/(d)_s,&d\ge s,\\0,&d<s.
 \end{cases}                                             \tag{G.15.12}
\]

For an integer \(c\ge m-1\), with
\(\mathbb E(d-c)_+^m>0\), define two probability tilts of the product law:

\[
 f_c(d)=(d-c)_+^m,\qquad
 {d\lambda_m\over d\mathbb P}={(d)_m\over\mathbb E(d)_m},\qquad
 {d\lambda_c\over d\mathbb P}={f_c(d)\over\mathbb Ef_c(d)}. \tag{G.15.13}
\]

Also put

\[
 \varphi_c(d)=\begin{cases}f_c(d)/(d)_m,&d\ge m,\\0,&d<m,
 \end{cases}\quad
 P_\gamma=\mathbb E[\varphi_c(d)\mid\gamma\preceq X],\quad
 {d\tau_c\over d\pi}(\gamma)={P_\gamma\over\mathbb E_\pi P_\gamma}. \tag{G.15.14}
\]

Then every unused label sums out exactly:

\[
 \boxed{
 \mathbb E_\pi\Xi_\gamma^\circ
  =\sum_{s=2}^m{m\choose s}\mathbb E_{\lambda_m}\overline K_s,
 \qquad
 \mathbb E_{\tau_c}\Xi_\gamma^\circ
  =\sum_{s=2}^m{m\choose s}\mathbb E_{\lambda_c}\overline K_s.} \tag{G.15.15}
\]

To prove this, fix a state with \(d\) live root rows and a set of \(s\)
carrier positions.  After choosing their ordered subcarrier there are
\((d-s)_{m-s}\) ways to fill the other positions.  Hence (G.15.6) gives
the statewise identity

\[
 \sum_{\gamma\preceq X}\Xi_\gamma^\circ
 =\sum_{s=2}^m{m\choose s}(d-s)_{m-s}Y_s(X)
 =(d)_m\sum_{s=2}^m{m\choose s}\overline K_s(X).         \tag{G.15.16}
\]

Because \(\sum_\gamma q_\gamma=\mathbb E(d)_m\), averaging and dividing
proves the first identity in (G.15.15).  Furthermore

\[
 q_\gamma P_\gamma=
 \mathbb E[\mathbf1_{\{\gamma\preceq X\}}\varphi_c(d)]. \tag{G.15.17}
\]

Multiplying (G.15.16) by \(\varphi_c(d)\) and averaging gives

\[
 \sum_\gamma q_\gamma P_\gamma\Xi_\gamma^\circ
 =\sum_{s=2}^m{m\choose s}
   \mathbb E[f_c(d)\overline K_s(X)],                    \tag{G.15.18}
\]

whereas the same carrier count without \(\Xi^\circ\) gives

\[
 \sum_\gamma q_\gamma P_\gamma=\mathbb Ef_c(d).         \tag{G.15.19}
\]

Dividing (G.15.18) by (G.15.19) proves the second identity.

#### G.15.3 Exact remaining product term

At the literal Gate-A order \(m=12\), the adverse product-reference term
in (G.14.6.1) is therefore exactly

\[
 \boxed{q_0\left[
  \sum_{s=2}^{12}{12\choose s}
  \left(\mathbb E_{\lambda_{12}}\overline K_s-
        \mathbb E_{\lambda_c}\overline K_s\right)
 \right]_+.}                                             \tag{G.15.20}
\]

Its first unresolved member is

\[
 q_0{12\choose2}
 \left(\mathbb E_{\lambda_{12}}\overline K_2-
       \mathbb E_{\lambda_c}\overline K_2\right),       \tag{G.15.21}
\]

with \(K_2^\circ\) given by (G.15.11).  Thus there is no remaining
carrier-extension or between-label normalization: the open product input
is a tail-mass-relative estimate for the full signed sum (G.15.20), starting
with its tail-decorated connected two-star.  Exact two-shore slicing,
stopped actual/reference erosion, the realized center, and unequal-purge
transfer are later gates and are not asserted here.

## G.18 The two-shore overlap-cell determinant

The two covariances in the carrier comparison recombine exactly.  Retain middle and lower
targets independently with probabilities \(y,x\in(0,1)\), respectively.  For distinct
root rows \(P=(F,H)\), let
\[
 q_P=\Pr(F,H\text{ live}),\qquad
 L_g(P)=\mathbb E[g(d_v)\mid F,H\text{ live}],           \tag{G.18.1}
\]
and at carrier order twelve put
\[
 g_{12}(d)=(d-2)_{10},\qquad
 g_c(d)={(d-c)_+^{12}\over(d)_2},\quad c\ge11,           \tag{G.18.2}
\]
with the second expression zero for \(d<2\).  Set
\[
\begin{gathered}
 Z_{12}=\sum_Pq_PL_{12}(P)=\mathbb E(d_v)_{12},\qquad
 Z_c=\sum_Pq_PL_c(P)=\mathbb E(d_v-c)_+^{12},\\
 \Pi_{12}(P)={q_PL_{12}(P)\over Z_{12}},\qquad
 S(P)={L_c(P)\over L_{12}(P)},\qquad
 \overline S={Z_c\over Z_{12}}.                         \tag{G.18.3}
\end{gathered}
\]
Assume the tail mass is positive.  The cutoff pair law is the
\(S\)-tilt of \(\Pi_{12}\).  Hence, writing \(K(P)=K_2^\circ(F,H)\) for \(P=(F,H)\), with \(K_2^\circ\) defined in (G.15.11),
\[
 \boxed{\Delta_{2,c}:=
 \mathbb E_{\lambda_{12}}\overline K_2-
 \mathbb E_{\lambda_c}\overline K_2
 =-{\operatorname {Cov}_{\Pi_{12}}(K,S)\over\overline S}.} \tag{G.18.4}
\]
Indeed, \((d)_2g_{12}(d)=(d)_{12}\) and
\((d)_2g_c(d)=(d-c)_+^{12}\), so the two state tilts followed by a uniform
ordered live-pair choice are exactly the two pair laws; expanding the
tilted expectation proves (G.18.4).

Partition ordered pairs by
\[
 \tau(P)=(t_M,t_L),                                      \tag{G.18.5}
\]
the numbers of common middle and lower targets after removing the common
root.  If \(\delta_M\) records that the root is middle and
\(\delta_L=1-\delta_M\), then every row has \(2r\) targets per shore and
\[
 q_P=q_\tau=y^{4r-t_M-\delta_M}x^{4r-t_L-\delta_L}.      \tag{G.18.6}
\]
Thus \(\tau\), unlike total overlap when \(x\ne y\), is sufficient for
the pair survival weight.

For the cell \(\mathcal P_\tau\), define
\[
\begin{aligned}
 A_{12,\tau}&=\sum_{P\in\mathcal P_\tau}L_{12}(P),&
 A_{c,\tau}&=\sum_{P\in\mathcal P_\tau}L_c(P),\\
 B_{12,\tau}&=\sum_{P\in\mathcal P_\tau}K(P)L_{12}(P),&
 B_{c,\tau}&=\sum_{P\in\mathcal P_\tau}K(P)L_c(P),
\end{aligned}                                            \tag{G.18.7}
\]
and put
\[
\begin{gathered}
 \rho_\tau={q_\tau A_{12,\tau}\over Z_{12}},\qquad
 \kappa_\tau={B_{12,\tau}\over A_{12,\tau}},\qquad
 s_\tau={A_{c,\tau}\over A_{12,\tau}},\\
 \mathfrak D_\tau=A_{12,\tau}B_{c,\tau}
                  -B_{12,\tau}A_{c,\tau},\qquad
 \eta_\tau={\mathfrak D_\tau\over A_{12,\tau}^2}.       \tag{G.18.8}
\end{gathered}
\]
Conditional on \(\tau\), the factorial pair law has mass
\(L_{12}(P)/A_{12,\tau}\).  Its means of \(K,S\) are
\(\kappa_\tau,s_\tau\), and its covariance is \(\eta_\tau\).
The law of total covariance therefore gives the exact live reduction
\[
 \boxed{\Delta_{2,c}=-{1\over\overline S}
 \left\{\operatorname {Cov}_\rho(\kappa_\tau,s_\tau)
       +\sum_\tau\rho_\tau
             {\mathfrak D_\tau\over A_{12,\tau}^2}\right\}.} \tag{G.18.9}
\]
Moreover
\[
 \mathfrak D_\tau={1\over2}\sum_{P,Q\in\mathcal P_\tau}
 L_{12}(P)L_{12}(Q)
 [K(P)-K(Q)][S(P)-S(Q)],                                \tag{G.18.10}
\]
by expanding the four products.  The within-cell part of (G.18.9) is
therefore
\[
                         -{1\over Z_c}\sum_\tau
 q_\tau{\mathfrak D_\tau\over A_{12,\tau}}.             \tag{G.18.11}
\]
This is already normalized by tail mass and preserves cancellation between
cells.  Write \(z=z_\sigma\) for the average degree on the root shore. Its first honest sufficient boundary target is
\[
 q_0\left[-{1\over Z_c}\sum_\tau
 q_\tau{\mathfrak D_\tau\over A_{12,\tau}}\right]_+=o(z), \tag{G.18.12}
\]
together with a favorable or \(o(z/q_0)\) between-cell term.

No cellwise sign is asserted. The open theorem is the aggregate punctured estimate in (G.18.9)--(G.18.12), followed by the kernels \(3\le s\le12\) and the slice, stopped, center, and purge transfers.

## G.19 Factorial pair-Palm mass is off-root disjoint

Assume \(x\ge r^{-\alpha}\) for a fixed \(\alpha>0\), condition on retaining a root \(v\), and let \(\mathcal F_v\) be its \(D\)
catalogue rows; each has the same conditional survival probability \(w\).
For distinct \(F,G\), put
\[
 t(F,G)=|(F\cap G)-\{v\}|.                               \tag{G.19.1}
\]
For fixed \(c\ge1\), define the rooted kernels
\[
 R_c=\max_F{1\over D}\sum_{G\ne F}(x^{-ct(F,G)}-1),\qquad
 Q_c=\max_F{1\over D}\sum_{\substack{G\ne F\\t(F,G)>0}}
                                      x^{-ct(F,G)}.       \tag{G.19.2}
\]
The rooted boundary-polymer estimate proved in C.3 and C.3bis gives, for
\(c\alpha<1/2\),
\[
 R_c,Q_c=O_c\!\left({1\over rx^{3c}}+
                         {1\over r^2x^{4c}}\right).       \tag{G.19.3}
\]

For an ordered distinct \(m\)-tuple
\(\gamma=(F_1,\ldots,F_m)\), let \(q_\gamma^*\) be its joint survival
probability conditional on \(v\).  If a nonroot target \(u\) occurs in
\(n_u\) carriers, then
\[
 {q_\gamma^*\over w^m}
 =\prod_{\substack{u\ne v\\n_u\ge2}}p_u^{1-n_u}
 \le x^{-\sum_{a<b}t(F_a,F_b)},                         \tag{G.19.4}
\]
because \(p_u\ge x\) and \(n_u-1\le{n_u\choose2}\); the ratio is also at
least one.  Normalize these weights to the carrier law \(\pi_m\).

Fix \(F_1,\ldots,F_{i-1}\).  With \(j=i-1\), apply AM--GM to
\(z_a=x^{-jt(F_a,F_i)}\).  Its geometric mean is the summand below, and
(G.19.2) gives
\[
 \sum_{F_i\notin\{F_1,\ldots,F_{i-1}\}}
 x^{-\sum_{a<i}t(F_a,F_i)}
 \le D(1+R_{i-1}).                                      \tag{G.19.5}
\]
If \(t(F_1,F_2)>0\), the corresponding second-carrier sum is at most
\(DQ_1\).  Summing (G.19.4) successively from \(F_m\) down to \(F_2\)
therefore yields
\[
 \sum_{\substack{\gamma\\t(F_1,F_2)>0}}q_\gamma^*
 \le w^mD^mQ_1\prod_{j=2}^{m-1}(1+R_j).                 \tag{G.19.6}
\]
On the other hand the lower half of (G.19.4) gives
\[
                         \sum_\gamma q_\gamma^*
                         \ge(D)_mw^m.                    \tag{G.19.7}
\]
If \(\alpha<1/[3(m-1)]\), (G.19.3) makes every displayed \(R_j=o(1)\);
also \(D^m/(D)_m=1+o(1)\).  Dividing (G.19.6) by (G.19.7) proves
\[
 \boxed{\Pr_{\pi_m}(t(F_a,F_b)>0)
 =O_m\!\left({1\over rx^3}+{1\over r^2x^4}\right)}       \tag{G.19.8}
\]
for every specified pair, and a union bound gives the same order for any
of the fixed number of pairs.

At \(m=12\), summing the last ten carrier labels gives exactly
\[
 \sum_{F_3,\ldots,F_{12}}q^*_{F,H,F_3,\ldots,F_{12}}
 =q^*_{FH}\,
 \mathbb E[(d_v-2)_{10}\mid F,H\text{ live}].            \tag{G.19.9}
\]
Thus the first-pair marginal is the factorial Palm law \(\Pi_{12}\) of
G.18.  With \(E=\{\tau\ne(0,0)\}\), (G.19.8) gives, for
\(\alpha<1/33\),
\[
                         \boxed{\Pi_{12}(E)
                         =O((rx^3)^{-1})=o(1).}          \tag{G.19.10}
\]

This is not a tail-relative conclusion.  The cutoff law obeys
\[
 \Pi_c(E)={\mathbb E_{\Pi_{12}}[S\mathbf1_E]
                  \over\mathbb E_{\Pi_{12}}S},           \tag{G.19.11}
\]
whose denominator can be a rare tail mass, and \(K\) is not bounded.  To
delete the exceptional cells from the signed comparison one still needs
\[
 \Pi_c(E)=o(1),\qquad
 {q_0\over z}\left\{
 \mathbb E_{\Pi_{12}}[|K|\mathbf1_E]
 +\mathbb E_{\Pi_c}[|K|\mathbf1_E]\right\}=o(1).         \tag{G.19.12}
\]
Even these estimates leave the arrangement-sensitive determinant
\[
 \mathfrak D_{(0,0)}
 ={1\over2}\sum_{P,Q\in\mathcal P_{(0,0)}}
 L_{12}(P)L_{12}(Q)[K(P)-K(Q)][S(P)-S(Q)]               \tag{G.19.13}
\]
on the dominant cell.  Its favorable or tail-relative small signed bound,
the higher carrier kernels, and all stopped transfers remain open.

# Appendix H: Gate B—certified zero-avoidance lemmas

Only independently reconstructible local, shore-current, and Venn-gap
lemmas are retained. Skipped labels correspond to omitted branches.

## H.1 Exact zero-avoidance setup

Put \(b=2r+1\), identify the label and position sets with
\(\Omega=\mathbb Z_b\), and define
\(I_s^w(u)=\{w_u,\ldots,w_{u+s-1}\}\), with cyclic subscripts. A
permutation \(w\) defines

\[
 E(w)=\{(M,I_r^w(u)):u\ne0\}\mathbin{\dot\cup}
      \{(L,I_{r-1}^w(u)):u\ne0\},\qquad
 D_M=2r\,r!(r+1)! .                                      \tag{H.1.1}
\]

Write \(I_s(u)=I_s^{\mathrm{id}}(u)\), and put
\[
 X=\{(M,I_r(u)),(L,I_{r-1}(u)):u\in\mathbb Z_b\},\quad
 A_0=(M,I_r(0)),\quad B_0=(L,I_{r-1}(0)),\quad
 E_0=X-\{A_0,B_0\}.                                      \tag{H.1.2}
\]
For a tagged target \(S=(\sigma,U)\), write \(\underline S=U\). If
\(J\) is a set of tagged targets, \(\deg(S,J)\) counts the permutations
whose configuration contains \(S\) and every member of \(J\). For
\(s\in\{r,r-1\}\), define
\[
\begin{aligned}
 d_s(S)&=|\{w:S\in E(w)\}|,\\
 W_{1,s}(S)&=\sum_{T\in E_0}\deg(S,\{T\}),\\
 e_s(S)&=\sum_{w:S\in E(w)}(|E(w)\cap E_0|-1)_+,\\
 Z_s(S)&=|\{w:S\in E(w),\ E(w)\cap E_0=\varnothing\}|.
\end{aligned}                                             \tag{H.1.3}
\]
The identity \((m-1)_+=m-1+\mathbf1_{\{m=0\}}\) and finite
inclusion--exclusion give
\[
 \boxed{e_s=W_{1,s}-d_s+Z_s,\qquad
 Z_s(S)=\sum_{J\subseteq E_0}(-1)^{|J|}\deg(S,J).}         \tag{H.1.4}
\]

Fix \(2\le j\le r-2\) disjoint ordered label pairs \((a_i,b_i)\), put
\(k=r-2\), \(\ell=r+3\), and, for every \(U\subseteq\Omega\), set
\[
 H_j(U)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in U\}}-\mathbf1_{\{b_i\in U\}}),
 \qquad H_{s,j}(S)=H_j(\underline S).                     \tag{H.1.5}
\]
For a permutation \(z\), let \(zU=\{z(u):u\in U\}\) and
\(z(\sigma,U)=(\sigma,zU)\). For \(K_t=I_k(t)\), let \(\mathcal B_t\)
be the injective placements of the distinguished labels in which pair one
occupies positions \((t-1,t)\), pair two occupies
\((t+k-1,t+k)\), and every remaining pair has one position in
\(K_t-\{t,t+k-1\}\) and one in its complement after the four boundary
positions are removed. Both orientations are allowed. Thus
\[
 |\mathcal B_t|=2^j(k-2)_{j-2}(\ell-2)_{j-2}.              \tag{H.1.6}
\]
Complete each placement arbitrarily to a permutation \(z\), and put
\(\varepsilon(z)=H_j(zK_t)\). For a coefficient function \(x\) on the
tagged shore-\(s\) targets, define
\[
 \omega_x(t)={1\over|\mathcal B_t|}
 \sum_{z\in\mathcal B_t}\varepsilon(z)
       \sum_{S:|\underline S|=s}x(S)H_j(z\underline S).    \tag{H.1.7}
\]
Only the positions of the distinguished labels occur, so the value is
independent of the completion of \(z\).

The zero-avoidance coefficient has exactly the same boundary profile as
the exposure coefficient. First, \(d_s(S)\) is constant in \(S\) by label
symmetry, and the sum of \(H_j\) over one rank is zero by swapping
\(a_1,b_1\); hence \(\omega_{d_s}=0\). Next fix \(T\in E_0\) and one
boundary placement \(z\). Let \(u_i,v_i\) be the two position coordinates
occupied by event pair \(i\). If \(T\) has equal membership at \(u_i,v_i\),
then \(\tau=(u_i\ v_i)\) fixes \(T\). Pair the inner-sum root set \(S\)
with \(\tau S\). Label equivariance gives
\(\deg(\tau S,\{T\})=\deg(S,\{T\})\), while \(\varepsilon(z)\) is fixed
and \(H_j(z\tau\underline S)=-H_j(z\underline S)\). Thus the two inner
terms cancel. If neither event edge permits this involution, both are
boundaries of \(T\); their intervening arcs have
lengths \(k,\ell\), whereas \(T\) has rank \(r\) or \(r-1\), a
contradiction. Thus the profile of \(S\mapsto\deg(S,\{T\})\) is zero.
Summing over \(T\in E_0\) and using (H.1.4) gives
\[
                         \boxed{\omega_{e_s}(t)=\omega_{Z_s}(t).}
                                                               \tag{H.1.7a}
\]

The blocker coordinates must move with the event. For
\(T=(\sigma,I_{s_\sigma}(u))\in X\), where
\(s_M=r\) and \(s_L=r-1\), define
\[
 \psi_t(T)=\{-2(u-t),-2(u+s_\sigma-t)\}\subseteq\mathbb Z_b.
 \tag{H.1.8}
\]
This bijects \(X\) with the edges of
\(\widetilde B_r=\operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})\),
and sends the event cuts to the fixed roots \(0,5\). The two omitted
targets become
\[
 \mathcal P_t=\{\{2t,2t+1\},\{2t,2t+3\}\},\qquad
 B_r(t)=\widetilde B_r\setminus\mathcal P_t.               \tag{H.1.9}
\]
For an edge set \(J\), abbreviate
\(\deg_t(S,J)=\deg(S,\psi_t^{-1}(J))\). Appendices H.11, H.15, and H.16
prove a local affine identity, a remote shore-difference estimate, and a
Venn-gap bound. They do not prove Gate B: the missing output remains the
compatible all-depth positive cover stated in Section 5 and C.10.

## H.11 Sixteen local atoms for zero avoidance [I]

Assume \(r\ge6\). In the nonwrapping integer neighbourhood of the event
roots \(0,5\), the four-vertex supports of blocker terms incident with both
roots are exactly
\[
\begin{array}{rrrr}
(-3,0,2,5),&(-3,0,4,5),&(-3,0,5,6),&(-3,0,5,8),\\
(-1,0,2,5),&(-1,0,4,5),&(-1,0,5,6),&(-1,0,5,8),\\
(0,1,2,5),&(0,1,4,5),&(0,1,5,6),&(0,1,5,8),\\
(0,2,3,5),&(0,3,4,5),&(0,3,5,6),&(0,3,5,8).
\end{array}                                                \tag{H.11.1}
\]
Call this list \(\mathscr V\). For \(V\in\mathscr V\), let \(M(V)\)
be the unique two-edge matching in \(\widetilde B_r[V]\) covering all
four vertices. For the six supports
\[
 \mathscr Q_V=\{(-1,0,2,5),(0,1,2,5),(0,1,4,5),
 (0,2,3,5),(0,3,4,5),(0,3,5,6)\},                         \tag{H.11.2}
\]
the induced graph has one additional connector; write
\(P(V)=E(\widetilde B_r[V])\) for the resulting three-edge path. The
other ten induced graphs equal \(M(V)\). This is exhaustive: choose one
of the four neighbours of each root, giving the sixteen supports in
(H.11.1); on a support in (H.11.2), an edge set incident with all four
vertices is either its endpoint matching or its full path.

For a tagged shore-\(s\) root target \(S\), define the punctured local
coefficient
\[
\begin{aligned}
 \mathcal L_{s,t}(S)={}&
 \sum_{V\in\mathscr V\setminus\mathscr Q_V}
  \mathbf1_{\{M(V)\cap\mathcal P_t=\varnothing\}}
       \deg_t(S,M(V))\\
 &+\sum_{V\in\mathscr Q_V}\left[
  \mathbf1_{\{M(V)\cap\mathcal P_t=\varnothing\}}
       \deg_t(S,M(V))
 -\mathbf1_{\{P(V)\cap\mathcal P_t=\varnothing\}}
       \deg_t(S,P(V))\right],
\end{aligned}                                             \tag{H.11.3}
\]
and put \(L_{s,j}(t)=\omega_{\mathcal L_{s,t}}(t)\). These are exactly
the ten matching terms and the six matching-minus-path pairs, hence 22
signed inclusion--exclusion terms. Every bracket is nonnegative: if the
matching survives the puncture but its path does not, only the positive
term remains; otherwise
\[
 \deg_t(S,M(V))-\deg_t(S,P(V))\ge0                         \tag{H.11.4}
\]
because containment of the full path implies containment of its matching.

Remove the puncture indicators in (H.11.3), call the resulting coefficient
\(\mathcal L_{s,t}^{\circ}\), and set
\(\Omega_{s,j}=\omega_{\mathcal L_{s,t}^{\circ}}(t)\).
Cyclic translation makes \(\Omega_{s,j}\) independent of \(t\). Put
\(C_{s,j}(t)=\Omega_{s,j}-L_{s,j}(t)\).

Before edge orientation is forgotten, the unique edge of a local term
incident with an event root is its supplier. Mark it \(S\) if that root is
the start cut of the corresponding central interval, and \(E\) if it is
the end cut. Let \(F_{s,SS},F_{s,SE},F_{s,ES},F_{s,EE}\) be the complete
signed profile totals by the supplier types at roots \(0,5\). Reflection
\(u\mapsto5-u\) permutes the 22 terms, preserves the degree kernel and the
orientation-free harmonic product, and reverses both suppliers. Hence
\(F_{s,SS}=F_{s,EE}\).

Now \(\mathcal P_0=\{\{0,1\},\{0,3\}\}\), while
\(2\ell=5\pmod b\) gives
\(\mathcal P_\ell=\{\{5,6\},\{5,8\}\}\). At either shift, no local
term contains both omitted edges, because it has a unique supplier at the
affected root. Therefore
\[
 C_{s,j}(0)=F_{s,SS}+F_{s,SE},\qquad
 C_{s,j}(\ell)=F_{s,SS}+F_{s,ES}.                          \tag{H.11.5}
\]
At \(t=3\), \(\mathcal P_3=\{\{6,7\},\{6,9\}\}\), and neither edge
occurs in any of the 22 terms, so \(L_{s,j}(3)=\Omega_{s,j}\). Using
\(F_{s,SS}=F_{s,EE}\) in (H.11.5) gives
\[
 C_{s,j}(0)+C_{s,j}(\ell)=\Omega_{s,j},\qquad
 \boxed{L_{s,j}(0)+L_{s,j}(\ell)=L_{s,j}(3).}              \tag{H.11.6}
\]

For arbitrary \(x,y\in\mathbb R\), put
\(p_t=xL_{r,j}(t)+yL_{r-1,j}(t)\) and \(e_t=1-p_t\). Then
\(e_0+e_\ell-e_3=1\), so Cauchy--Schwarz proves
\[
 \boxed{{1\over b}\min_{x,y}\sum_{t\in\mathbb Z_b}
 (1-xL_{r,j}(t)-yL_{r-1,j}(t))^2\ge {1\over3b}.}           \tag{H.11.7}
\]

For completeness, a boundary-event profile vanishes unless its blocker
edge set is incident with both roots: transposing the two positions on an
unsplit event edge preserves the blocker constraints and reverses the
harmonic sign. The preceding neighbour enumeration therefore contains
every nonzero four-cut term. Let \(R_{s,j}(t)\), denoted \(R_s(t)\) when
\(j\) is fixed in H.15, be the sum of every other nonzero
inclusion--exclusion term. The remote-tail theorem H.15 gives
\[
 \omega_{Z_s}(t)=L_{s,j}(t)+R_{s,j}(t),\qquad
 |R_{s,j}(t)|=O(D_M/r^2),\quad
 |R_{r,j}(t)-R_{r-1,j}(t)|=O(jD_M/r^3).                    \tag{H.11.8}
\]
Thus the local affine gap is rigorous, but these absolute remote bounds do
not transfer it to the full zero-avoidance profile. The compatible
all-depth positive cover required by Gate B remains open.

## H.15 A shore-difference current bound for the remote tail [I]

Assume \(r\ge6\) and \(2\le j\le r-2\), as in H.1 and H.11.

**Status.**  This note proves a shore-adapted estimate for every blocker
set, before inclusion--exclusion is summed.  It improves the factor `2r` in
the usual rooted-current bound to `2j` after subtracting the middle and
lower shores.  Applied to the complete remote zero-avoidance tail outside the 22 signed
local terms of H.11, it gives

\[
 \boxed{|R_r(t)-R_{r-1}(t)|\le CjD_Mr^{-3},\qquad
        |R_s(t)|\le CD_Mr^{-2}.}                              \tag{H.15.0.1}
\]

Equivalently, the remote vector has ambient radius `O(D_M/r^2)` and
transverse distance `O(jD_M/r^3)` from the common-shore line. This is an
absolute directional statement; it does not assert a relative angle when
the common component vanishes, and it does not prove Gate B.

#### H.15.1 Configurations and currents

Put `b=2r+1`.  A word `w=(w_0,...,w_(b-1))` defines cyclic windows

\[
 I_s^w(a)=\{w_a,w_{a+1},\ldots,w_{a+s-1}\},
 \qquad a\in\mathbb Z_b,                                    \tag{H.15.1.1}
\]

with indices read modulo `b`.  Its directed punctured configuration is

\[
 E(w)=\{(M,I_r^w(a)):a\ne0\}\mathbin{\dot\cup}
      \{(L,I_{r-1}^w(a)):a\ne0\}.                            \tag{H.15.1.2}
\]

Fix `j` disjoint ordered label pairs `(a_i,b_i)`.  On an `s`-set put

\[
 H_{s,j}(S)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in S\}}-\mathbf1_{\{b_i\in S\}}),        \tag{H.15.1.3}
\]

and define the shore current of one configuration by

\[
 K_s(w)=\sum_{a=1}^{b-1}H_{s,j}(I_s^w(a)),
 \qquad s\in\{r,r-1\}.                                     \tag{H.15.1.4}
\]

For a set `J` of prescribed tagged targets, let

\[
 \deg(J)=|\{w:E(w)\supseteq J\}|,
 \qquad
 \Omega_s(J)=\sum_{w:E(w)\supseteq J}K_s(w).                \tag{H.15.1.5}
\]

The same definitions may be made after relabelling all targets and all
distinguished pairs, and may then be averaged with arbitrary coefficients
of absolute value at most one.  In particular they include the signed
boundary-event profiles used in the zero-avoidance quotient.

#### H.15.2 The pointwise shore coupling

##### Theorem H.15.2.1

For every word `w` and every choice of the `j` distinguished pairs,

\[
                         \boxed{|K_r(w)-K_{r-1}(w)|\le2j.}   \tag{H.15.2.1}
\]

Consequently, for every blocker set `J`,

\[
 \boxed{|\Omega_r(J)-\Omega_{r-1}(J)|\le2j\deg(J),\qquad
        |\Omega_s(J)|\le2r\deg(J).}                         \tag{H.15.2.2}
\]

#### Proof

Pair the two windows at the same retained start.  They are nested and
differ in exactly one label:

\[
 I_r^w(a)=I_{r-1}^w(a)\mathbin{\dot\cup}\{w_{a+r-1}\}.
                                                                    \tag{H.15.2.3}
\]

The product (H.15.1.3) depends only on membership of the `2j` distinguished
labels.  Therefore the two summands at start `a` agree unless
`w_(a+r-1)` is distinguished.  If it is distinguished, only one factor in
(H.15.1.3) changes, by one, while every other factor lies in `{-1,0,1}`; the
absolute change of the product is at most one.  As `a` runs through the
retained starts, each label occurs as `w_(a+r-1)` at most once.  At most
`2j` summands can therefore change, proving (H.15.2.1).

Sum (H.15.2.1) over the `deg(J)` words containing `J` to obtain the first
inequality in (H.15.2.2).  Each shore has `b-1=2r` retained starts and every
summand in (H.15.1.4) has absolute value at most one, which proves the second.
\(\square\)

##### Corollary H.15.2.2 (signed families and boundary averaging)

Let `A` be any finite family of blocker sets, let `|c_J|<=1`, and let

\[
 T_s=\sum_{J\in A}c_J\Omega_s(J),\qquad
 \mathcal M(A)=\sum_{J\in A}\deg(J).                        \tag{H.15.2.4}
\]

Then

\[
 |T_s|\le2r\mathcal M(A),\qquad
 |T_r-T_{r-1}|\le2j\mathcal M(A).                           \tag{H.15.2.5}
\]

The same inequalities hold if every current is first averaged over a
probability space and multiplied by a sign of modulus one.

#### Proof

Apply (H.15.2.2), the triangle inequality, and then Jensen's inequality for the
optional average. \(\square\)

#### H.15.3 The complete remote zero-avoidance tail

We record the application without suppressing its counting input.  After
the standard multiplication of cut labels by `-2 modulo b`, the blocker
graph is

\[
 \widetilde B_r=\operatorname {Cay}(\mathbb Z_b,\{\mathord\pm1,
                                      \mathord\pm3\}),\qquad
 \mathcal P_t=\{\{2t,2t+1\},\{2t,2t+3\}\},\qquad
 B_r(t)=\widetilde B_r\setminus\mathcal P_t.       \tag{H.15.3.1}
\]

The event-dependent formula is (H.1.9), and blocker terms use \(B_r(t)\). The two boundary-event roots are `p=0,q=5`.
For a blocker set `J`, write `V(J)` for its incident cuts.  The signed
boundary current vanishes unless `{p,q}` is contained in `V(J)`: if an
event-root pair is not split by a blocker, transposing its two positions
fixes the blocker constraints and reverses the harmonic sign.

Let `A_rem(t)` be the family of all nonzero signed inclusion--exclusion
terms `((-1)^|J|,J)` other than the 22 local terms in H.11: ten
matching-only terms and, on six supports, one matching and one path term. For this indexed signed family define \(\mathcal M(A_{\rm rem}(t))=\sum_{(\epsilon,J)\in A_{\rm rem}(t)}\deg(J)\). The boundary-codegree estimate is

\[
 {\deg(J)\over D_M}\le C_0^{|J|}r^{2-|V(J)|},
 \qquad D_M=2r\,r!(r+1)!.                                  \tag{H.15.3.2}
\]

Here is the short summation needed below.  A bounded-degree exploration
from fixed roots has at most `A_*^m` connected `m`-edge shapes for an absolute constant `A_*`.  A connected rooted shape meeting both `p,q` and not among the six local
four-vertex paths has at least five vertices.  If the roots lie in separate components, the only
four-vertex possibility is a two-edge matching; every other rooted shape
again has at least five vertices.  Equations (H.15.3.2) and
`|J|<=2(|V(J)|-1)` therefore make the total weight of the nonlocal rooted
shape `O(D_M/r^3)`.

Additional components contain neither root.  Dropping mutual
vertex-disjointness only enlarges their sum.  A connected component with
`v` vertices has `O(rA_*^m)` placements and contributes the factor
`C_0^m r^{-v}` after the common `D_Mr^2` rooted normalization is removed.
The one-edge case is `O(1/r)`, and all larger cases form a convergent
geometric tail for large `r`.  The exponential formula hence multiplies
the rooted estimate by `exp(O(1/r))`.  If the rooted part is one of the 22 local signed terms but at least one
additional component is present,
that added component itself supplies the missing `O(1/r)`.  Thus, uniformly
in the event shift,

\[
              \boxed{\mathcal M(A_{\rm rem}(t))
                     \le C D_M/r^3.}                        \tag{H.15.3.3}
\]

The finitely many `r` below the geometric-tail threshold are absorbed by
enlarging `C`.

Let `R_s(t)` be the signed inclusion--exclusion current of this remote
family, including the boundary-event probability average.  Corollary H.15.2.2
and (H.15.3.3) give

\[
 |R_s(t)|\le {2CD_M\over r^2},
 \qquad
 |R_r(t)-R_{r-1}(t)|\le {2CjD_M\over r^3},                  \tag{H.15.3.4}
\]

which is (H.15.0.1) after changing the absolute constant.

In common/transverse coordinates

\[
 R_+(t)={R_r(t)+R_{r-1}(t)\over2},\qquad
 R_-(t)={R_r(t)-R_{r-1}(t)\over2},                          \tag{H.15.3.5}
\]

the conclusion is

\[
 |R_+(t)|=O(D_M/r^2),\qquad
 |R_-(t)|=O(jD_M/r^3).                                      \tag{H.15.3.6}
\]

Thus its transverse distance from the common-shore line is
`O(jD_M/r^3)` inside an ambient radius `O(D_M/r^2)`. For `j` comparable
with `r`, (H.15.3.6) gives no improvement over the absolute estimate.

#### H.15.4 Scope

The theorem is exact before blocker summation and is independent of the
number of blocker components. It controls the shore difference at every
fixed harmonic depth, but it neither controls cancellation along the
common-shore line nor proves the Gate-B cover.  These estimates do not construct the compatible all-depth positive cover
required by Gate B in Section 5 and C.10.

## H.16 Venn-gap localization [I]

Let \(\varnothing\ne J\subseteq E_0\) be a finite set of canonical tagged central
targets, and let \(\deg(J)\) be the number of directed punctured
configurations containing them. Their standard interval presentations in
(H.1.2) give canonical boundary cuts. List the distinct cuts cyclically,
form their positive cyclic gaps, reorder that multiset as
\(g_1\ge g_2\ge\cdots\ge g_q\), and put
\(\delta=\sum_{i=3}^qg_i\). The proved estimate is

\[
 \boxed{{\deg(J)\over D_M}
 \le32^{|J|-1}{r+2\over
  (\delta+1){r\choose\delta+1}}}
 \qquad(0\le\delta\le r-2).                         \tag{H.16.1}
\]


### H.16.1 Venn-gap localization

Let `J subseteq E_0` contain `t>=1` canonical tagged central targets.  Write

\[
 \deg(J)=|\{w:E(w)\supseteq J\}|,
\]

where `E(w)` is the directed punctured configuration of the cyclic word
`w`; thus each of its middle and lower targets has nonzero start.  List the `q>=2` distinct original cut positions of `J` in cyclic order and
call the resulting positive gaps `d_1,...,d_q`. Reorder this gap multiset
nonincreasingly as

\[
                         g_1\ge g_2\ge\cdots\ge g_q,
 \qquad\sum_i g_i=b,                                       \tag{H.16.2}
\]

and define

\[
                         \delta=\sum_{i=3}^qg_i.             \tag{H.16.3}
\]

#### Theorem H.16.1

If `0<=delta<=r-2`, then (H.16.1) holds.

#### Proof

Fix an anchor target.  A second central interval with prescribed length and
intersection has at most four possible relative starts.  Hence the number
of retained positional target tuples with the labelled Venn signature of
`J` is at most

\[
                         (b-1)4^{t-1}.                       \tag{H.16.4}
\]

If the labelled Venn-cell sizes are `n_tau`, compatible labels contribute
`V(J)=prod_tau n_tau!`.  Put `G(J)=prod_i g_i!`.  Refining the cells one
interval at a time gives

\[
                         V(J)\le8^{t-1}\prod_{i=1}^qg_i!.    \tag{H.16.5}
\]

Here is the full refinement argument.  Expose the targets one at a time and
write `R=V/G`.  If an old Venn cell of size `n` receives `a` labels of the
new target, its factorial contribution is multiplied by
`a!(n-a)!/n!=1/binom(n,a)`.  If a new cut splits an old elementary gap of
size `g` into `u,g-u`, the gap-factorial contribution is multiplied by
`1/binom(g,u)`.  When the two new cuts lie in different old gaps, choosing
the required labels independently in the split gaps injects into the
choice of the required labels in their containing Venn cells.  Hence the
product of the gap binomials is at most the product of the Venn-cell
binomials, and `R` cannot increase.  The same argument covers one new cut;
two old cuts can only decrease `V`.

If both new cuts lie in one old gap of size `g`, write the three pieces as
`x,y,z`, with `y` between the new cuts.  The gap-refinement factor is

\[
 {g!\over x!y!z!}={g\choose y}{g-y\choose x}.              \tag{H.16.5a}
\]

The middle piece has length `r` or `r-1`, or the complementary length.
The containing Venn-cell binomial cancels `binom(g,y)`.  Every old gap lies
inside one of the two arcs of the first exposed central target, so
`g<=r+2`.  Therefore `g-y<=3` in the first case and `g-y<=1` in the
complementary case.  The uncancelled factor in (H.16.5a) is at most
`2^(g-y)<=8`.  Thus each added target multiplies `R` by at most eight,
which proves (H.16.5).

Write `G=prod_i g_i!`.  Merging the gaps after the two largest gives
`prod_(i>=3)g_i!<=delta!`.  Every elementary gap is at most `r+2`.
Since `g_1+g_2=2r+1-delta` and `delta<=r-2`, factorial log-convexity moves
mass toward the larger gap and yields

\[
 G\le(r+2)!(r-1-\delta)!\,\delta!.                          \tag{H.16.6}
\]

The exact Venn count is the positional count times `V(J)`.  Divide
(H.16.4)--(H.16.6) by `D_M=(b-1)r!(r+1)!` and use

\[
 { (r+2)!(r-1-\delta)!\delta!\over r!(r+1)!}
 ={r+2\over(\delta+1){r\choose\delta+1}}.                  \tag{H.16.7}
\]

This proves (H.16.1). \(\square\)

For fixed `delta`, (H.16.1) is `O_t(delta! r^-delta)`.  A consequence needed
below avoids any assertion about the number of positions at fixed
`delta`.  Fix `t_0>=2` and a family of `O_(t_0)(1)` rooted boundary-graph
shapes, each incident with both event roots `{0,5}` and having at most `t_0-1` blocker edges;
to each realization adjoin one central blocker edge.  There are at most
`2b=O(r)` choices for that edge.  For
`7<=delta<=r/2`, the right side of (H.16.1) is largest at `delta=7`; hence the
sum over *all* edge positions is at most

\[
 O_{t_0}\left({r(r+2)\over8{r\choose8}}\right)
 =O_{t_0}(r^{-6}).                                         \tag{H.16.8}
\]

For `delta>r/2`, use the unsimplified bound (H.16.4)--(H.16.5).  Since
`q<=2t_0`, one has

\[
 g_3\ge {\delta\over q-2}\ge {r\over2(2t_0-2)},
 \qquad g_1,g_2\ge g_3.                                   \tag{H.16.9}
\]

Also every `g_i<=r+2`.  With `p_i=g_i/b`, the vectors `(p_i)` therefore
belong, up to `O(1/r)`, to the compact set

\[
 \sum p_i=1,qquad \max p_i\le {1\over2},qquad
 p_3\ge {1\over6(2t_0-2)}.
\]

Put `H(p)=-sum_i p_i log p_i`. This continuous function has a minimum
on the displayed compact set. Under `max p_i<=1/2`, its value is at
least `log 2`, with equality only at a permutation of
`(1/2,1/2,0,...)`; the lower bound on the third-largest coordinate
excludes every equality point. Hence `H(p)>=log 2+c_(t_0)` for some
`c_(t_0)>0`.  The integral comparisons
\(\int_1^n\log t\,dt\le\log(n!)\le\int_1^n\log t\,dt+\log n\) give
\(\log(n!)=n\log n-n+O(\log(n+1))\). Hence
\[
 \log{\prod_i g_i!\over r!(r+1)!}
 =-b\{H(p)-\log2\}+O_{t_0}(\log r),
\]
and therefore, uniformly in this range,

\[
 {\prod_i g_i!\over r!(r+1)!}
 \le \exp(-c'_{t_0}r).                                    \tag{H.16.10}
\]

The positional factor (H.16.4), the at most `2b` edge choices, and the
bounded number of rooted core types are polynomial and are absorbed by
the exponential.  Combining (H.16.8)--(H.16.10) proves

\[
 \sum_{\substack{J:\text{from the fixed core family}\\
                         \text{plus one edge},\ \delta(J)\ge7}}
 \deg(J)=O_{t_0}(D_Mr^{-6}).                               \tag{H.16.11}
\]

Multiplying by the current bound \(2r\) from (H.15.2.2) makes their normalized profile
contribution `O(r^-5)`.


The conclusion proved here is exactly this: after fixing
an \(O(1)\)-sized family of blocker-edge patterns incident with both event
roots, adjoining one further blocker edge with Venn-gap defect at least
seven has total normalized profile contribution \(O(r^{-5})\), after the
\(2r\) current factor. It does not sum arbitrary root-incident patterns,
two or more components disjoint from both roots, or the full
inclusion--exclusion series. These retained lemmas do not prove Gate B; the
missing output is the compatible all-depth positive cover stated in
Section 5 and C.10.

# Appendix I: Gate C—direct-hole compilation and balanced coset tour banks

This appendix contains only the Gate-C statements used by the live direct
route.  All ground sets and all target sets are labelled.  Throughout,
\(b\) is sufficiently large and odd, so \(H\le b-2\),
\[
 \lvert\Omega\rvert=2b,\qquad
 W=\binom{2b}{b},\qquad
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,\qquad
 g=b+H .
 \tag{I.1}
\]
Thus \(H=o(b/\log b)\) and \(g=(1+o(1))b\).

The results below have three roles.

1. A direct-hole compiler turns one literal family of physical fragments
   into a coefficient-one word.
2. Coherent tours and their linear cosets give large integral banks which
   are already disjoint at ranks \(b-1,b,b+1\).
3. The cosets may simultaneously have dual distance greater than \(H\);
   hence every bank has exact \(H\)-wise state balance.

The only unproved assertion is the final boxed selection gate.

## I.1 The direct-hole compiler

A singleton word is a word whose letters are one-element subsets of
\(\Omega\).  For a finite singleton word
\(w=(w_1,\ldots,w_n)\), write
\[
 I_s^w(a)=\{w_a,w_{a+1},\ldots,w_{a+s-1}\}
 \tag{I.2}
\]
when the displayed letters are pairwise distinct.  We call such a window
clean.  A physical \(H\)-fragment of core length \(L\) consists of a
singleton word and \(L\) consecutive core starts for which every window
of length
\[
                       b-H\le s\le b+H                 \tag{I.3}
\]
is contained in the word and clean.  Its designated rank-\(s\) targets
are the \(L\) sets in (I.2) at those core starts.

Consider physical \(H\)-fragments \(F_1,\ldots,F_t\), with core lengths
\(L_1,\ldots,L_t\).  Assume that their designated middle targets are
globally distinct.  Put
\[
 M=\sum_{\ell=1}^tL_\ell,\qquad
 \mathcal I_s=\bigcup_{\ell=1}^t
  \{\text{designated rank-\(s\) targets of }F_\ell\},
 \qquad
 h_s=\binom{2b}{s}-|\mathcal I_s|.                    \tag{I.4}
\]

### Theorem I.1 (direct-hole compiler) [I]/[C]

For every such family, the following finite inequality is [I]:
\[
\boxed{
 \nu(2b)\le
 M+(g-1)t+
 \sum_{s=b-H}^{b+H}h_s+
 \sum_{\substack{1\le s\le2b\\|s-b|>H}}\binom{2b}{s}.}
 \tag{I.5}
\]
Consequently, the following implication is [C]:
\[
 M=W-o(W),\qquad gt=o(W),\qquad
 \sum_{s=b-H}^{b+H}h_s=o(W)                         \tag{I.6}
\]
imply
\[
                         \nu(2b)=(1+o(1))W.          \tag{I.7}
\]

#### Proof

Linearize each fragment separately, retaining its \(L_\ell\) core starts
and the following \(g-1\) singleton letters.  This costs
\(L_\ell+g-1\) letters and realizes every one of its designated targets.
Concatenate the resulting blocks.  No witness is allowed to cross a block
boundary, so repetitions between different blocks are irrelevant.

For every absent band target append one letter equal to that target.
For every nonempty target outside the band do the same.  A one-letter
interval realizes each appended target, proving (I.5).

It remains to bound the far-rank sum.  If
\(X\sim\operatorname {Bin}(2b,1/2)\), the exponential-moment proof of
Hoeffding's bound gives
\[
 \Pr(|X-b|\ge H)\le 2e^{-H^2/b}.
 \tag{I.8}
\]
Also \(W\ge2^{2b}/(2b+1)\), since \(W\) is the largest of the
\(2b+1\) binomial coefficients.  By (I.1),
\[
 \sum_{|s-b|>H}\binom{2b}{s}
 \le2^{2b+1}e^{-H^2/b}=o(W).                        \tag{I.9}
\]
Equations (I.5)--(I.6) give the coefficient-one upper bound.  The central
rank witness lower bound gives \(\nu(2b)\ge W\), so (I.7) follows.
\(\square\)

Theorem I.1 deliberately asks for literal holes, not balanced quotas.
It therefore remains valid when different fragments overlap at
off-middle ranks; only the middle core targets must be disjoint.

## I.2 Coherent FIFO tours

Fix a perfect pairing
\[
 \mathcal P=\{P_j:j\in\mathbb Z_b\},\qquad
 P_j=\{a_j^0,a_j^1\},
 \tag{I.10}
\]
and a directed cyclic order of its pairs.  An initial state
\(x=(x_0,\ldots,x_{b-1})\in\mathbb F_2^b\) selects \(a_j^{x_j}\)
from \(P_j\). The boundary state \(C_{s,0}\) is a FIFO queue, in pair
order \(P_s,P_{s+1},\ldots,P_{s-1}\), containing the currently selected
member of each pair. For \(1\le k<b\), append the opposite member of
\(P_{s+k}\), eject the queue front, and call the resulting middle set
\(C_{s,k}\). Finally append the retained selected member of \(P_s\), eject
the front, and obtain
\[
                         C_{s,b}=C_{s+1,0}.            \tag{I.10a}
\]
Define, for \(1\le k<b\),
\[
 M_{s,k}=C_{s,k},\qquad
 L_{s,k}=C_{s,k}\cap C_{s,k+1},\qquad
 U_{s,k}=C_{s,k}\cup C_{s,k+1}.                    \tag{I.10b}
\]
Thus each packet flips every nonspecial pair once and then rotates the
coordinate queue and special index. Every pair is nonspecial in \(b-1\)
packets; since \(b-1\) is even, the \(b\) packets return both the selected
members and queue order, forming a cyclic tour \(T_{\mathcal P}(x)\).
The cyclic list of appended singleton labels is the tour word, and every
\(C_{s,k}\) above is its current length-\(b\) FIFO window.

Index the internal flags by
\[
                  (s,k),\qquad s\in\mathbb Z_b,\quad
                  1\le k<b,                              \tag{I.11}
\]
and put \(q=b(b-1)\).  The sets in (I.10b) are the attached targets at
ranks \(b-1,b,b+1\). Their
pair-occupancy signatures are
\[
\begin{array}{c|c|c}
\text{target}&\text{empty pairs}&\text{doubled pairs}\\ \hline
L_{s,k}&P_s&\varnothing\\
M_{s,k}&P_s&P_{s+k}\\
U_{s,k},\ k\le b-2&P_s&P_{s+k},P_{s+k+1}\\
U_{s,b-1}&\varnothing&P_{s-1}.
\end{array}                                                \tag{I.12}
\]
Every other pair is split.  On a split pair \(P_j\), the selected member
has the form
\[
                         a_j^{\,x_j+c_{s,k}(j)},             \tag{I.13}
\]
where the chronology constant \(c_{s,k}(j)\in\mathbb F_2\) is independent
of \(x\).  Formulas (I.12)--(I.13) follow directly by recording the pairs
already flipped in the FIFO packet.

Within one tour the middle targets are distinct because their ordered
empty/doubled pair \((P_s,P_{s+k})\) is recoverable.  The lower targets
from different packets have different empty pairs; within one packet
they are successive distinct transversals of a cube path.  The internal
upper signature recovers \(s,k\), and a boundary upper signature has a
different type and recovers \(s\).  Hence one tour has exactly \(q\)
distinct targets separately at all three displayed ranks.

## I.3 Pairing incidence and the necessary pairing scale

A middle target is defect one relative to \(\mathcal P\) if one pair is
empty, a different pair is doubled, and every other pair is split.  The
defect-one stratum has size
\[
 |\mathcal V_{\mathcal P}^{(1)}|
 =b(b-1)2^{b-2}=q2^{b-2},                              \tag{I.14}
\]
because one chooses the ordered empty/doubled pair and one member from
each remaining pair.  Every coherent tour on \(\mathcal P\) uses one
target from each of the \(q\) ordered empty/doubled fibers.

Thus any family of tours on one pairing whose retained middle targets are
disjoint and whose tours each retain at least \((1-\varepsilon)q\)
targets has size at most
\[
                 \frac{2^{b-2}}{1-\varepsilon}.             \tag{I.15}
\]
Any coherent-tour family satisfying the final target (I.41) uses at least
\((1-o(1))W/q\) tours, because one tour supplies at most \(q\) retained
core starts.  If the total number \(D=o(W)\) of deleted starts is nonzero,
put \(\varepsilon_b=\sqrt{D/W}\).  Tours losing more than
\(\varepsilon_bq\) starts number at most
\(D/(\varepsilon_bq)=o(W/q)\); deleting those tours costs only \(o(W)\)
further starts.  The remaining tours satisfy (I.15) with
\(\varepsilon_b=o(1)\).  Consequently any such construction needs
\[
 R\ge(1-o(1))\frac{W}{q2^{b-2}}
       =\Omega\!\left(\frac{2^b}{b^{5/2}}\right)             \tag{I.17}
\]
different pairings.  This is a counting necessity, not a construction.

The complete incidence of pairings with targets is also explicit.  Let
\[
 \mathfrak P=\frac{(2b)!}{2^bb!}.
 \tag{I.18}
\]
A fixed middle target \(C\) is defect one for
\[
\boxed{
 D_1=\binom b2^2(b-2)!=\frac{b!\,b(b-1)}4}
 \tag{I.19}
\]
pairings: choose the internal pair of \(C\), the internal pair of
\(\Omega\setminus C\), and biject the remaining vertices across the cut.
Double counting gives
\[
 p:=\frac{D_1}{\mathfrak P}
   =\frac{q2^{b-2}}{W}.                                  \tag{I.20}
\]

For two targets \(C,D\), put \(d=|C\setminus D|\), \(a=b-d\), and name
their Venn cells
\[
 A=C\cap D,\quad B=C\setminus D,\quad
 G=D\setminus C,\quad E=\Omega\setminus(C\cup D).
\]
Their sizes are \(a,d,d,a\).  Denote an edge between cells \(X,Y\) by
\(XY\), allowing \(X=Y\).  After the small core which
supplies the two defect-one incidences for each cut is removed, all
remaining pairing edges are forced between the two size-\(a\) cells and
between the two size-\(d\) cells.  The exhaustive core list, after
division by the remaining \(a!d!\) bijections, is
\[
\begin{array}{c|c}
AA,EE&a(a-1)/4\\
BB,GG&d(d-1)/4\\
GG,AB,BE;\ BB,AG,GE&ad(d-1)/2\ \text{each}\\
EE,AB,AG;\ AA,BE,GE&da(a-1)/2\ \text{each}\\
AB,AG,BE,GE&a(a-1)d(d-1).
\end{array}                                                \tag{I.21}
\]
The rows partition the four required internal cut incidences according
as two are supplied by one same-cell edge or all are supplied separately;
hence no core is omitted or counted twice.  Summing (I.21) proves that
the common pairing degree is
\[
\boxed{
 \Lambda_d=a!d!\left[
 ad(ad-1)+\frac{a(a-1)+d(d-1)}4\right].}
 \tag{I.22}
\]
Therefore
\[
 \frac{\Lambda_d}{D_1}
 =\frac{4ad(ad-1)+a(a-1)+d(d-1)}
 {b(b-1)\binom bd}.                                      \tag{I.23}
\]
After quotienting \(C\sim\Omega\setminus C\), for \(b\ge7\),
\[
\boxed{
 \max_{1\le d\le(b-1)/2}\frac{\Lambda_d}{D_1}
 =\frac{5(b-2)}{b^2}}                                    \tag{I.24}
\]
attained at \(d=1\).  Substitution gives the displayed value.  For
\(d=2\), the comparison reduces to
\(5b^3-54b^2+179b-186\ge0\).  For \(d\ge3\), use
\(\binom bd\ge\binom b3\) and
\[
 \frac{b^4}{4}+b^2
 \le\frac56(b-1)^2(b-2)^2 .
\]
Both inequalities hold at \(b=7\) and their differences increase
thereafter, proving (I.24).

If \(R\) pairings are sampled uniformly without replacement, a fixed
target is missed with probability at most \(e^{-pR}\).  Hence, for any
arbitrarily slow \(a_b\to\infty\) (in particular \(a_b=o(D_1)\)), some menu of
\[
\boxed{
 R=\left\lceil\frac{a_b}{p}\right\rceil
  =(a_b+o(1))\frac4{\sqrt\pi}\frac{2^b}{b^{5/2}}}
 \tag{I.25}
\]
pairings leaves at most \(We^{-a_b}=o(W)\) targets outside the union of
their defect-one strata. The internal central-binomial estimate (A.1)
and (I.20) give the asymptotic expression. Equations (I.17) and (I.25)
locate the pairing
resource to within the arbitrarily slow factor \(a_b\).

## I.4 Three-rank collision differences

For fixed \(\mathcal P\) and fixed pair order, target membership is affine
in the initial state.  Thus whether \(T_{\mathcal P}(x)\) and
\(T_{\mathcal P}(x')\) collide at one of ranks \(b-1,b,b+1\) depends only
on \(h=x+x'\).  Let
\[
 \mathcal B\subseteq\mathbb F_2^b\setminus\{0\}
 \tag{I.26}
\]
be the set of collision differences.

Equality of two targets first forces equality of their occupancy
signatures in (I.12), and then fixes \(h\) on every split pair.  The
possible equal-signature index pairs and free state bits are
\[
\begin{array}{c|c|c|c}
\text{rank class}&\text{compatible index pairs}
 &\text{free bits}&\text{candidate differences}\\ \hline
b-1&b(b-1)^2&1&2b(b-1)^2\\
b&b(b-1)&2&4b(b-1)\\
b+1\text{ internal}&b(b-2)&3&8b(b-2)\\
b+1\text{ boundary}&b&1&2b.
\end{array}                                                \tag{I.27}
\]
For example, a lower signature fixes the empty pair and leaves only its
state bit free; a middle signature leaves the empty and doubled pair bits
free.  The upper cases are identical.  Internal and boundary upper
signatures cannot agree.  Taking the union in (I.27) gives
\[
\boxed{
 |\mathcal B|\le M_b:=2b^3+8b^2-16b.}
 \tag{I.28}
\]
Moreover \(\mathcal B\) contains every word of Hamming weight one or two.
Indeed, for any ordered \(t\ne i\), two tours share the middle target in
the \((t,i)\)-fiber exactly when their difference is supported on
\(\{t,i\}\).

## I.5 Balanced linear-coset banks

The next theorem strengthens an arbitrary greedy independent bank: all
banks arise as cosets of one code and are exactly balanced on every set
of at most \(H\) state coordinates.

Put
\[
 \rho=\left\lceil\log_2(4M_b)\right\rceil .
 \tag{I.29}
\]
For all sufficiently large \(b\), \(\rho<b\).

### Theorem I.2 (balanced separating code) [I]

More generally than the default value in (I.1), for every integer
\(1\le H=o(b/\log b)\) there is a full-rank linear map
\[
 A:\mathbb F_2^b\longrightarrow\mathbb F_2^\rho
 \tag{I.30}
\]
such that, with \(\mathcal C=\ker A\),
\[
\boxed{
 \mathcal C\cap\mathcal B=\varnothing,\qquad
 d(\mathcal C^\perp)>H.}
 \tag{I.31}
\]
Every coset has
\[
 |\mathcal C|=2^{b-\rho}\ge\frac{2^b}{8M_b}           \tag{I.32}
\]
states.

#### Proof

Choose the \(\rho\) rows of \(A\) independently and uniformly.  For each
nonzero \(h\),
\(\Pr(Ah=0)=2^{-\rho}\), so
\[
 \Pr(\ker A\cap\mathcal B\ne\varnothing)
 \le M_b2^{-\rho}\le\frac14.                         \tag{I.33}
\]
For a fixed nonzero row coefficient
\(u\in\mathbb F_2^\rho\), the word \(uA\) is uniform in
\(\mathbb F_2^b\).  Hence
\[
 \Pr(\exists\,u\ne0:\operatorname {wt}(uA)\le H)
 \le(2^\rho-1)2^{-b}\sum_{j=0}^H\binom bj.           \tag{I.34}
\]
The elementary bound
\[
 \sum_{j=0}^H\binom bj\le(H+1)(eb/H)^H              \tag{I.35}
\]
and \(H=o(b/\log b)\), \(\rho=O(\log b)\), make the logarithm of
the right side \(-(\log2)b+o(b)\).  It is below \(1/4\) for large \(b\).
With positive probability neither bad event occurs.  Avoidance of the
second event also makes the rows independent, because \(uA=0\) would have
weight zero.  Their span is \(\mathcal C^\perp\), proving (I.31).
Finally \(2^\rho<8M_b\), which gives (I.32).
\(\square\)

### Corollary I.3 (three-rank banks and exact resolutions) [I]

For every coset \(z+\mathcal C\),
\[
 \mathfrak B_z=\{T_{\mathcal P}(x):x\in z+\mathcal C\}
 \tag{I.36}
\]
is jointly target-disjoint at ranks \(b-1,b,b+1\).  The cosets resolve
every defect-one middle target exactly four times.

#### Proof

Distinct states in one coset differ by a nonzero word of
\(\mathcal C\), which is outside \(\mathcal B\) by (I.31).  This proves
three-rank disjointness, including within-tour disjointness from I.2.

Fix a defect-one target with empty/doubled pair \((P_t,P_i)\).  Its split
choices determine all state bits outside \(\{t,i\}\), so its four
preimages are
\[
             x_0+\{0,e_t,e_i,e_t+e_i\}.             \tag{I.37}
\]
Every nonzero difference of these states has weight one or two, hence
belongs to \(\mathcal B\) and not to \(\mathcal C\).  The four states
occupy four different cosets, and no other state produces the target.
\(\square\)

The same argument records the adjacent multiplicities.  A lower target
with one empty pair and all others split has \(2(b-1)\) state-index
preimages: there are \(b-1\) positions in its packet and its empty-pair
bit is free.  An accessible internal upper target has eight preimages,
while a packet-boundary upper target has two.  Since any two preimages
share that target, they lie in distinct cosets.  Thus these are also the
exact numbers of coset banks containing the corresponding target.

### Lemma I.4 (dual distance gives exact projections) [I]

If \(J\subseteq[b]\) and \(|J|\le H\), the projection of
\(\mathcal C\) onto \(\mathbb F_2^J\) is surjective.  Every pattern on
\(J\) therefore occurs exactly \(|\mathcal C|/2^{|J|}\) times in every
coset.

#### Proof

If the projection were not onto, a nonzero linear functional on
\(\mathbb F_2^J\) would annihilate it.  Extending the functional by zero
outside \(J\) would give a nonzero word of
\(\mathcal C^\perp\) of weight at most \(H\), contrary to (I.31).
Every fiber of a surjective linear map has the same size, and translation
proves the coset assertion.
\(\square\)

### Theorem I.5 (coset-independent low-order profiles) [I]

Fix the pairing and order.  For every ground-coordinate set
\(S\subseteq\Omega\) with \(|S|\le H\), every coset bank contains the
same number of middle targets containing \(S\).  The same assertion holds
separately at ranks \(b-1\) and \(b+1\).  For one ground coordinate
\(a\),
\[
\boxed{
 |\{T:\ T\text{ is a middle target in }\mathfrak B_z,\ a\in T\}|
 =\frac{q|\mathcal C|}{2}.}
 \tag{I.38}
\]

#### Proof

At a fixed flag index, (I.12)--(I.13) show that containment of \(S\) is
either impossible, automatic on an empty or doubled pair, or prescribes
one state bit for every split pair met by \(S\).  It prescribes at most
\(|S|\le H\) bits.  Lemma I.4 makes the number of solutions independent
of the coset.  Sum over the \(q\) flag indices.  The same proof applies
to the adjacent signatures.

For (I.38), let \(a\in P_j\).  Among the \(q\) middle indices, \(b-1\)
have \(P_j\) empty, \(b-1\) have it doubled, and
\((b-1)(b-2)\) have it split. Averaged uniformly over the coset states,
their contribution is
\[
 0+(b-1)+\frac{(b-1)(b-2)}2=\frac q2.
 \tag{I.39}
\]
Coset independence turns the average into the exact value (I.38).
\(\square\)

Consequently any middle-target-disjoint union of whole coset banks is an
exact one-design: every coordinate lies in half of its selected middle
targets.  Its residual in the full middle layer is also an exact
one-design.  Across different pairings, higher-order profiles can differ.

There is also a useful global codegree consequence. For each pairing and
order, choose a map satisfying Theorem I.2, and then choose a uniform
coset. A fixed defect-one target belongs to four cosets. Two
targets belong to at most four common cosets.  Conditional on the pairing,
their normalized bank codegree is therefore at most one; averaging over
pairings and using (I.23)--(I.24) gives
\[
 \frac{\Pr(C,D\text{ lie in the sampled bank})}
      {\Pr(C\text{ lies in the sampled bank})}
 \le\frac{\Lambda_d}{D_1}
 \le\frac{5(b-2)}{b^2}                                  \tag{I.40}
\]
for noncomplementary targets and \(b\ge7\).  This supplies outer volume
and small pair codegree, but growing bank size prevents a conclusion from
a generic fixed-uniformity matching theorem.

## I.6 Exact remaining independent fragment gate

A repaired coherent-tour fragment is a physical \(H\)-fragment whose
middle core starts are a subset of the ordered flags of one coherent tour
and whose designated targets agree with the attached targets at the
central three ranks.  Splitting one tour into several fragments is
allowed; every split is charged through the fragment count in (I.5).

### Gate \(C_{\rm F}\) [O]

Construct, for every sufficiently large odd \(b\), a family of repaired
coherent-tour fragments drawn from whole balanced coset banks, possibly
followed by deletion of \(o(W)\) total core starts, such that
\[
\boxed{
\begin{aligned}
 &\text{all retained middle core targets are distinct},\\
 &M=W-o(W),\qquad gt=o(W),\\
 &\sum_{s=b-H}^{b+H}
 \left[\binom{2b}{s}-|\mathcal I_s|\right]=o(W).
\end{aligned}}
 \tag{I.41}
\]
Theorem I.1 then proves
\(\nu(2b)=(1+o(1))W\).  The top-bit splice transfers this to the
next three dimensions; since the present base dimensions are
\(2b\equiv2\pmod4\), these bounded transfers cover every sufficiently
large dimension.

The proved input to (I.41) is exact:

* a near-optimal menu of pairings covers all but \(o(W)\) defect-one
  middle targets, by (I.25);
* within every pairing/order, each coset is an integral
  \(2^b/\operatorname {poly}(b)\)-tour bank disjoint at the three central
  ranks;
* all cosets exactly fourfold-resolve the middle stratum and have exact
  adjacent signature loads; and
* every coset is \(H\)-wise uniform, with the pairing-independent
  one-coordinate balance (I.38).

What is not proved is precisely:

1. a target-disjoint selection of whole banks across different pairings
   covering \(W-o(W)\) middle targets while respecting both adjacent
   ranks; and
2. a physical all-offset lift or repair of that same selection whose
   aggregate band-hole sum and fragmentation charge satisfy (I.41).

Neither random pairing coverage, fractional incidence, pair codegree, nor
the low-order balance theorem is being asserted to imply these two
statements.  Conversely, no common symmetric-chain factor is an additional
hypothesis on this direct-hole route: the literal conditions (I.41) are
already sufficient.
