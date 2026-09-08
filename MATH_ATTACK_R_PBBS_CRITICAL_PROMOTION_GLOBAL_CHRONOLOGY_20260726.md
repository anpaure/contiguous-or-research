# PBBS chronology at the critical promotion scale: exact FIFO extraction, linear residence defect, and the surviving global braid

Date: 2026-07-26

Method: pure hand mathematics.  No computation, finite search, solver, or
web input is used.  The PBBS parity convention and every off-by-one
constant in the decisive return equation were independently audited.

## 0. Outcome

Write

\[
 B_m=\operatorname {Cat}_m,
 \qquad W_e=\binom{2m}{m}=(m+1)B_m,
 \qquad W_o=\binom{2m+1}{m}=(2m+1)B_m.
 \tag{0.1}
\]

The even and odd normalizations in (0.1) are not interchangeable.  The
tuned promotion rings live on \([2m]\), whereas the native PBBS return
word lives on \([2m+1]\).

Let

\[
 H_0=\lfloor\sqrt{m\log m}\rfloor,
 \qquad M=m+H,
 \qquad N_H=\binom{2m}{m-H}.
 \tag{0.2}
\]

The principal conclusions are as follows.

1.  There is an exact local criterion.  In any strongly geodesic
    Johnson chronology

    \[
    X_{t+1}=X_t-\{d_t\}+\{a_t\},
    \]

    the height-\(H\) future top is stationary from phase \(t\) to
    phase \(t+1\) if and only if

    \[
    \boxed{d_t=a_{t+H}.}                         \tag{0.3}
    \]

    A closed component is a literal promotion ring only when (0.3)
    holds at every phase **and** its \(m+H\) arrival labels are a
    permutation of the common top.  Thus local strong fans do not by
    themselves give a promotion frame.

2.  In the audited PBBS convention, (0.3) is exactly the omitted-label
    return

    \[
    \lambda_{i+2t+1}=\lambda_{i+2t+2H},          \tag{0.4}
    \]

    of ordinary gap \(2H-1\), hence first-return shell \(H-1\).
    The complementary orientation uses gap \(2H+1\), shell \(H\).

3.  There is an unconditional critical-height obstruction, even though
    the mass of the single predetermined critical shell is unknown.
    For every sequence \(L_m\to\infty\) with

    \[
    L_m=o\!\left(\sqrt{m/\log m}\right),
    \]

    some

    \[
    H\in[H_0+1,H_0+L_m]                         \tag{0.5}
    \]

    satisfies

    \[
    (m+H)N_H=(1+o(1))W_e                       \tag{0.6}
    \]

    and has only \(o(W_e)\) native strong PBBS starts capable of
    satisfying (0.3), in either orientation.  Consequently the native
    start-incidence residence defect is linear:

    \[
    \boxed{\Delta_H^{\rm res}=(1-o(1))W_o.}     \tag{0.7}
    \]

    Any native rebundling of \(W_o-o(W_o)\) phase occurrences, or any
    collar-preserving odd-to-even projection of \(W_e-o(W_e)\) phase
    occurrences, must change at least

    \[
    \boxed{b\ge(1-o(1)){T\over H}}              \tag{0.8}
    \]

    successor edges, where \(T\) is the retained phase mass.  A changed
    edge can repair \(H+1\) consecutive
    FIFO tests, so (0.8), not \(\Omega(W_e)\), is the sharp conclusion
    obtainable from residence incidence.

4.  The canonical infinity-cut MSW/PBBS paths have an even more explicit
    defect.  Exactly

    \[
    \boxed{(m-H)B_m=(1-o(1))W_e}                \tag{0.9}
    \]

    internal FIFO tests fail, and any fixed-top rebundling retaining the
    inherited successor order outside seams needs

    \[
    B_m\left\lceil{m+1\over H+1}\right\rceil
      =(1-o(1)){W_e\over H}                     \tag{0.10}
    \]

    inherited path pieces.  Independently collared repairs therefore
    cost \(\Omega(W_e)\).  This is a changed-successor/local-collar
    obstruction, not an extra-letter obstruction against one globally
    compiled braid.

5.  A genuinely single global cyclic order is ruled out in the literal
    middle layer.  If every critical top restricts the same ambient cyclic
    order, its middle support has size at most

    \[
    2m\binom{2m-H}{m}\le 2m\,2^{-H}W_e=o(W_e).
    \tag{0.11}
    \]

    Hence its actual middle holes and collision excess are both
    \((1-o(1))W_e\).  The same holds for any library of
    \(L=o(2^H/m)\) ambient orders.

