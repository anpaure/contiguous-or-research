# Screened unsaturated hinges: common upper signatures, exact residence collars, and the freshness obstruction

**Date:** 2026-08-02  
**Lane:** A, integral coloured rotors  
**Status:** exact local theorem.  It completes the residence/upper interface
of the unsaturated one-copy hinge at the **menu projection**, and gives a
sharp local obstruction to promoting the original repeated-filler word to a
one-copy owner path.  It does not prove the global predecessor matching,
Hoffman cuts, source/common-cap compatibility, or a connected Euler carrier.

## 0. Setup

Fix

\[
 \varnothing\ne S_1\subsetneq\cdots\subsetneq S_\ell\subsetneq T,
 \qquad |T|=r\ge3,\qquad 1\le\ell\le d.                 \tag{0.1}
\]

Put \(S_0=\varnothing\), \(D_q=S_q-S_{q-1}\),
\(U=T-S_\ell\), and \(p=d-\ell\).  Choose \(y\in S_1\).  The
unsaturated hinge of
`MATH_THEOREM_A_UNSATURATED_ONECOPY_HINGE_AND_PROTECTED_COMPLETION_GATE_20260802.md`
has letters

\[
 \begin{aligned}
 B_0(A)&=U\cup A, && A\subseteq S_1-\{y\},\\
 B_t&=\{x\}, &&1\le t\le p,\\
 B_{d-q+1}&=D_q, &&1\le q\le\ell .
 \end{aligned}                                          \tag{0.2}
\]

When \(p=0\), the filler line is absent.  The choice of \(x\), when
present, is as in the cited theorem: \(x\ne y\) and
\(S_\ell\cup\{x\}\ne T\).

For a source word \(L=(L_j)\), write

\[
                         \Omega_j(L)=\bigcup_{t=j}^{j+d}L_t              \tag{0.3}
\]

for its length-\((d+1)\) owner window.  Upper targets are interval unions
of consecutive \(\Omega_j\)'s.

## 1. The exact screen criterion

Let

\[
                         D=S_1-\{y\}.                                  \tag{1.1}
\]

Consider a family of source words which differ only at position zero,
where \(L_0=B_0(A)=U\cup A\), \(A\subseteq D\).  For every
\(-d\le j\le0\), put

\[
       Q_j=\bigcup_{\substack{j\le t\le j+d\\t\ne0}}L_t .             \tag{1.2}
\]

### Lemma 1.1 (necessary and sufficient owner-screen test)

The owner \(\Omega_j(L)\) is independent of \(A\subseteq D\) if and only if

\[
                              D\subseteq Q_j.                            \tag{1.3}
\]

Consequently the complete owner chronology is independent of \(A\) if and
only if (1.3) holds for every window containing position zero.

#### Proof

The choices \(A=\varnothing\) and \(A=D\) give owner unions
\(Q_j\cup U\) and \(Q_j\cup U\cup D\).  Since \(D\cap U=\varnothing\),
these are equal exactly when \(D\subseteq Q_j\).  All other choices lie
between these two.  Windows avoiding position zero are already fixed.
\(\square\)

Thus failure of menu-level upper transparency has the exact finite
certificate

\[
       (a,j),\qquad a\in D-Q_j,\quad -d\le j\le0.                       \tag{1.4}
\]

There are at most \(d|D|\) nontrivial certificates, because the window
starting at zero already contains \(B_d=S_1\supseteq D\).

## 2. One literal screen closes every upper-width row

Choose a new coordinate \(z\notin T\) and prepend the fixed screen letter

\[
                         G=(S_1-\{y\})\cup\{z\}.                        \tag{2.1}
\]

Place \(G\) at source position \(-1\), followed by
\(B_0(A),B_1,\ldots,B_d\) at positions \(0,1,\ldots,d\).

### Theorem 2.1 (screened common predecessor and full upper signature)

For every \(A\subseteq S_1-\{y\}\):

1. the two displayed consecutive owners are

   \[
   \Omega_{-1}=(T-\{y\})\cup\{z\}=:P,
   \qquad \Omega_0=T;                                  \tag{2.2}
   \]

2. \(P,T\) are a Johnson edge, with fixed lower and upper colours

   \[
                  P\cap T=T-\{y\},\qquad P\cup T=T\cup\{z\};          \tag{2.3}
   \]

3. in every fixed exterior source context, **every** owner
   \(\Omega_j\) is independent of \(A\); hence every lower intersection and
   every arbitrary-width interval union of owners is independent of \(A\);
