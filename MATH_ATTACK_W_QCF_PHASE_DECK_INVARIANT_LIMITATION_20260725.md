# QCF phase decks: exact endpoint/pin limitation after baseline recycling

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Exact outcome

Put

\[
 N=2m+1,
 \qquad M=N\ell,
\]

where \(\ell\) is the length of one long quotient block and all \(N\)
phase lifts are present.  The question is whether the endpoint, rank, or
compatible-pin constraints currently available can force additive
\(\Omega(N\ell)\) length after the \(N\ell\) baseline owner positions
are allowed to be recoded.

They cannot do so from their present hypotheses.

There are two exact statements.

1.  At signed depth \(q\), the complete internal-plus-two-collar window
    family has at most

    \[
       N(\ell+q)=M+Nq                                      \tag{0.1}
    \]

    occurrences.  Thus equal-rank endpoint injectivity can force at most
    \(Nq\) additive positions at that rank, and at all depths
    \(q\le H\) it has only the \(O(NH)\) scale.  The multirank mandatory
    span inequality of
    `MATH_ATTACK_AD16_PBBS_GLOBAL_CROSS_CUT_BASELINE_FUSION_20260725.md`
    is still smaller: even when every occurrence in (0.1) is a distinct
    lower target, its nonlinear span term has exact root

    \[
       {HM+NH(H+1)/2\over M+H}<2H.                         \tag{0.2}
    \]

    It does not add the \(N\) phase costs, because the same word positions
    may be endpoints at many ranks and in many phase-labelled target
    families.

2.  More decisively, there is an explicit rotational deck of \(N\)
    chronological Johnson paths with \(N\ell\) distinct middle owners,
    maximal distinct lower and upper target support through depth \(H\),
    and a direct nonzero literal word of exact length

    \[
       \boxed{N\ell+4NH}.                                  \tag{0.3}
    \]

    The word represents every union and every intersection of every
    consecutive owner interval in the full radius-\(H\) collar, not only
    the windows of depth at most \(H\).  Its lower flags contain explicit
    compatible-pin bundles of size exactly \(H\).

Consequently, when \(H/\ell\to0\), no theorem whose hypotheses use only
local Johnson chronology, all \(N\) rotational phase lifts, distinct
middle owners, distinct signed target sets, rank/endpoint antichains,
freely chosen literal witnesses, and compatible-pin necessity can force
additive \(\Omega(N\ell)\).  Such a theorem would be false on the deck
constructed below, whose excess is \(4NH=o(N\ell)\).

This is an exact limitation, not a proof of QCF for PBBS.  The constructed
deck is not proved to extend to one exact PBBS factor and is not proved to
obey the PBBS first-avoided/omitted-label recurrence.  Hence a genuine
PBBS-specific obstruction may still use exact-factor extendibility,
return dynamics, occurrence-labelled ownership, or a prescribed witness
chronology.  None of those extra inputs is supplied by the audited
endpoint or pin inequalities.

## 1. The exact collar occurrence ceiling

Fix one phase and a block of owner indices

\[
 0,1,\ldots,\ell-1,
 \qquad 1\le q\le H<\ell.
\]

A depth-\(q\) owner window has \(q+1\) consecutive owners.  There are
\(\ell-q\) windows contained in the block, \(q\) crossing the left
boundary, and \(q\) crossing the right boundary.  These families are
disjoint because \(q<\ell\).  Thus the exact occurrence count per phase is

\[
 (\ell-q)+q+q=\ell+q.                               \tag{1.1}
\]

Over all phases this proves (0.1).  Any selected support family is a
subfamily, so if \(D_q^-\) and \(D_q^+\) denote the numbers of distinct
lower and upper target values, respectively, then

\[
 D_q^\pm\le N(\ell+q)=M+Nq.                        \tag{1.2}
\]

### Lemma 1.1 (fixed-rank endpoint ceiling)

If a literal word of length \(M+e\) represents one of the target
families in (1.2), equal-rank endpoint injectivity can give no numerical
conclusion stronger than

\[
 e\ge D_q^\pm-M\le Nq.                             \tag{1.3}
\]

In particular its strongest possible scale over \(q\le H\) is \(NH\),
not \(N\ell\).

#### Proof

Choose one witnessing interval for every distinct target at the fixed
rank.  Two such intervals cannot contain one another: containment of
intervals gives containment of their unions, and two distinct sets of the
same cardinality are incomparable.  Hence their left endpoints are
distinct, so the word has at least \(D_q^\pm\) positions.  Therefore
\(M+e\ge D_q^\pm\).  Insert (1.2). \(\square\)

