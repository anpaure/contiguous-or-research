# Canonical BTK terminal-pair recursion cannot give (O(W/m)) rotor paths

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, web input,
or probabilistic black box is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N_r=\binom{2m}{m-r},\qquad
 c_r=N_r-N_{r+1},
\tag{0.1}
\]

and retain the canonical BTK chains of native radius at least

\[
 q_0=\lceil a\sqrt m\rceil,
 \qquad a>0\text{ fixed}.
\tag{0.2}
\]

Tune the full rotor collar to

\[
 H=\left\lfloor\sqrt{m\log m}\right\rfloor.
\tag{0.3}
\]

The explicit terminal-suffix rotor matching is correct. It has

\[
 M_H=\binom{2m-2}{m-H-1}
 =\left(\frac14+o(1)\right)N_H
 =\left(\frac14+o(1)\right)\frac Wm
\tag{0.4}
\]

vertex-disjoint genuine radius-\(H\) rotor edges. Thus the exposed top
imbalance really is affordable.

It cannot, however, be recursively extended inside the canonical BTK SCD
to an \(O(W/m)\)-path forest using terminal replacements
\({**}\to01/10\). There are two exact reasons.

1. A canonical BTK signature is a word
   \[
   D_0*D_1*\cdots *D_{2r}
   \]
   with every \(D_i\) Dyck. For two consecutive free stars, the only
   canonical contraction is
   \[
   *D*\longmapsto0D1.
   \tag{0.5}
   \]
   The proposed opposite block \(1D0\) is not Dyck: immediately after
   its initial \(1\), its Dyck height is negative. In particular
   \(S10\) is never a canonical BTK signature when \(S\) is a complete
   prefix signature. Using the \(10\) shore changes the SCD or the local
   coordinate order.

2. Every legal contraction in (0.5) decreases native radius by one.
   Even if every such contraction is generously declared to be a legal
   rotor edge, every resulting path is strictly radius-decreasing. Hence
   its number \(p\) of paths obeys
   \[
   \boxed{
   p\ge\max_{r\ge q_0}c_r
    =\left(\kappa(a)+o(1)\right)\frac W{\sqrt m},}
   \tag{0.6}
   \]
   where
   \[
   \kappa(a)=
   \begin{cases}
   \sqrt{2/e},&0<a\le1/\sqrt2,\\[1mm]
   2ae^{-a^2},&a\ge1/\sqrt2.
   \end{cases}
   \tag{0.7}
   \]

Thus the monotone imbalance is \(\Theta(W/\sqrt m)\), not \(W/m\).
The two quantities of order \(W/m\)—the radius-zero Catalan layer and the
tuned top aggregate \(N_H\)—do not control the largest intermediate
radius layer.

For the direct radius-\(H\) hard-start compiler, (0.6) gives collar cost

\[
 \boxed{
 2Hp\ge\left(2\kappa(a)+o(1)\right)W\sqrt{\log m}.}
\tag{0.8}
\]

This is fatal for coefficient one. The explicit suffix matching saves only
\(M_H=\Theta(W/m)\) path starts and does not affect the dominant
\(W/\sqrt m\) radius cut.

More generally, if a proposed canonical-BTK forest has \(p\) paths and
uses \(b\) edges which do not strictly decrease native radius, then

\[
 \boxed{
 p+b\ge\max_{r\ge q_0}c_r.}
\tag{0.9}
\]

Consequently an \(O(W/m)\)-path construction must supply

\[
 b\ge\left(\kappa(a)+o(1)\right)\frac W{\sqrt m}
\tag{0.10}
\]

genuine horizontal or radius-increasing state transitions. The terminal
\(01\) contractions supply none, and the \(10\) alternative is not a
canonical signature. This is the sharp obstruction to the proposed
recursive matching. A positive BTK open-path compiler must use
state-compatible nonmonotone collar transitions, or leave the canonical
BTK decomposition through a second local frame.

The owner ledger is exact throughout: the retained chains have distinct
BTK middle owners, and the obstruction is solely a path-component cut. It
does not arise from owner duplication or from the tuned top leave.

## 1. Canonical BTK signatures