4. the alternatives therefore have one common predecessor owner, one
   common q1 seam, and one common complete owner-level residence/upper
   boundary signature.

#### Proof

The union of \(B_0,\ldots,B_{d-1}\) is
\((T-S_1)\cup A\cup\{x\}\) when \(p>0\), and
\((T-S_1)\cup A\) when \(p=0\).  In either case adjoining \(G\), the
layers \(D_\ell,\ldots,D_2\), and the allowed filler gives precisely
\((T-\{y\})\cup\{z\}\).  The second equality in (2.2) is the complete-union
identity of the unsaturated hinge.  This proves (2.2)--(2.3).

Only \(B_0(A)\) varies.  Every length-\((d+1)\) window containing position
zero either starts at zero, in which case its union is \(T\), or starts
before zero and therefore contains the screen \(G\supseteq D\).  Lemma 1.1
then makes every owner window independent of \(A\).  Intersections and
interval unions are functions of this fixed owner chronology.  \(\square\)

This is stronger than compressed prefix/suffix deck inclusion: the complete
owner word, and hence every owner-derived deck, is literally the same for
all menu choices.  It is only a **menu-comparison** statement.  It does not
say that this owner word contains every required upper target, nor that it
preserves the upper deck of a different antecedent word.

## 3. Exact residence collar at the screened seam

The transition \(P\to T\) in (2.2) inserts \(y\) and deletes \(z\).  The
screen occurrence of \(z\) at position \(-1\) makes \(z\) present in the
\(d+1\) owners \(\Omega_{-d-1},\ldots,\Omega_{-1}\).  The occurrence of
\(y\) in \(B_d=S_1\) makes \(y\) present in
\(\Omega_0,\ldots,\Omega_d\).

### Lemma 3.1 (two exact absence collars)

At the seam \(P\to T\), signed residence at least \(d+1\) for the two
changing coordinates is certified by exactly the two local conditions

\[
 \boxed{
 y\notin\bigcup_{t=-d-1}^{-2}L_t,
 \qquad
 z\notin\bigcup_{t=d+1}^{2d}L_t .}                                  \tag{3.1}
\]

Under (3.1), the \(y\)-zero run immediately before the seam, the
\(y\)-positive run immediately after it, the \(z\)-positive run immediately
before it, and the \(z\)-zero run immediately after it all have length at
least \(d+1\).  Conversely, because the displayed local letters already
omit \(y\) before \(B_d\) and omit \(z\) after \(G\), a violation of either
condition in (3.1) makes the corresponding length-\((d+1)\) collar test
fail.

#### Proof

The union of the owner windows
\(\Omega_{-d-1},\ldots,\Omega_{-1}\) inspects source positions
\(-d-1,\ldots,d-1\).  All fixed local positions \(-1,\ldots,d-1\) omit
\(y\), so these \(d+1\) owners all omit \(y\) exactly when the left collar
in (3.1) does.  The occurrence at position \(d\) then supplies \(y\) to
\(\Omega_0,\ldots,\Omega_d\).

Dually, the screen occurrence supplies \(z\) to
\(\Omega_{-d-1},\ldots,\Omega_{-1}\), while the right collar is exactly
what makes \(\Omega_0,\ldots,\Omega_d\) omit \(z\).  \(\square\)

No menu choice appears in (3.1).  Hence, once the two collars are fixed,
residence filtering does not shrink the \(A\)-menu.  Other coordinate runs
created elsewhere in a longer predecessor macro still require their usual
finite-state audit.

### Corollary 3.2 (exact Cartesian screen expansion)

Let the ambient ground set be \([k]\), and fix only the two exterior collar
unions

\[
 L^-=\bigcup_{t=-d-1}^{-2}L_t,\qquad
 R^+=\bigcup_{t=d+1}^{2d}L_t.                         \tag{3.2}
\]

At the owner/history/q1 projection, the complete set of screened choices
passing Lemma 3.1 is the Cartesian product

\[
 \boxed{
 \mathcal Y\times\mathcal Z,\qquad
 \mathcal Y=S_1-L^-,
 \quad
 \mathcal Z=([k]-T)-R^+.}                             \tag{3.3}
\]

For fixed \(T\), the map

\[
 (y,z)\longmapsto
 \bigl(T-\{y\},\,T\cup\{z\}\bigr)                     \tag{3.4}
\]

from this product to its lower/upper q1 colour pair is injective.  Hence a
role has exactly

\[
 (|S_1|-|S_1\cap L^-|)
 \bigl((k-r)-|([k]-T)\cap R^+|\bigr)                  \tag{3.5}
\]