This is precisely where baseline recycling enters.  The \(M\) internal
targets at a new rank do not require another \(M\) positions.  They may
reuse the \(M\) positions already paid for at the middle rank.  Only the
\(Nq\) collar surplus remains visible to a one-rank count.

### Lemma 1.2 (the audited multirank span term stays order \(H\))

Assume the lower families attain the maximum in (1.2):

\[
 D_q^-=M+Nq\qquad(1\le q\le H).                   \tag{1.4}
\]

The lower-rank span inequality

\[
 \sum_{q=1}^H(D_q^--e)_+\le Me                    \tag{1.5}
\]

has smallest real feasible \(e\) from its span term equal to

\[
 e_{\rm span}
 ={\sum_{q=1}^H D_q^-\over M+H}
 ={HM+NH(H+1)/2\over M+H}<2H.                    \tag{1.6}
\]

Thus the complete presently audited endpoint/rank package has the
\(NH\) scale from Lemma 1.1; summing many depths in (1.5) does not amplify
it to \(N\ell\).

#### Proof

For \(e<\min_qD_q^-\), equation (1.5) is equivalent to

\[
 \sum_qD_q^-\le(M+H)e.
\]

The value in (1.6) is less than

\[
 H+{H(H+1)\over2\ell}<2H
\]

because \(M=N\ell\) and \(H<\ell\).  It is therefore far below
\(\min_qD_q^-\), so it is indeed the first root of the full positive-part
inequality.  Formula (1.4) gives the displayed numerator. \(\square\)

Lemma 1.2 concerns the lower-rank mandatory-span theorem exactly as
proved.  No unproved complement-to-OR duality is used for the upper
families.  The fixed-rank bound of Lemma 1.1 applies to either sign.

## 2. An exact rotational depth-\(H\) deck compiler

The next theorem makes the limitation structural rather than merely
numerical.

### Theorem 2.1 (rotational \(2H\)-window deck)

Let

\[
 N=2m+1,
 \qquad r\in\{m,m+1\},                            \tag{2.1}
\]

and let \(H,\ell\) be positive integers satisfying

\[
 H<\ell,
 \qquad r>5H,
 \qquad \ell+2H+1\le N-r.                        \tag{2.2}
\]

There exist rank-\(r\) owner sets

\[
 X_{u,i}
 \quad
 (u\in\mathbb Z_N,\ -H\le i\le\ell+H-1)          \tag{2.3}
\]

with the following properties.

1.  Rotational equivariance holds:

    \[
       X_{u,i}=\rho^uX_{0,i}.                     \tag{2.4}
    \]

2.  For each phase \(u\), the sequence in \(i\) is a chronological
    Johnson path.  Consecutive owners differ by deleting one coordinate
    and inserting one coordinate.  For \(r=m\) this path is the
    even-time projection of an integral odd-graph path; for \(r=m+1\)
    the same is true after taking complements.

3.  The \(N\ell\) assigned owners

    \[
       \{X_{u,i}:u\in\mathbb Z_N,\ 0\le i<\ell\}  \tag{2.5}
    \]

    are pairwise distinct.

4.  For every fixed sign, every \(1\le q\le H\), every phase \(u\), and
    every start

    \[
       -q\le i\le\ell-1,                          \tag{2.6}
    \]

    the signed targets

    \[
    \begin{aligned}
       L_{u,i,q}&=\bigcap_{h=0}^qX_{u,i+h},\\
       U_{u,i,q}&=\bigcup_{h=0}^qX_{u,i+h}
    \end{aligned}                                 \tag{2.7}
    \]

    are pairwise distinct as \((u,i)\) varies.  Their ranks are exactly

    \[
       |L_{u,i,q}|=r-q,
       \qquad |U_{u,i,q}|=r+q.                    \tag{2.8}
    \]

    Hence each signed depth has exactly the maximal support

    \[
       D_q^-=D_q^+=N(\ell+q).                     \tag{2.9}
    \]

5.  There is a direct nonzero literal word \(w\) of exact length

    \[
       |w|=N(\ell+4H)=N\ell+4NH                  \tag{2.10}
    \]

    representing every assigned owner and all the targets in (2.7).
    More strongly, for each phase it represents the union and the
    intersection of every consecutive nonempty owner interval contained
    in the full collar \([-H,\ell+H-1]\).

#### Construction and proof

Regard the ground set as the cycle \(\mathbb Z_N\), with one-step
rotation \(\rho\).  Choose a cyclic interval \(G\) of size

\[
 |G|=r-2H.                                        \tag{2.11}
\]

Its complement has size \(N-r+2H\).  Inside that complement choose, in
cyclic order, distinct consecutive coordinates

\[
 a_j,
 \qquad -H\le j\le\ell+3H-2,                    \tag{2.12}
\]

