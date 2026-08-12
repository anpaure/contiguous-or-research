# In-place PBBS compilers: an exact positive collar and two sharp local barriers

Date: 2026-07-25

Only the coefficient-one seam problem is considered here. No computation,
solver, or probabilistic input is used.

## 0. Outcome

Let \(H\ge1\). This note proves three exact facts about the sought
\(S+O(H)\) replacement of an \(S\)-transition owner segment.

1. A no-overtaking fixed-core collar of \(S\) transitions has one literal
   word of length exactly \(S+H+1\) covering every consecutive lower
   intersection and upper union through depth \(H\).
2. On one maximal \(H\)-collar, the \(2H+1\) central-marker word is optimal
   even among arbitrary nonzero set-valued words with arbitrary helpers.
3. Endpoint-capped erosion cannot be repaired merely by adding coordinates
   to its existing letters while retaining its canonical witnesses. One
   positive run of length at most \(H\) is already impossible.

Thus the missing compiler cannot be a letterwise augmentation of erosion
and cannot be a sectorwise shortening of the central-marker gadget. It has
to change witness alignment and fuse successive active-coordinate orders.

## 1. Exact coefficient-one compiler for a sliding collar

Let \(K\ne\varnothing\), let

\[
 \gamma_0,\gamma_1,\ldots,\gamma_{S+H}
\]

be distinct coordinates outside \(K\), and put

\[
 X_i=K\cup\{\gamma_i,\gamma_{i+1},\ldots,\gamma_{i+H}\},
 \qquad 0\le i\le S.                              \tag{1.1}
\]

### Theorem 1.1 (global sliding-collar compiler)

The word

\[
 \boxed{
  K\cup\{\gamma_0\},
  K\cup\{\gamma_1\},\ldots,
  K\cup\{\gamma_{S+H}\}}
                                                               \tag{1.2}
\]

has length \(S+H+1\) and represents, for every
\(0\le q\le H\) and \(0\le i\le S-q\), both

\[
 \bigcap_{t=0}^{q}X_{i+t}
 \quad\hbox{and}\quad
 \bigcup_{t=0}^{q}X_{i+t}.                         \tag{1.3}
\]

#### Proof

Sliding the active window gives

\[
 \bigcap_{t=0}^{q}X_{i+t}
 =K\cup\{\gamma_{i+q},\ldots,\gamma_{i+H}\},       \tag{1.4}
\]

and

\[
 \bigcup_{t=0}^{q}X_{i+t}
 =K\cup\{\gamma_i,\ldots,\gamma_{i+H+q}\}.         \tag{1.5}
\]

The union of positions \(a,\ldots,b\) in (1.2) is exactly
\(K\cup\{\gamma_a,\ldots,\gamma_b\}\). Use
\((a,b)=(i+q,i+H)\) for (1.4) and
\((a,b)=(i,i+H+q)\) for (1.5). Every entry is nonzero. \(\square\)

The overhead over the \(S+1\) owner positions is exactly \(H\), independent
of the number of local depth-\(H\) windows.

## 2. The central-marker sector is already optimal

Fix \(s\ge1\), a nonempty common base \(K\), and pairwise distinct labels
\(\ell_1,\ldots,\ell_s,r_1,\ldots,r_s\) outside \(K\). Put

\[
 T_{a,b}
 =K\cup\{\ell_1,\ldots,\ell_a\}
    \cup\{r_1,\ldots,r_b\},
 \qquad 0\le a,b\le s.                             \tag{2.1}
\]

This is the target family of one fixed-core open wreath sector after
absorbing its common central active label into \(K\) and reversing its
left labels: its consecutive intersections and unions are precisely the
\((s+1)^2\) sets \(T_{a,b}\).

### Theorem 2.1 (exact local optimum)

Every nonzero literal word representing all sets in (2.1) has length at
least

\[
 \boxed{2s+1}.                                      \tag{2.2}
\]

The central-marker word attains equality.

#### Proof

Choose a witness for \(T_{0,0}=K\). At least one position in it contains
no active label; call one such position neutral.

For each \(1\le i\le s\), a witness for \(T_{i,0}\) contains a letter
\(E_i\) with \(\ell_i\in E_i\). Since every letter in that witness is a
subset of \(T_{i,0}\), \(E_i\) contains no \(r\)-label and no \(\ell_j\)
with \(j>i\). The positions \(E_1,\ldots,E_s\) are distinct: if \(i<j\),
then \(E_j\) contains \(\ell_j\), whereas every letter in a witness for
\(T_{i,0}\) excludes \(\ell_j\).