Use the BTK bracketing convention in which \(0\) is an opening symbol and
\(1\) a closing symbol. A chain signature of native radius \(r\) has the
unique form

\[
 \Sigma=D_0*D_1*\cdots *D_{2r},
\tag{1.1}
\]

where every \(D_i\) is a Dyck word, possibly empty. The \(2r\) star
positions are the free coordinates of the chain. Replacing the first
\(j\) stars by ones gives its member at offset \(-r+j\) from the middle.

The number of native radius-\(r\) chains is independent of the SCD and is

\[
 c_r=N_r-N_{r+1}.
\tag{1.2}
\]

Indeed the chains reaching rank \(m-r\) are precisely those of radius at
least \(r\), and there are \(N_r\) of them. Taking consecutive differences
proves (1.2). The exact formula is

\[
 \boxed{
 c_r=N_r\frac{2r+1}{m+r+1}.}
\tag{1.3}
\]

The retained owner mass is

\[
 \sum_{r\ge q_0}c_r=N_{q_0}.
\tag{1.4}
\]

Every retained canonical chain has its own middle member, so these
providers are owner-simple before any rotor edges are chosen.

## 2. The genuine physical suffix edge

Let \(S\) be a canonical BTK signature on the first \(2m-2\) coordinates,
of native radius \(r\ge H\). Put \(a_*=2m-1\), \(b_*=2m\). Then

\[
 C_*(S)=S**,
 \qquad
 C_{01}(S)=S01
\tag{2.1}
\]

are canonical chains of radii \(r+1\) and \(r\), respectively. The final
\(01\) is matched internally.

If the free positions of \(S\) are

\[
 u_1<\cdots<u_{2r},
\]

the radius-\(H\) clipping of \(S**\) has lower block containing
\(u_{r+1-H}\) and residual block containing \(b_*\). The full rotor with

\[
 x=u_{r+1-H},\qquad y=b_*
\tag{2.2}
\]

has successor exactly the clipping of \(S01\). Its singleton word changes
from the central window of

\[
 u_1,\ldots,u_{2r},a_*,b_*
\]

to

\[
 u_{r+1-H},u_{r+2-H},\ldots,u_{r+H},
\]

which is the clipped word of \(S01\). Thus

\[
 \boxed{S**\longrightarrow S01}
\tag{2.3}
\]

is a genuine radius-\(H\) rotor edge.

As \(S\) ranges over the BTK chains of \(B_{2m-2}\) of radius at least
\(H\), these edges are vertex-disjoint: sources end in \(**\), targets in
\(01\), and the prefix \(S\) is recovered from either endpoint. Their
number is

\[
 M_H=\binom{2m-2}{m-H-1}.
\tag{2.4}
\]

This proves the exact matching asserted in (0.4).

## 3. Why the (10) terminal shore is not canonical

### Lemma 3.1 (unique orientation of a BTK contraction)

Let two consecutive stars in (1.1) have intervening Dyck word \(D\). The
replacement

\[
 *D*\longmapsto0D1
\tag{3.1}
\]

is a valid canonical BTK signature of radius one less. The replacement

\[
 *D*\longmapsto1D0
\tag{3.2}
\]

is not a canonical BTK signature.

#### Proof

Around the two stars, the relevant fixed block after contraction is a
concatenation of an old Dyck block, the displayed new block, and another
old Dyck block. The word \(0D1\) is Dyck, so concatenation preserves the
Dyck property.

For \(1D0\), inspect the prefix ending at its first new symbol. The old
preceding Dyck word has returned to height zero, and the new \(1\) lowers
the height to \(-1\). Thus the fixed block is not Dyck. \(\square\)

### Corollary 3.2 (no canonical (S10) child)

For every complete canonical prefix signature \(S\), the word \(S10\) is
not a canonical BTK chain signature. In particular the explicit suffix
rotor cannot be doubled by adding a second canonical edge

\[
 S**\longrightarrow S10.
\]

Reversing the local order of the terminal coordinate pair makes \(10\)
look like \(01\), but that changes the BTK coordinate order and therefore
changes the SCD. It is a legitimate two-frame proposal, not a recursion
inside the fixed canonical BTK decomposition.