6.  The positive scalar fact is exact: the infinity-cut paths contain
    \((1+o(1))W_e/H\) clean \(H\)-transition promotion segments, which
    is precisely the number demanded by the critical rings.  However,
    successive segments on one ring must have ordered deletion/insertion
    overlap \(H-o(H)\) on average, and the raw MSW factor has no
    full-overlap same-top continuation.  Thus supply is not the missing
    theorem; ordered, top-resolved cycle fusion is.

The proved obstruction therefore closes direct same-row residence,
bounded or polynomially many master frames, and separately collared local
switches.  It does **not** close a growing, zero-monodromy, cross-top braid
which absorbs \(\Theta(W_e/H)=o(W_e)\) changed successors in one literal
construction.  Such a braid must solve the ordered-overlap, owner, and
all-depth target ledgers simultaneously.

## 1. Critical promotion normalization

For \(0\le h<m\), put

\[
 T_h=(m+h)\binom{2m}{m-h}.                      \tag{1.1}
\]

The exact ratio is

\[
 {T_{h+1}\over T_h}={m-h\over m+h}.            \tag{1.2}
\]

For \(h=o(m^{2/3})\), the product formula gives

\[
\begin{aligned}
 \log {\binom{2m}{m-h}\over W_e}
 &=\sum_{j=0}^{h-1}
   \left(\log(1-j/m)-\log(1+(j+1)/m)\right)\\
 &=-{h^2\over m}+O\!\left({h^3\over m^2}+{h\over m}\right).
                                                               \tag{1.3}
\end{aligned}
\]

Consequently, uniformly for

\[
 h=\sqrt{m\log m}+o\!\left(\sqrt{m/\log m}\right),
\]

one has

\[
 {T_h\over W_e}
 =(1+h/m)\,m\,
  \exp\!\left(-{h^2\over m}+o(1)\right)
 =1+o(1).                                      \tag{1.4}
\]

Thus any height in (0.5) has the correct coefficient-one scalar mass,
whether \(T_H\) lies just above or just below \(W_e\).  The discrepancy
is \(o(W_e)\) and may be put in the permitted exceptional ledger.

For a top \(U\in\binom{[2m]}{M}\), an oriented cyclic frame

\[
 c=(c_0,c_1,\ldots,c_{M-1})                     \tag{1.5}
\]

gives the middle owners

\[
 X_t=U\setminus\{c_t,c_{t+1},\ldots,c_{t+H-1}\}.
                                                               \tag{1.6}
\]

There are \(M\) phases per top and \(N_H\) tops.  Equation (1.4) is
exactly the assertion that their total phase mass is \(W_e+o(W_e)\).

## 2. The exact sliding-top/FIFO theorem

### Theorem 2.1 (one-step top derivative)

Let \((X_t)\) be a Johnson chronology of rank \(m\):

\[
 X_{t+1}=X_t-\{d_t\}+\{a_t\}.                  \tag{2.1}
\]

Fix \(H\ge1\).  Suppose the two blocks

\[
 X_t,\ldots,X_{t+H}
 \quad\hbox{and}\quad
 X_{t+1},\ldots,X_{t+H+1}                       \tag{2.2}
\]

are strongly Johnson-geodesic, meaning that each has intersection rank
\(m-H\) and union rank \(m+H\).  Put

\[
 U_t=\bigcup_{j=0}^{H}X_{t+j}.                  \tag{2.3}
\]

Then

\[
 \boxed{U_{t+1}=U_t-\{d_t\}+\{a_{t+H}\}.}      \tag{2.4}
\]

In particular,

\[
 \boxed{U_{t+1}=U_t\iff d_t=a_{t+H}.}           \tag{2.5}
\]

#### Proof

Strong geodesicity of the first block says that its \(H\) deleted
coordinates are distinct members of \(X_t\), while its \(H\) inserted
coordinates are distinct coordinates outside \(X_t\).  Hence

\[
 U_t=X_t\mathbin{\dot\cup}\{a_t,\ldots,a_{t+H-1}\}.  \tag{2.6}
\]

Likewise,

\[
 U_{t+1}=X_{t+1}\mathbin{\dot\cup}
          \{a_{t+1},\ldots,a_{t+H}\}.           \tag{2.7}
\]

Substituting (2.1) into (2.7) and comparing with (2.6) proves (2.4).
Both sets have size \(m+H\), so (2.4) gives (2.5). \(\square\)

### Theorem 2.2 (literal promotion-frame criterion)

Let a closed Johnson component have length \(M=m+H\).  Assume every two
adjacent height-\(H\) blocks satisfy Theorem 2.1.  The component is the
middle chronology of one oriented cyclic frame on a top \(U\) if and
only if