residence-safe screen pairs before global palette collisions are imposed.
In particular, bounded collar damage gives a literal product expansion,
not merely separate nonempty projections.

#### Proof

Lemma 3.1 excludes precisely the guards \(y\in L^-\) and outside
coordinates \(z\in R^+\), independently.  This proves (3.3)--(3.5).
For fixed \(T\), the lower colour determines \(y\), and the upper colour
determines \(z\), proving injectivity.  \(\square\)

The qualifier “for fixed \(T\)” is essential.  Different owner roles can
still collide on a lower or upper colour, and the opposite orientation of
one Johnson edge exchanges the two endpoint owners.  Those are global
matching rows, not consequences of the local product (3.3).

### Corollary 3.3 (no rotating casualties inside one screened subcube)

Fix one accepted pair \((y,z)\in\mathcal Y\times\mathcal Z\) and one
allowed filler choice.  In the literal completed-state table, the protected
residence/upper filter either rejects the entire role or retains all

\[
                              2^{|S_1|-1}                              \tag{3.6}
\]

tails indexed by \(A\subseteq S_1-\{y\}\).  On acceptance they form a
cylinder over one identical owner/history/upper state; there is no
target-by-target rotation inside the \(A\)-subcube.

#### Proof

Theorem 2.1 makes the complete owner chronology independent of \(A\), and
Lemma 3.1 makes its acceptance predicate independent of \(A\).  Literal
tails remain distinct because \(B_0=U\cup A\) is injective in \(A\).
\(\square\)

This cylinder is not a Cartesian predecessor relation in the literal
de Bruijn states: the distinct tails still have to be supplied by distinct
compatible predecessor occurrences.  Corollary 3.3 only proves that
residence and upper guards do not further thin that matching menu.

## 4. The sharp local one-copy obstruction

The preceding positive statements live at the owner/history/upper
projection.  They do not make the distinct literal de Bruijn tails equal.
There is also a direct obstruction to flushing the original source word as
a one-copy owner path.

### Lemma 4.1 (fresh-incoming necessity)

Let \(L\) be any source word whose consecutive length-\((d+1)\) unions
\(\Omega_{t-1},\Omega_t\) both have rank \(r\).  If

\[
                              L_{t+d}\subseteq\Omega_{t-1},             \tag{4.1}
\]

then \(\Omega_t=\Omega_{t-1}\).

Equivalently, every transition in a one-copy rank-\(r\) owner path must have
an incoming source cell containing at least one coordinate absent from the
previous owner.

#### Proof

The new window is obtained from the old one by deleting its first source
cell and adjoining \(L_{t+d}\).  Under (4.1) this can only decrease its
union.  Equal rank forces equality.  \(\square\)

For the screened local word put

\[
 N_t=B_t-\left(G\cup B_0\cup\cdots\cup B_{t-1}\right),
 \qquad 1\le t\le d.                                    \tag{4.2}
\]

Every displayed previous local letter belongs to the preceding owner
window.  Therefore

\[
                             N_t=\varnothing                             \tag{4.3}
\]

is a solver-free certificate that a rank-(r) realization repeats an
owner at that step, independently of the exterior.

### Corollary 4.2 (the repeated-filler hinge is not a flush macro)

If \(p=d-\ell\ge2\), then \(B_1=B_2=\{x\}\), so \(N_2=\varnothing\).
Thus the original unsaturated hinge cannot be promoted, letter for letter,
to a one-copy rank-\(r\) owner path through all of its source positions.

If \(p=1\), it already fails at the filler step whenever
\(x\in G\cup B_0\).  If the filler is fresh, the next layer step fails
whenever \(D_\ell\subseteq G\cup B_0\cup\{x\}\); in the disjoint-layer
case this includes the sharp singleton collision \(D_\ell=\{x\}\).

When \(p=0\), all layer differences are disjoint and the final layer
\(D_1=S_1\) contains the unscreened coordinate \(y\), so this particular
freshness obstruction is absent.  That is not a sufficiency theorem: rank,
deletion chronology, predecessor matching, and connectivity remain.

### Theorem 4.3 (exact aperture for removing all local freshness failures)

Allow the \(p=d-\ell\) filler cells in (0.2) to be replaced by arbitrary
nonempty cells \(F_1,\ldots,F_p\subseteq T-\{y\}\), while keeping the
chain layers and the screen \(G\).  Suppose every filler transition and
every later chain-layer transition is to avoid the zero-novelty certificate
(4.3).  Then necessarily

\[
 \boxed{
 p\le \sum_{q=2}^{\ell}(|D_q|-1)
   =|S_\ell|-|S_1|-(\ell-1).}                         \tag{4.4}
\]

