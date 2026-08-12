# One common-core tight-path fusion theorem would imply constant one

Date: 2026-07-26

This note packages the independently audited common-core atlas into one
integral statement. Unlike separate rankwise Hall matchings, the
hypothesis below chooses one actual ordered tail and one nested tag
history per critical top.

## 0. Critical parameters

Put

\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
\]

choose a calibrated critical integer \(H\), and write

\[
M=m+H,\qquad s=m-H,\qquad
N=N_H,\qquad L=m-3H+1,\qquad
\Lambda={W\over N}.
\]

The exact calibration hypotheses are

\[
H=(1+o(1))\sqrt{m\log m},\qquad m>4H,
\tag{0.1a}
\]

and, for fixed constants \(c_0,C_0>0\),

\[
L+c_0H\le\Lambda\le m+C_0H.
\tag{0.1b}
\]

For example, \(H=\lfloor\sqrt{m\log m}\rfloor\) satisfies these
conditions for all sufficiently large \(m\).  The weaker assertion
\(H=(1+o(1))\sqrt{m\log m}\) by itself is not enough: an unbounded
additive displacement on the \(\sqrt{m/\log m}\) scale can change
\(\Lambda\) by a nonconstant factor and destroy the coefficient-one
ledger.

Choose the fixed \(2H\)-cores \(Q_U\subset U\) supplied by the audited
common-core theorem, one for every \(M\)-top
\(U\in\binom{[2m]}M\). Define

\[
b_0=L
\]

and, for \(1\le q<H\),

\[
b_q=\min\left\{L-1,\,
\max\left\{0,\left\lfloor\frac{N_q}{N}\right\rfloor-1\right\}
\right\}.                                                       \tag{0.1}
\]

The sequence \(b_0,b_1,\ldots,b_{H-1}\) is nonincreasing.

## 1. The sole integral hypothesis

### Common-core tight-path fusion (CCTPF)

For every top \(U\), there are:

1. an order of \(Q_U\);
2. an order of \(S_U=U\setminus Q_U\); and
3. a stopping tag \(d_U(j)\in\{0,\ldots,H-1\}\) on each of the
   \(L\) core-safe phases \(1\le j\le L\),

such that:

\[
\left|\{j:d_U(j)\ge q\}\right|=b_q
\qquad(0\le q<H),                                               \tag{1.1}
\]

and the following global injectivity conditions hold.

* The \(LN\) middle masks of all retained phases are pairwise distinct.
* For every \(1\le q<H\), the lower depth-\(q\) masks of the active
  phases \(d_U(j)\ge q\) are pairwise distinct over all \(U,j\).
* For every \(1\le q<H\), the upper depth-\(q\) masks of the same
  active phases are pairwise distinct over all \(U,j\).

All masks here are the literal truncated-chain masks of the one
core-safe promotion path determined by the two orders. Thus (1.1) is
one nested phase history, not a collection of unrelated rank
matchings.

## 2. Conditional coefficient-one theorem

### Theorem 2.1

If CCTPF holds for all sufficiently large \(m\), then

\[
\boxed{\nu(2m)\le(1+o(1))W.}                                   \tag{2.1}
\]

The standard trimmed lift then gives the same constant for odd
dimensions, and hence the constant-one conjecture.

#### Proof

For each top, the retained phases are one literal directed promotion
path.  Here is the exact linearization.  Let \((X_i)\) be the full
promotion-cycle row of middle owners in that top, indexed so the retained
phases are the \(L\) consecutive indices \(i_0,\ldots,i_0+L-1\), and
define the delayed atoms

\[
B_j=\bigcap_{a=0}^{H}X_{j-a}.
\tag{2.2a}
\]

The cyclic interval owner row has \(G_H+P_H\): every segment of at most
\(H\) transitions is a Johnson geodesic, and every nonconstant positive
coordinate run has length \(m\ge H+1\).  Therefore the exact delayed-atom
identities give