Similarly, witnesses for \(T_{0,j}\), \(1\le j\le s\), give \(s\)
distinct positions \(F_j\) containing \(r_j\), containing no
\(\ell\)-label, and distinct from every \(E_i\). The neutral position is
different from all of them. Hence the word has at least \(1+s+s=2s+1\)
positions.

Equality is attained by the word
\[
 \{\ell_s\},\ldots,\{\ell_1\},K,
 \{r_1\},\ldots,\{r_s\}.
\]
Every \(T_{a,b}\) is the union of the corresponding interval through the
central \(K\)-position. \(\square\)

Thus the factor two of an isolated sector is genuine. The global
\(S+O(H)\) target can only come from sharing active positions between
adjacent sectors.

## 3. Canonical erosion witnesses cannot survive a short run

Let a word have integer-indexed positions and fix \(H\ge1\). Suppose the
designated witness for owner \(X_t\) is always

\[
 J_t=[t-H,t].                                      \tag{3.1}
\]

For a coordinate \(x\), let
\[
 P_x=\{j:x\hbox{ belongs to the word letter at position }j\}.
\]

### Theorem 3.1 (fixed-witness short-run obstruction)

The set of owner times whose designated witnesses contain \(x\) is

\[
 \boxed{
  \{t:J_t\cap P_x\ne\varnothing\}
  =\bigcup_{p\in P_x}[p,p+H].}                     \tag{3.2}
\]

Consequently every nonempty connected positive run of \(x\) in the owner
sequence has at least \(H+1\) owner times. No assignment of coordinates to
the existing erosion positions can represent a positive run of length at
most \(H\) while retaining (3.1).

#### Proof

The union of the letters in \(J_t\) contains \(x\) exactly when some
\(p\in P_x\) satisfies \(t-H\le p\le t\), equivalently
\(p\le t\le p+H\). This is (3.2). Every connected component of a union of
integer intervals \([p,p+H]\) contains at least \(H+1\) integers.
\(\square\)

The obstruction already uses singleton owners, before deeper targets are
requested. An integrated compiler must move owner witnesses as well as
lower and upper witnesses.

## 4. Exact coefficient-one boundary

There is one useful PBBS-specific contrast.  Let
\(X_0,\ldots,X_S\) be any Johnson path, and suppose it has an internally
bounded positive coordinate run \([a,b]\) of minimum length
\(\ell=b-a+1\).  Then

\[
 \boxed{
  \bigcap_{i=a-1}^{b}X_i
  =
  \bigcap_{i=a}^{b+1}X_i.}                         \tag{4.1}
\]

Indeed, if \(x\) is the coordinate of the run and
\(C=\bigcap_{i=a}^{b}X_i\), the entering transition shows
\(C\cap X_{a-1}=C-\{x\}\), and the leaving transition similarly gives
\(C\cap X_{b+1}=C-\{x\}\).  Both displayed windows are floor-correct:
an internally bounded run strictly inside either one would have length
less than \(\ell\), contradicting the choice of \([a,b]\).

Consequently, injectivity of the floor-correct consecutive-intersection
map at every depth \(1,\ldots,H\) forbids every internal positive run of
length at most \(H\), and the ordinary endpoint-capped erosion compiler
then applies.  At depth one this is exactly why the actual
complement-projected PBBS path escapes the star obstruction: its lower
edge colours are intervening exact middle owners and are distinct.
At larger depths global injectivity is arithmetically unavailable, so the
remaining issue is structured, floor-balanced collision rather than a
black-box Johnson compiler.

Long no-overtaking blocks have the exact \(S+H+1\) compiler (1.2). A short
fixed-core return cannot be compressed below \(2s+1\) in isolation. The
canonical erosion alignment cannot absorb even one short return.

Therefore a successful PBBS proof must splice active-coordinate orders of
successive returns into long collars and change witness alignment across
their boundaries. The admissible \(o(W)\) loss is the total unshared collar
boundary, not the sum of local sector lengths.

This note does not prove that canonical PBBS returns admit such a splice.
It proves that this global active-order sharing is the unique surviving
local geometry after the two exact barriers above.