with at least one unused coordinate separating this active segment from
\(G\) at each end.  The active segment has \(\ell+4H-1\) coordinates.
It and the two separators fit exactly under

\[
 (\ell+4H-1)+2
 \le N-r+2H,
\]

which is the last condition in (2.2).

Put

\[
 G_u=\rho^uG,
 \qquad a_{u,j}=\rho^ua_j,                       \tag{2.13}
\]

and define

\[
 \boxed{
 X_{u,i}=G_u\cup
 \{a_{u,i},a_{u,i+1},\ldots,a_{u,i+2H-1}\}.}    \tag{2.14}
\]

Every owner has rank \((r-2H)+2H=r\), and

\[
 X_{u,i+1}
 =X_{u,i}-\{a_{u,i}\}+\{a_{u,i+2H}\}.           \tag{2.15}
\]

This proves (2.4) and Johnson chronology.

The asserted local odd-graph lift is also exact.  When \(r=m\), put

\[
 Y_{u,i}=\mathbb Z_N\setminus(X_{u,i}\cup X_{u,i+1}).       \tag{2.15a}
\]

The two consecutive owners have union size \(m+1\), so \(Y_{u,i}\) has
size \(m\) and is disjoint from both.  Thus
\(X_{u,i},Y_{u,i},X_{u,i+1}\) is a two-edge path in the odd graph
\(KG(2m+1,m)\).  When \(r=m+1\), apply the same construction to the
rank-\(m\) complements of the owners.  This proves only local integral
odd-graph legality, not the PBBS recurrence or completion to its canonical
factor.

Each owner in (2.14) has exactly two cyclic components: the core \(G_u\)
of size \(r-2H\), and an active interval of size \(2H\).  Since
\(r>5H\), the core has size greater than \(3H\), and in particular is the
unique largest component.  Equality

\[
 X_{u,i}=X_{v,j}
\]

therefore forces \(G_u=G_v\).  A proper cyclic interval has trivial
rotational stabilizer, so \(u=v\), after which equality of the active
intervals forces \(i=j\).  This proves (2.5).

Direct calculation gives, for \(0\le q\le H\),

\[
 \boxed{
 L_{u,i,q}
 =G_u\cup
 \{a_{u,i+q},\ldots,a_{u,i+2H-1}\},}             \tag{2.16}
\]

and

\[
 \boxed{
 U_{u,i,q}
 =G_u\cup
 \{a_{u,i},\ldots,a_{u,i+2H+q-1}\}.}            \tag{2.17}
\]

Their active components have sizes \(2H-q\) and \(2H+q\), respectively,
so (2.8) follows.  Through depth \(H\), every active component has size
at most \(3H\), strictly less than the core.  Equality of two targets of
one fixed sign and depth again identifies the unique large core, hence
the phase, and then identifies the active-interval start.  There are
\(\ell+q\) starts in (2.6), proving (2.9).

For the literal compiler, define nonzero set-letters

\[
 E_{u,j}=G_u\cup\{a_{u,j}\}                      \tag{2.18}
\]

and emit, for each phase \(u\),

\[
 w_u=
 (E_{u,-H},E_{u,-H+1},\ldots,
   E_{u,\ell+3H-2},G_u).                         \tag{2.19}
\]

There are \(\ell+4H-1\) letters of type \(E\) and one terminal core
letter, so

\[
 |w_u|=\ell+4H.                                  \tag{2.20}
\]

Let \(-H\le i\le j\le\ell+H-1\).  The union of the corresponding owner
interval is

\[
 \boxed{
 \bigcup_{h=i}^jX_{u,h}
 =\bigcup_{t=i}^{j+2H-1}E_{u,t}.}                \tag{2.21}
\]

If \(j-i<2H\), its intersection is

\[
 \boxed{
 \bigcap_{h=i}^jX_{u,h}
 =\bigcup_{t=j}^{i+2H-1}E_{u,t}.}                \tag{2.22}
\]

If \(j-i\ge2H\), the intersection is exactly the terminal letter
\(G_u\).  Every index in (2.21)--(2.22) lies between
\(-H\) and \(\ell+3H-2\), so each right side is a contiguous OR in
\(w_u\).  In particular (2.16)--(2.17) and every owner are represented.

Finally concatenate the \(N\) words \(w_u\).  This gives (2.10).
Additional ORs crossing the phase-word seams are harmless: literal
realizability requires the specified targets to occur and does not forbid
extra represented sets. \(\square\)

### Clause-4 accounting

The emitted helpers do not re-emit an owner position from a neighbouring
block.  Indeed,

\[
 |E_{u,j}|=r-2H+1<r,
 \qquad |G_u|=r-2H<r.                            \tag{2.23}
\]