1. \(d_t=a_{t+H}\) for every \(t\in\mathbb Z_M\); and
2. \((a_0,a_1,\ldots,a_{M-1})\) is a permutation of \(U\).

In that case

\[
 X_t=U\setminus\{a_t,a_{t+1},\ldots,a_{t+H-1}\}. \tag{2.8}
\]

#### Proof

Condition 1 and Theorem 2.1 make all \(U_t\) equal to one top \(U\).
Equation (2.6), with \(|U\setminus X_t|=H\), gives (2.8).  Condition 2
makes the arrival word a cyclic ordering of every coordinate of \(U\),
so (2.8) is a literal promotion ring.  Conversely, (1.6) deletes
\(c_{t+H}\) and inserts \(c_t\) in the appropriate cyclic indexing;
equivalently its departure at phase \(t\) is its arrival at phase
\(t+H\).  Its arrival word is the cyclic frame itself. \(\square\)

The global permutation condition in Theorem 2.2 is essential.  A supply
of isolated clean starts, or even local constancy of the top, does not
prove a promotion ring.

## 3. PBBS translation: the correct shell is \(H-1\)

Let \(n=2m+1\).  On a PBBS orbit write \(A_i\) for the consecutive
rank-\(m\) states and

\[
 \lambda_i=[n]\setminus(A_i\cup A_{i+1})        \tag{3.1}
\]

for the omitted label.  The audited recurrence is

\[
 \boxed{A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.}
                                                               \tag{3.2}
\]

Fix a parity and put \(X_t=A_{i+2t}\).  Then

\[
 d_t=\lambda_{i+2t+1},
 \qquad a_t=\lambda_{i+2t}.                    \tag{3.3}
\]

At a clean pair of starts, Theorem 2.1 becomes

\[
 \boxed{
 \lambda_{i+2t+1}=\lambda_{i+2t+2H}.}          \tag{3.4}
\]

The two occurrences in (3.4) have ordinary omitted-label gap \(2H-1\).
Moreover the gap is a first return.  Indeed, strong geodesicity makes the
deleted labels distinct original coordinates and the inserted labels
distinct coordinates outside the first owner.  After
\(\lambda_{i+2t+1}\) is deleted, it cannot occur among any intermediate
insertion or deletion labels in the two clean blocks.  Its first possible
return is the final label in (3.4).

With the native convention that gap \(2s+1\) is shell \(s\), (3.4) is
therefore shell

\[
 \boxed{s=H-1.}                                  \tag{3.5}
\]

For the complemented parity chronology, (3.2) reads

\[
 A^c_{i+2}=A^c_i-\{\lambda_i\}+\{\lambda_{i+1}\},
\]

and the corresponding equation is

\[
 \lambda_{i+2t}=\lambda_{i+2t+2H+1},            \tag{3.6}
\]

of gap \(2H+1\), shell \(H\).  Equations (3.4) and (3.6) are the two
boundary orientations; merging them into one shell is an off-by-two
error.

Let \(M_{m,s}\) be the normalized number of PBBS roots whose first
omitted-label return has shell \(s\).  The exact mass identity is

\[
 \sum_{s\ge0}M_{m,s}=B_m.                       \tag{3.7}
\]

Let \(G^-_{m,H}\) be the physical number of starts satisfying the strong
geodesicity hypotheses and (3.4).  A shell return need not make every
label in the whole fan clean, so only the following direction is valid:

\[
 \boxed{G^-_{m,H}\le nM_{m,H-1}.}               \tag{3.8}
\]

Similarly,

\[
 \boxed{G^+_{m,H}\le nM_{m,H}.}                 \tag{3.9}
\]

Thus the native odd failed-start defects obey

\[
\begin{aligned}
 \Delta^-_{m,H}:=W_o-G^-_{m,H}
   &\ge n(B_m-M_{m,H-1}),\\
 \Delta^+_{m,H}:=W_o-G^+_{m,H}
   &\ge n(B_m-M_{m,H}).                         \tag{3.10}
\end{aligned}
\]

For the single predetermined critical value
\(H=\lfloor\sqrt{m\log m}\rfloor\), neither

\[
 M_{m,H-1}=B_m-o(B_m)                           \tag{3.11}
\]

nor its negation is presently proved for the actual PBBS word.  The
exact renewal recurrence, the shallow shell values, and the Kac first
moment do not decide (3.11).  The audited two-tail completion constructs
formal shell histograms satisfying all those scalar constraints while
placing zero mass at a prescribed critical shell.  That completion is a
no-go for a deduction from the scalar identities; it is not a realized
PBBS counterexample.

## 4. An unconditional near-critical shell with linear defect

### Theorem 4.1 (critical-window shell sparsification)

Let \(L_m\to\infty\) and