Conversely, if (4.4) holds, there is a singleton-filler choice for which
every local novelty set is nonempty.  Namely reserve one coordinate
\(b_q\in D_q\) for every \(2\le q\le\ell\), choose distinct

\[
 x_1,\ldots,x_p\in
 (S_\ell-S_1)-\{b_2,\ldots,b_\ell\},                  \tag{4.5}
\]

and put \(F_t=\{x_t\}\).  The resulting hinge retains the exact suffix
chain, unsaturated tail and head, screened predecessor (2.2), common upper
signature, and residence collar (3.1).

Thus (4.4) is an exact necessary-and-sufficient aperture for eliminating
the **local zero-novelty obstruction** within this generalized singleton
filler class.  It is not sufficient for a rank-\(r\) sliding-window path:
one must still schedule exactly one expiration against every fresh arrival.

#### Proof

A fresh coordinate at a filler step cannot lie in

\[
 (G\cup B_0)\cap T=(S_1-\{y\})\cup U,
\]

and it cannot equal an earlier filler's fresh coordinate.  Since \(y\) is
forbidden, the \(p\) filler steps therefore require \(p\) distinct
coordinates from \(S_\ell-S_1\).  When the later cell \(D_q\) arrives, it
must still contain a coordinate not used in any filler; otherwise its local
novelty set is empty.  Hence at least one coordinate of each disjoint
\(D_q\), \(2\le q\le\ell\), is unavailable to the filler pivots.  This
gives (4.4).

For the converse, (4.4) makes (4.5) possible.  Each \(x_t\) is new at its
filler position.  The reserved \(b_q\) is new when \(D_q\) arrives, and
\(y\) is new when \(D_1\) arrives.  The filler union is contained in
\(S_\ell-S_1\), so it changes neither the hinge's head union \(S_\ell\)
nor the omission of \(y\) from its tail.  The proofs of Theorems 2.1 and
3.1 are otherwise unchanged.  \(\square\)

## 5. Exact consequence for protected completion

The screened hinge separates the live gate into two parts.

* **Residence and upper rows:** one outside coordinate \(z\), the screen
  (2.1), and the two absence collars (3.1) make the whole \(A\)-menu carry
  one identical owner chronology, every owner-derived upper deck, and the
  same accepting seam history.
* **Literal one-copy row:** the tails
  \((B_0(A),\ldots,B_{d-1})\) remain distinct.  They still require an exact
  occurrence-labelled predecessor matching.  Moreover (4.3) must be
  excluded at every source step of any proposed multi-edge completion.

Thus residence and arbitrary-width upper transparency add only the finite
screen failures (1.4) and the two collar failures (3.1) **after a literal
screen occurrence has been supplied**.  They do **not** by themselves create
a new exponential family of Hoffman cuts.  The supply qualification is
load-bearing: predecessor Hall matches the tail tuple
`(B_0,...,B_(d-1))` to an earlier head, but the required screen is the
earlier packet's discarded first source letter.  That letter generally
depends on the earlier packet's chosen tail and is not determined by its
head.  Encoding it in the interface therefore creates a two-step
occurrence constraint and may destroy the fixed-head reduction.  A global
use of this theorem must plant the screen as a protected macro/owner or solve
the resulting correlated larger-state problem.  Its predecessor owner and
the lower/upper q1 pair `(T-{y},T union {z})` must be charged, with exact
cross-role capacity; injectivity in Corollary 3.2 holds only for fixed `T`.

Conditional on that literal occurrence binding, the smallest genuine new
local obstruction is the zero-novelty certificate (4.3); its complete local
filler aperture is (4.4).  Any positive all-depth construction must use that
fresh-coordinate schedule, use a larger correlated macro, or keep the hinge
as one transition and obtain both its literal incoming tail and its screen
from the global occurrence model.

No claim is made here about global screen-occurrence binding, source
maximality/common-Q, protected compiler addresses, existence of the global
predecessor matching, or a connected Euler skeleton.

## 6. Audit

Run

```bash
python3 scratch/audit_a_unsaturated_hinge_screened_signature_20260802.py
```

The audit exhausts all strict chains on fixed owners of ranks three through
six at depths up to four, all allowed menu choices \(A\), and all admissible
fillers \(x\).  It checks (2.2)--(2.3), full owner-window invariance under
the screen, the two signed collar traces, every zero-novelty certificate
used in Corollary 4.2, the Cartesian q1 expansion (3.3), and the constructive
direction of the aperture formula (4.4).