Even granting this second shore formally does not evade the radius cut
below: \(S**\to S10\) also replaces two free positions by fixed positions
and therefore decreases native radius by one. It can enlarge an
adjacent-layer matching, but it cannot carry two chains from the same
native-radius layer on one monotone path.

## 4. Granting every (01) contraction still leaves too many paths

Let \(\mathfrak C\) be the following generous directed graph on the
retained canonical signatures. Put an edge \(\Sigma\to\Sigma'\) for every
replacement of two consecutive stars by the valid block \(0D1\), whether
or not that particular replacement has been proved to lift to one full
radius-\(H\) rotor update.

Every edge of \(\mathfrak C\) lowers native radius by exactly one. Thus
every directed path in \(\mathfrak C\) contains at most one vertex of each
native radius.

### Theorem 4.1 (native-radius layer cut)

Every vertex-disjoint directed path cover of the retained signatures in
\(\mathfrak C\) has

\[
 \boxed{
 p\ge\max_{r\ge q_0}c_r.}
\tag{4.1}
\]

#### Proof

Fix a native radius \(r\). A strictly decreasing path contains at most one
radius-\(r\) signature. Since there are \(c_r\) such signatures, at least
\(c_r\) paths are required. Maximize over \(r\). \(\square\)

This theorem is proved in a supergraph of the physically certified
terminal-suffix rotor graph. It therefore obstructs every recursion using
only canonical \({**}\to01\) contractions, even if all its hoped-for local
rotor lifts are granted for free.

If reversed-frame signatures and formal \({**}\to10\) edges are adjoined,
but every selected edge still strictly decreases native radius, the same
proof remains valid: a path contains at most one of the original canonical
radius-\(r\) providers. Thus the second shore is useful only if its
stateful realization also creates horizontal or upward transitions.

The simple last-star-pair map is worse still: it is many-to-one. For
example,

\[
 **01\longmapsto0101,
 \qquad
 01**\longmapsto0101.
\tag{4.2}
\]

Its image consists of the signatures with nonempty final Dyck block, so a
matching restricted to that one functional map has at least the number of
BTK signatures in dimension \(2m-1\) as path starts. Allowing every
consecutive-star contraction removes this particular functional collision,
but cannot remove the layer cut (4.1).

## 5. The exact Gaussian layer maximum

Uniformly for \(r=x\sqrt m+O(1)\), with \(x\) in a fixed compact subset of
\((0,\infty)\),

\[
 \frac{N_r}{W}=e^{-x^2+o(1)}.
\tag{5.1}
\]

Combining this with (1.3) gives

\[
 \frac{c_r}{W}
 =\frac{2xe^{-x^2}+o(1)}{\sqrt m}.
\tag{5.2}
\]

The location of the maximum can also be checked without an asymptotic
tail argument. From (1.3),

\[
 \frac{c_{r+1}}{c_r}
 =\frac{(m-r)(2r+3)}{(m+r+2)(2r+1)}.
\tag{5.3}
\]

This ratio exceeds one exactly when

\[
 2r^2+4r+1<m.
\tag{5.4}
\]

Hence \((c_r)\) is unimodal, with its maximum at
\(r=\sqrt{m/2}+O(1)\).

The function \(2xe^{-x^2}\) increases through
\(x=1/\sqrt2\) and decreases afterwards. Since
\(H/\sqrt m=\sqrt{\log m}+o(1)\), the retained radius range reaches far
past its maximum. Consequently

\[
 \boxed{
 \max_{r\ge q_0}c_r
 =\left(\kappa(a)+o(1)\right)\frac W{\sqrt m},}
\tag{5.5}
\]

with \(\kappa(a)\) as in (0.7). This proves (0.6).

The two endpoint scales are smaller. At the tuned top,

\[
 \log\frac{N_H}{W}
 =-\frac{H^2}{m}+o(1)
 =-\log m+o(1),
\tag{5.6}
\]

so

\[
 N_H=(1+o(1))\frac Wm.
\tag{5.7}
\]

The exact ratio

\[
 \frac{M_H}{N_H}
 =\frac{(m-H)(m+H)}{2m(2m-1)}
 =\frac14+o(1)
\tag{5.8}
\]

then gives (0.4). At the bottom, the radius-zero Catalan count is

\[
 c_0=\frac{W}{m+1}.
\tag{5.9}
\]

These \(W/m\) endpoints do not bound the interior maximum (5.5).

## 6. Nonmonotone edges are quantitatively necessary

Let \(F\) be any directed path forest on the retained canonical chains.
Write \(p\) for its number of paths and \(b\) for the number of selected
edges \(C\to C'\) satisfying

\[
 \operatorname{rad}(C')\ge\operatorname{rad}(C).
\tag{6.1}
\]

### Theorem 6.1 (cross-grading burden)

One has

\[
 \boxed{
 p+b\ge\max_{r\ge q_0}c_r.}
\tag{6.2}
\]

#### Proof

Delete the \(b\) nondecreasing edges. Every deletion increases the number
of path components by one. All remaining paths strictly decrease native
radius and therefore contain at most one chain from any fixed radius layer.
Theorem 4.1 applied to the remaining forest gives (6.2). \(\square\)

If \(p=O(W/m)\), equations (5.5) and (6.2) yield (0.10). Thus a positive
open-path construction needs \(\Theta(W/\sqrt m)\) horizontal or upward
state-compatible edges. This burden is much larger than the certified
suffix matching (0.4).

## 7. Exact owner and literal-length accounting

The retained BTK chains have exactly \(N_{q_0}\) distinct middle owners.
At every controlled depth \(q\ge q_0\), their tag-at-least-\(q\)
subfamily contains every lower and upper target exactly once. Hence a
radius-\(H\) rotor path forest on these providers, with \(p\) paths, has
the following exact hard-start construction length:

\[
 \boxed{L_{\rm hard}=W+2Hp.}
\tag{7.1}
\]

The \(N_{q_0}\) path states are the paid provider occurrences; the other
\(W-N_{q_0}\) middle owners are appended as singletons. There is no owner
collision term.

For a terminal contraction which is a genuine rotor, the middle owners are
Johnson adjacent, so concatenating it consumes one new word letter and
does not duplicate an owner. The obstruction is entirely the number of
hard starts.

At the tuned \(H\), Theorem 4.1 gives the following lower bound on the
reset term in this stipulated hard-start architecture:

\[
 \frac{2Hp}{W}
 \ge\left(2\kappa(a)+o(1)\right)\sqrt{\log m}.
\tag{7.2}
\]

Thus the proposed canonical terminal recursion does not merely miss an
\(o(W)\) estimate; under the common radius-\(H\) hard-start compiler its
reset term is larger than \(W\) by a growing factor.

Even if each path were initialized only at a native Gaussian radius
\(r=\Theta(\sqrt m)\), the \(\Theta(W/\sqrt m)\) layer components would
pay \(\Theta(W)\) aggregate hard-start cost. Hence replacing the common
\(2H\) collar by native-radius resets would still not prove coefficient
one.

## 8. Exact scope

Proved here:

1. the explicit suffix-pair rotor matching and its tuned
   \(W/(4m)\) scale;
2. invalidity of the \(10\) terminal child in the canonical BTK signature
   language;
3. the native-radius cut even after granting every valid \(01\)
   contraction as a rotor edge;
4. the exact Gaussian constant \(\kappa(a)\);
5. the \(\Theta(W/\sqrt m)\) nonmonotone-edge burden for any
   \(O(W/m)\)-path construction; and
6. the exact owner and hard-start compiler ledger.

Not proved here:

1. an \(O(W/m)\)-path forest using nonmonotone collar transitions;
2. a two-frame recursion in which the \(10\) shore is legal and ownership
   remains one-copy;
3. a useful bridge compiler for the unavoidable cross-grading edges; or
4. coefficient one.

The corrected conclusion is therefore sharp. The tuned top leave and its
explicit suffix matching are both genuinely at the affordable \(W/m\)
scale. The recursive interior is not. Inside one canonical BTK SCD,
terminal-pair contractions are one-way and monotone, and the Gaussian
radius census forces \(\Theta(W/\sqrt m)\) open paths. The next positive
step must construct state-compatible nonmonotone transitions; another
iteration of \({**}\to01\) cannot do so.