\[
 L_m=o\!\left(\sqrt{m/\log m}\right).           \tag{4.1}
\]

Then some integer \(H\in[H_0+1,H_0+L_m]\) satisfies

\[
 M_{m,H-1}+M_{m,H}\le {2B_m\over L_m}.          \tag{4.2}
\]

At that height, (0.6) holds and

\[
 G^-_{m,H}+G^+_{m,H}=o(W_o).                    \tag{4.3}
\]

#### Proof

As \(H\) runs through the interval, every shell index occurs in at most
two of the sums \(M_{m,H-1}+M_{m,H}\).  Therefore (3.7) gives

\[
 \sum_{H=H_0+1}^{H_0+L_m}
   (M_{m,H-1}+M_{m,H})\le2B_m.                  \tag{4.4}
\]

Pigeonhole proves (4.2).  Condition (4.1) puts this \(H\) in the uniform
range of (1.4), proving (0.6).  Equations (3.8), (3.9), and
\(L_m\to\infty\) prove (4.3). \(\square\)

Reversing the time orientation of a PBBS component does not evade this
count.  A cyclic forward gap becomes the backward gap based at its other
endpoint, so the aggregate first-return shell census is unchanged.
Spatial deck shifts also merely permute the phase starts.  Hence, if
\(G^{\rm any}_{m,H}\) is the set of native starts good in any of the
allowed time/parity orientations, then at the height of Theorem 4.1

\[
 |G^{\rm any}_{m,H}|=o(W_o),\qquad
 \Delta_H^{\rm res}:=W_o-|G^{\rm any}_{m,H}|
 =(1-o(1))W_o.                                  \tag{4.4a}
\]

This height may depend on \(m\).  That is legitimate for a
coefficient-one construction: its scalar ring mass is still
\(W_e+o(W_e)\).  The theorem does not identify which member of the short
critical interval works.

For an explicit rate, take

\[
 L_m=\lfloor\log\log m\rfloor                  \tag{4.4b}
\]

once this is positive.  Then some height in (0.5) satisfies

\[
 G^-_{m,H}+G^+_{m,H}
 \le {2W_o\over\lfloor\log\log m\rfloor}.       \tag{4.4c}
\]

Thus the two audited parity directions together have residence defect at
least

\[
 W_o\left(1-{2\over\lfloor\log\log m\rfloor}\right),
                                                               \tag{4.4d}
\]

before taking the asymptotic form (4.4a).  Allowing time reversal changes
only the harmless absolute constant in (4.4c), because it permutes the
same cyclic gaps.

### Theorem 4.2 (seam dilution inequality)

Suppose \(T\) selected PBBS phase occurrences are placed in promotion
rings.  Let \(b\) be the number of final successor edges which are not
the corresponding native PBBS successor.  Let \(G\) be the number of
native starts which are both strongly geodesic and satisfy the required
FIFO equation.

Then

\[
 \boxed{T-(H+1)b\le G,}                         \tag{4.5}
\]

and hence

\[
 \boxed{b\ge {T-G\over H+1}.}                  \tag{4.6}
\]

#### Proof

The FIFO comparison at phase \(t\) uses the \(H+1\) transitions

\[
 t,t+1,\ldots,t+H.                              \tag{4.7}
\]

If all of them are native, the final ring follows the native PBBS
chronology through both adjacent height-\(H\) fans.  Since a promotion
ring satisfies Theorem 2.1, this phase must be one of the \(G\) native
good starts.  A changed successor lies in exactly \(H+1\) cyclic test
collars, or fewer at a linear boundary.  Thus at most \((H+1)b\) tests
can avoid injection into the native good-start set.  This proves (4.5).
\(\square\)

The factor \(H+1\) is sharp at the interval-hitting level.  The formerly
tempting inequality \(b\ge T-G\) is false.

Apply Theorems 4.1 and 4.2 natively with
\(T=W_o-o(W_o)\).  Equation (4.3) gives

\[
 \boxed{b\ge(1-o(1)){W_o\over H}.}              \tag{4.8}
\]

If a separately proved owner-injective odd-to-even projection or aligned
trim selects \(W_e-o(W_e)\) native phase occurrences and preserves every
seam-free \((H+1)\)-transition collar, the same proof gives

\[
 b\ge(1-o(1)){W_e\over H}.                       \tag{4.9}
\]

No such common projection is inferred merely from the native count.  The
unconditional even statement is instead Corollary 5.2 below.  This proves
the scoped form of (0.7)--(0.8).  Notice that (4.8)--(4.9) count changed
successors, not appended letters.  A global exact braid may realize a
changed successor at baseline cost; the theorem only says that the braid
must correlate \(\Theta(T/H)\) such changes.