Thus no emitted letter is one of the rank-\(r\) middle owners.  The word
may incidentally represent collar owners as ORs of helper letters, which
is allowed by literal-support QCF and costs no foreign owner position.
This verifies only that literal accounting interpretation.  It does not
embed the helper positions into an exact factor.

## 3. The compatible-pin condition is met at the required scale

The model does not evade the pin theorem by making its lower flags
degenerate.  It realizes the required order-\(H\) bundles explicitly.

For a baseline start \(i\), use the owner witness

\[
 X_{u,i}=\bigcup_{t=i}^{i+2H-1}E_{u,t}.           \tag{3.1}
\]

The \(H\) strict lower targets

\[
 L_{u,i,H}\subset L_{u,i,H-1}\subset\cdots
 \subset L_{u,i,1}\subset X_{u,i}                \tag{3.2}
\]

all use witnesses with the same right endpoint \(E_{u,i+2H-1}\).  Choose
the pins in increasing-target order to be

\[
 a_{u,i+H},a_{u,i+H-1},\ldots,a_{u,i+1}.          \tag{3.3}
\]

The first lies in \(L_{u,i,H}\); each subsequent pin lies in the newly
added difference, so these are valid pins.

Fix an active index \(j\) away from the baseline ends, for example
\(H\le j\le\ell\).  For

\[
 i=j-s,
 \qquad 1\le s\le H,                             \tag{3.4}
\]

take the request in (3.2) whose pin is \(a_{u,j}\).  These \(H\) requests
come from \(H\) distinct mandatory right endpoints.  Every corresponding
outer owner \(X_{u,i}\) contains \(a_{u,j}\), and the single word letter
\(E_{u,j}\) contains their common pin and lies in every corresponding
owner witness.  Hence they form a compatible-pin bundle of cardinality

\[
 \boxed{H}.                                       \tag{3.5}
\]

Thus the \(\Omega(H)\)-bundle necessity from the audited pin lemma is
attained in this baseline-relative model.  A negative PBBS theorem must
prove that the actual PBBS block has uniformly smaller capacity for every
admissible witness and pin selection, not merely that one canonical flag
choice has low capacity.

## 4. Exact implication boundary

Theorem 2.1 proves the following no-go statement.

### Corollary 4.1 (no abstract \(\Omega(N\ell)\) phase-deck invariant)

Let \(H=H(m)\), \(\ell=\ell(m)\) satisfy

\[
 H/\ell\to0,
 \qquad \ell+2H=o(m).                             \tag{4.1}
\]

For either middle rank \(r\in\{m,m+1\}\), all hypotheses (2.2) hold for
large \(m\).  There are then all-phase chronological decks satisfying
properties 1--4 of Theorem 2.1 and having literal excess

\[
 4NH=o(N\ell).                                    \tag{4.2}
\]

Therefore no valid lower bound derived solely from those properties can
force additive \(cN\ell\) for any fixed \(c>0\).

The corollary is deliberately not a PBBS counterexample.  The following
possible obstruction sources remain outside its hypotheses:

* completion of the displayed deck to one integral exact middle factor;
* the actual PBBS omitted-label and first-return recurrence;
* owner-labelled or occurrence-labelled preservation rather than target
  support preservation;
* a demand that prescribed old witness endpoints survive, rather than
  allowing an arbitrary new literal witness;
* a PBBS-specific theorem bounding compatible-pin capacity by \(o(H)\)
  uniformly over every possible witness system.

The already proved rigid Gaussian PBBS packet gives \(Nq\) distinct
phase-deck targets and an \(N(s-1)\) toll for the canonical verbatim-port
opening.  Those results are consistent with (0.3): both have the
\(O(NH)\) scale and neither is an additive lower bound against arbitrary
in-place recoding.  No genuine PBBS block with a forced
\(\Omega(N\ell)\) excess is obtained here.

## 5. Independent audit of the decisive construction

An independent proof audit checked the strengthened \(2H\)-window
version above.  The audited points were:

* the active-segment and two-separator capacity is exactly equivalent to
  \(\ell+2H+1\le N-r\);
* all indices in (2.21)--(2.22) lie in the emitted range;
* \(r>5H\) makes the core uniquely larger than every signed active
  component through depth \(H\), which is the needed phase-distinctness
  argument;
* the size-\(H\) pin bundle is diagonal across \(H\) distinct owner
  endpoints, not the nested flag at one endpoint;
* the conclusion is a limitation on free literal recoding, not an
  exact-factor or genuine-PBBS realization theorem.

No unproved lemma is used inside Theorem 2.1.  The sole open step relevant
to QCF is whether actual PBBS long blocks admit such a compiler, or instead
carry an additional PBBS-specific invariant absent from this model.