\[
\bigcap_{t=0}^{q}X_{i+t}
 =\bigcup_{j=i+q}^{i+H}B_j,
\qquad
\bigcup_{t=0}^{q}X_{i+t}
 =\bigcup_{j=i}^{i+H+q}B_j
\tag{2.2b}
\]

for every \(0\le q\le H\).  Up to the common phase convention, these
are exactly the lower and upper masks of the full promotion states.  Emit

\[
B_{i_0},B_{i_0+1},\ldots,B_{i_0+L-1+2H}
\tag{2.2c}
\]

and delete empty atoms.  This has at most \(L+2H\) entries and covers
every active tagged trace of every retained phase.  (It may also cover
inactive traces, which only reduces the later repair.)

Across all tops, the retained middle mass is \(LN\). By middle
injectivity, exactly \(W-LN\) middle masks are absent. Append those masks
literally. The middle baseline plus all collars is therefore at most

\[
LN+(W-LN)+2HN=W+2HN.                                           \tag{2.2}
\]

At signed depth \(q\), (1.1) gives exactly \(b_qN\) active
occurrences. Global injectivity covers that many distinct lower targets
and that many distinct upper targets.  Thus the required repair is *at
most* \(N_q-b_qN\) on either side; extra inactive traces covered by
(2.2c) may only help.  No phase has tag \(H\), so append both entire
boundary layers at \(q=H\) literally, at cost \(2N\). The total
signed-mask repair is therefore at most

\[
2N+2\sum_{q=1}^{H-1}(N_q-b_qN).                               \tag{2.3}
\]

The audited common-core ledger proves

\[
(W-LN)+2N+2\sum_{q=1}^{H-1}(N_q-b_qN)
 =O(H^{3/2}N)=o(W).                                             \tag{2.4}
\]

Also

\[
HN=O\left(\frac{H}{m}W\right)=o(W).                            \tag{2.5}
\]

Finally append the established product-SCD exterior word below
rank \(m-H\) and above rank \(m+H\).  More precisely, take its cutoff
parameter \(r=m-H-1\); it covers every nonempty rank at most \(m-H-1\)
or at least \(m+H+1\), exactly the complement of the compiled central
band. Its length is

\[
O\!\left(e^{-H^2/(8m)}W\right)=o(W).                           \tag{2.6}
\]

Equations (2.2)--(2.6) give a literal contiguous-OR word of length
\(W+o(W)\), proving (2.1).

For completeness, the trimmed one-coordinate lift satisfies
\(\nu(2m+1)\le2\nu(2m)\), while

\[
\binom{2m+1}{m}={2m+1\over m+1}\binom{2m}{m}.
\]

Hence

\[
{2W\over\binom{2m+1}{m}}
={2(m+1)\over2m+1}=1+O(1/m),
\]

so the same coefficient one holds in odd dimensions. \(\square\)

## 3. What is already unconditional

The following parts of CCTPF are separately proved with the same fixed
cores.

1. There is an integral Hall assignment of \(L\) distinct compatible
   middle masks to every top, with no global repeats.
2. At every signed rank there is a separate integral Hall assignment
   of \(b_q\) compatible targets per top, with aggregate
   \(O(H^{3/2}N)=o(W)\) holes.
3. Every top has literal core-safe paths of \(L\) consecutive phases,
   and any nested histogram (1.1) fits on those phases.
4. The fixed-core tagged literal-path configuration has an exact
   feasible fractional point satisfying every combined nonnegative
   target-capacity inequality.
5. For any one chosen path, all active signed traces are already
   injective inside that top.

The only unproved passage is simultaneous **global** injectivity after
one path and one nested phase set are chosen for each top. In
configuration-hypergraph language, CCTPF is an integral
root-saturating matching in the fixed-core path catalogue. In
chronology language, it is the globally correlated tight-path fusion
gate. No scalar capacity, separate Hall, profile, low-degree character,
or local integrality condition remains.