## 5. The infinity-cut chronology has explicit linear FIFO defect

Cut an exact odd wreath factor at one distinguished coordinate.  The
result is a partition of the even middle layer into

\[
 B_m={W_e\over m+1}                             \tag{5.1}
\]

complement-ended geodesic paths

\[
 X_0,X_1,\ldots,X_m.                            \tag{5.2}
\]

On one path there is a coordinate order

\[
 (\delta_0,\ldots,\delta_{m-1},
   \eta_0,\ldots,\eta_{m-1})                    \tag{5.3}
\]

of \([2m]\) such that

\[
 X_{t+1}=X_t-\{\delta_t\}+\{\eta_t\}.          \tag{5.4}
\]

The deletion and insertion alphabets in (5.3) are disjoint.

### Theorem 5.1 (exact infinity-cut residence defect)

For every \(0\le t\le m-H-1\), the two adjacent height-\(H\) fans are
strongly geodesic but fail the FIFO equation:

\[
 \delta_t\ne\eta_{t+H}.                        \tag{5.5}
\]

Thus every path has exactly \(m-H\) failed internal top-stability tests,
and the complete path factor has

\[
 \boxed{F_{m,H}=(m-H)B_m}                       \tag{5.6}
\]

such tests.

#### Proof

All coordinates in (5.3) are distinct, so every subpath of length at
most \(m\) is strongly geodesic.  At phase \(t\), Theorem 2.1 asks for
\(d_t=a_{t+H}\), which is precisely (5.5) with equality in place of
inequality.  Disjointness of the two alphabets makes equality impossible.
There are \(m-H\) permitted values of \(t\) per path. \(\square\)

The ratio is

\[
 {F_{m,H}\over W_e}={m-H\over m+1}=1-o(1)      \tag{5.7}
\]

at the critical height.  Reversing paths independently or globally
relabeling coordinates does not change the argument.

### Corollary 5.2 (fixed-top slicing and changed successors)

A run of \(s\) consecutive inherited path owners has union rank

\[
 m+s-1.                                        \tag{5.8}
\]

If it lies in one promotion top of rank \(m+H\), then \(s\le H+1\).
Consequently any rebundling of all inherited owners into fixed-top rings
uses at least

\[
 \boxed{
 P_{m,H}=B_m\left\lceil{m+1\over H+1}\right\rceil}
                                                               \tag{5.9}
\]

maximal inherited runs, and therefore at least \(P_{m,H}\) non-inherited
successor edges in the final cyclic rings.  In particular,

\[
 P_{m,H}=(1-o(1)){W_e\over H}.                  \tag{5.10}
\]

If \(e=o(W_e)\) original owner occurrences are discarded, the same
argument still gives at least

\[
 {W_e-e\over H+1}=(1-o(1)){W_e\over H}          \tag{5.11}
\]

maximal retained runs.

#### Proof

Formula (5.8) follows directly from (5.3)--(5.4): every new transition
adds one new coordinate to the union.  The fixed top has only \(H\)
coordinates beyond rank \(m\), proving \(s\le H+1\).  Partition each of
the \(B_m\) paths into maximal final-ring runs.  Each run has at most
\(H+1\) owners, giving (5.9).  Every run has a final outgoing edge which
is not its inherited path successor; these outgoing edges are distinct.
The discarded version follows by applying the same bound to the retained
owner mass. \(\square\)

If each changed successor is implemented by its own disjoint
radius-\(H\) collar, (5.10) forces \(\Omega(HP_{m,H})=\Omega(W_e)\)
copied positions.  This rigorously closes separately collared local
repair.  It does not refute the audited infinity-cut full-state lift,
whose one-promotion/rotor chronology is not a fixed-top promotion-ring
conversion, and it does not refute a common braid in which many seams
share one literal word.

## 6. The clean segment bank and the exact ordered fusion gate

Although full same-row residence fails, every inherited path contains
many clean promotion **segments**.

Fix a length-\(H\) geodesic segment beginning at phase \(t\).  Write

\[
\begin{aligned}
 d(e)&=(\delta_t,\delta_{t+1},\ldots,\delta_{t+H-1}),\\
 i(e)&=(\eta_t,\eta_{t+1},\ldots,\eta_{t+H-1}),\\
 K(e)&=X_t\setminus\{\delta_t,\ldots,\delta_{t+H-1}\},\\
 U(e)&=K(e)\mathbin{\dot\cup}d(e)\mathbin{\dot\cup}i(e).
                                                               \tag{6.1}
\end{aligned}
\]

Then \(|K(e)|=m-H\), \(|U(e)|=m+H\), and the owner sequence of \(e\)
is a literal height-\(H\) promotion segment inside \(U(e)\).

Splitting every path into consecutive length-\(H\) blocks supplies

\[
 \left\lfloor{m\over H}\right\rfloor B_m
 =(1+o(1)){W_e\over H}                          \tag{6.2}
\]

clean segments.  The discarded row tails have total owner mass
\(O(HB_m)=o(W_e)\), and the block endpoints have total mass
\(O(W_e/H)=o(W_e)\).  On the demand side,

\[
 N_H{m+H\over H}=(1+o(1)){W_e\over H}.          \tag{6.3}
\]

Thus the scalar segment supply is exactly right.

It is not freely stitchable.  The following is the exact missing
geometric condition.

### Theorem 6.1 (ordered-overlap criterion)

Suppose intact clean segments
\(e_1,\ldots,e_k\) occur disjointly in one promotion frame, in this
cyclic order.  If their phase starts are separated by \(H+g_j\), then

\[
 \sum_{j=1}^{k}g_j=M-kH.                        \tag{6.4}
\]

Whenever \(0\le g_j\le H\), one necessarily has the ordered identity

\[
 \boxed{
 \operatorname {suffix}_{H-g_j}d(e_j)
 =\operatorname {prefix}_{H-g_j}i(e_{j+1}).}    \tag{6.5}
\]

Conversely, the cyclic identities (6.5), together with the requirement
that the resulting cyclic superword uses every coordinate of one top
\(U\) exactly once, are sufficient for a literal promotion frame
containing all the segments.

#### Proof

Use the arrival-label cyclic word \((a_t)\) from Theorem 2.2.  A clean
segment \(e\) occupies the consecutive \(2H\)-block

\[
 i(e)\,d(e)                                     \tag{6.6}
\]

because the FIFO law identifies its departures with the arrivals
\(H\) phases later.  Two segment starts separated by \(H+g_j\) make the
last \(H-g_j\) letters of the first block coincide with the first
\(H-g_j\) letters of the next block, which is exactly (6.5).  Summing the
cyclic start separations gives (6.4).  Conversely, (6.5) glues all the
blocks consistently; if the glued cyclic word is a permutation of \(U\),
Theorem 2.2 supplies the literal ring. \(\square\)

Let \(\omega(e,f)\) be the largest ordered suffix-prefix overlap in
(6.5).  Every selected cyclic family obeys

\[
 \sum_j(H-\omega(e_j,e_{j+1}))\le M-kH.         \tag{6.7}
\]

If \(k=(1-o(1))M/H\), its average overlap is \(H-o(H)\).  If

\[
 k=\lfloor M/H\rfloor-O(1),                    \tag{6.8}
\]

then the average gap is

\[
 O(H^2/m)=O(\log m)                             \tag{6.9}
\]

at the critical height.

There is no raw full-overlap same-top continuation.  The terminal owner
of an intact segment occurs once in the exact factor, so its raw forward
continuation is the next segment on the same inherited path.  For
\(1\le s\le m-H\), (5.3)--(5.4) give

\[
 U_{t+s}=U_t-
 \{\delta_t,\ldots,\delta_{t+s-1}\}
 +\{\eta_{t+H},\ldots,\eta_{t+H+s-1}\},         \tag{6.10}
\]

and hence

\[
 d_J(U_t,U_{t+s})=s.                            \tag{6.11}
\]

Thus the unique raw continuation immediately leaves the top.  Global
coordinate conjugation preserves the entire overlap matrix \(\omega\)
and cannot create the missing same-top chains.  A positive construction
must alter continuations across rows and solve a cyclic
shortest-superstring problem, not merely a degree-balanced block matching.

## 7. Ambient-row inheritance is too sparse

For a cyclic order \(\pi\) on \([2m]\), let \(E_m(\pi)\) be its family
of cyclic length-\(m\) intervals.

### Lemma 7.1 (one-row/top intersection)

For every \(U\subset[2m]\) with \(|U|=m+H<2m\),

\[
 \boxed{|E_m(\pi|_U)\cap E_m(\pi)|\le H+1.}     \tag{7.1}
\]

#### Proof

Decompose \(U\) into cyclic runs in \(\pi\).  A length-\(m\) ambient
interval contained in \(U\) lies in one run.  Since \(|U|<2m\), at most
one run has length at least \(m\).  A run of length \(r\le m+H\)
contains \(r-m+1\le H+1\) such intervals. \(\square\)

If the frame chosen for each top is allowed to inherit owners from at
most \(s\) ambient PBBS/MSW rows, (7.1) certifies at most \(s(H+1)\) of
its \(M\) phases.  Across all tops the uncertified provenance mass is at
least

\[
 \boxed{
 D_{\rm prov}\ge [M-s(H+1)]_+N_H.}              \tag{7.2}
\]

Therefore \(D_{\rm prov}=o(W_e)\) requires

\[
 \boxed{
 s\ge(1-o(1)){M\over H+1}
   =\Omega\!\left(\sqrt{m/\log m}\right)}       \tag{7.3}
\]

rows per top.  One assigned PBBS row per top certifies only

\[
 (H+1)N_H=O(W_eH/m)=o(W_e)                     \tag{7.4}
\]

owner phases.  This is a provenance obstruction, not an actual-hole
bound: cross-row phases may still cover the middle layer.

## 8. A master global coordinate cycle has actual linear holes

The following is stronger than the provenance bounds because it counts
literal middle targets.

### Theorem 8.1 (single-master-cycle no-go)

Fix one cyclic order \(\pi\) of \([2m]\).  For every critical top \(U\),
use the restricted frame \(\pi|_U\).  For an \(m\)-set \(X\), let

\[
 g_1(X),\ldots,g_m(X)                           \tag{8.1}
\]

be the lengths of the complementary gaps between consecutive elements
of \(X\) in \(\pi\).  The exact load of \(X\) in all the restricted
frames is

\[
 \boxed{
 \mu_\pi(X)=\sum_{j=1}^{m}\binom{g_j(X)}{H}.}   \tag{8.2}
\]

Consequently

\[
 |\operatorname {supp}\mu_\pi|
 \le2m\binom{2m-H}{m}
 \le2m\,2^{-H}W_e=o(W_e).                       \tag{8.3}
\]

Since the total phase mass is \(T_H=W_e+o(W_e)\), both the middle hole
count and the floor-one collision excess are \((1-o(1))W_e\).

#### Proof

Write \(U=X\mathbin{\dot\cup}Y\), \(|Y|=H\).  The set \(X\) is a
length-\(m\) interval in \(\pi|_U\) exactly when all of \(Y\) lies in
one complementary gap of \(X\).  There are \(\binom{g_j(X)}H\) choices
in gap \(j\), proving (8.2).

If \(\mu_\pi(X)>0\), some ambient cyclic \(H\)-interval is disjoint from
\(X\).  There are \(2m\) such intervals, and for each one there are
\(\binom{2m-H}{m}\) possible \(X\).  This proves the first inequality
in (8.3).  Moreover

\[
 {\binom{2m-H}{m}\over\binom{2m}{m}}
 =\prod_{j=0}^{H-1}{m-j\over2m-j}\le2^{-H},     \tag{8.4}
\]

proving the second.  The hole count is \(W_e-|\operatorname{supp}\mu|\).
The collision excess is
\(T_H-|\operatorname{supp}\mu|\). \(\square\)

For a library of \(L\) master cyclic orders, the union of all possible
supports is at most

\[
 2mL\,2^{-H}W_e.                                \tag{8.5}
\]

Thus every \(L=o(2^H/m)\) library has the same linear actual-hole
obstruction.  This closes bounded and polynomial-size globally shared
coordinate-cycle libraries.  It does not close the Catalan-size,
root-dependent PBBS row catalogue.

## 9. Seam influence across all depths

Even a small seam set changes many chronological windows.  In a cyclic
ring of length \(M\), let \(b_i\ge1\) edges differ from a chosen PBBS
provenance.  Let \(u_{i,q}\) count phase starts whose next \(q\) edges
meet at least one seam.  Then

\[
 \boxed{u_{i,q}\ge\min\{M,b_i+q-1\}.}           \tag{9.1}
\]

Indeed, the affected starts are the union of \(b_i\) cyclic intervals of
length \(q\); clustering the seams consecutively minimizes the union and
gives \(b_i+q-1\) until saturation.

Relative to the unconditional even infinity-cut provenance, every final
cyclic ring has at least one seam because the inherited components are
open paths.  Alternatively, in a collar-preserving native odd model, a
proper critical top cannot be a whole PBBS component: coordinate
homomesy makes every native component length a multiple of \(2m+1\),
whereas \(M=m+H<2m+1\).  Under either stated provenance hypothesis every
critical ring has at least one seam.  Summing (9.1) over \(N_H\) even
rings and \(1\le q\le H\) gives

\[
\begin{aligned}
 \sum_i\sum_{q=1}^{H}u_{i,q}
 &\ge N_H{H(H+1)\over2}\\
 &=\left({1\over2}+o(1)\right)W_e\log m.        \tag{9.2}
\end{aligned}
\]

Equation (9.2) is a PBBS-provenance turnover count.  It is **not** an
actual-hole or extra-letter lower bound: the new seam-crossing windows may
cancel collisions or cover targets.  It shows why independent seam signs
are the wrong model.  Any successful operation must correlate a
superlinear number of depth-labelled window effects using only
\(\Theta(W_e/H)\) physical changed successors.

## 10. Quotient voltage forces zero monodromy on almost every top

There is one further exact restriction on a global PBBS operation.  In a
cyclic deck model with coordinate rotation \(\rho\), a quotient circuit
of deck voltage \(v\) lifts a top \(U\) to \(\rho^vU\).  Hence closure on
the same top requires

\[
 \boxed{\rho^vU=U.}                             \tag{10.1}
\]

If \(v\not\equiv0\) modulo the deck length \(N\), the top has nontrivial
rotational stabilizer.  A nonidentity rotation of \(N\) coordinates has
at most \(N/2\) coordinate orbits, so the total number of subsets fixed by
some nonidentity rotation is at most

\[
 N2^{N/2}.                                      \tag{10.2}
\]

At a central rank displaced by \(O(\sqrt{N\log N})\), the number of tops
is \(2^{N-o(N)}\).  Therefore (10.2) is an exponentially vanishing
fraction.  Almost every critical top requires

\[
 v\equiv0\pmod N.                               \tag{10.3}
\]

Zero voltage is only necessary.  The FIFO identities, ordered overlap,
arrival-label permutation, exact middle ownership, and all-depth shadow
ledgers remain separate conditions.

## 11. Precise proved/conditional boundary

The following statements are proved.

1.  The stationary-top equation is the exact FIFO law (2.5), and a
    literal frame additionally needs the global arrival permutation.
2.  On the forward PBBS parity, the law is shell \(H-1\), not shell
    \(H\); the complement parity is shell \(H\).
3.  At some height in every growing, asymptotically negligible critical
    interval, the native PBBS good-start supply is \(o(W_o)\), the
    residence-incidence defect is linear, and at least
    \((1-o(1))W_o/H\) native successors must change.  The even version
    requires a collar-preserving projection; the infinity-cut version is
    independently unconditional.
4.  The infinity-cut path factor has the exact failed-test count (5.6)
    and the exact inherited-run lower bound (5.9).
5.  Local independent radius-\(H\) seam compilation costs
    \(\Omega(W_e)\).
6.  The PBBS/MSW paths supply the correct scalar number
    \(W_e/H+o(W_e/H)\)
    of clean segments, but literal fusion imposes the ordered-overlap
    equations (6.4)--(6.7).
7.  One ambient row contributes at most \(H+1\) inherited phases to one
    top; a single master cycle, or any \(o(2^H/m)\)-size master library,
    has \((1-o(1))W_e\) actual middle holes.
8.  Almost every critical top requires zero deck monodromy.

The following statements are not proved.

1.  The size of the actual PBBS shell \(M_{m,H-1}\) at the single exact
    crossing height is not known.
2.  A shell return is not automatically a clean strong fan, and a clean
    stable fan is not automatically part of a length-\(m+H\) rainbow
    frame.
3.  The clean segment bank has not been distributed topwise with the
    ordered near-overlaps, exact owner packing, and cyclic closure required
    by Theorem 6.1.
4.  The \(\Theta(W_e/H)\) necessary even successor changes have not been
    compiled into a common literal braid at \(o(W_e)\) extra-letter cost.
5.  The resulting lower and upper shadows have not been shown to have
    aggregate holes and floor-collision excess \(o(W_e)\) through all
    critical depths.

Accordingly, PBBS chronology does not directly turn into critical cyclic
residence: its direct residence defect is linear at an admissible critical
height, and the obvious globally shared frame models have linear actual
holes.  The sole surviving PBBS route is a genuinely nonlocal,
root-dependent, zero-monodromy braid which rethreads
\(\Theta(W_e/H)\) seams while enforcing near-complete ordered block overlap.
The edge scale is compatible with coefficient one; the known local collar
scale is not.

## 12. Audit note

The decisive indexing and seam-dilution steps were audited independently.
The audit confirmed:

\[
 d_t=\lambda_{i+2t+1},\qquad
 a_t=\lambda_{i+2t},\qquad
 d_t=a_{t+H}\iff
 \lambda_{i+2t+1}=\lambda_{i+2t+2H},
\]

so the forward gap is \(2H-1\), and confirmed that one changed successor
contaminates \(H+1\), not one, top-stability tests.  It also independently
checked the infinity-cut count \((m-H)B_m\) and the lower bound
\(b\ge\lceil(m-H)B_m/(H+1)\rceil\).  No claim in this report upgrades a
provenance or changed-successor count to an actual-hole or extra-letter
count without a separate literal argument; Theorem 8.1 is the explicit
case where such an actual-hole argument is available.
