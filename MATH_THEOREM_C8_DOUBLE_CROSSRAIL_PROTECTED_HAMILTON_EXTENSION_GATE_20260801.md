# The double-crossrail bridge has an exact protected Hamilton-extension gate

Date: 2026-08-01  
Lane: double-crossrail global owner embedding  
Status: exact occurrence ledger, exact contracted extension criterion,
protected rooted-tail Hall extension, and one literal resident source
continuation.  Simultaneous other-head/graphic extension and the final port
Hamilton path remain open.

## 0. Outcome

Work in the odd middle-level host between ranks `m-1` and `m` of
`[2m-1]`.  Put

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname {Cat}_m.
\]

The thirteen-component double-crossrail forest has

\[
 p=2d+15
\]

projected Johnson transitions.  After a compatible alternating incidence
colouring, its protected short shore `P1` is a matching of size `p`, and its
rooted links form thirteen vertex-disjoint directed paths.

Its upper-occurrence multiset is

\[
 M_+^d,\quad M_-^{d+1},\quad R_1,\ldots,R_{14},       \tag{0.1}
\]

where the sixteen displayed values are distinct.  Consequently

\[
 r_{\rm up}(P_1)=16,
 \qquad |P_1|-r_{\rm up}(P_1)=2d-1.                  \tag{0.2}
\]

This has an exact interpretation.  Choose one protected occurrence of each
of the sixteen values for the upper-representative forest.  The other
`2d-1` protected occurrences are forced connector edges.  They reduce the
remaining Catalan connector count from `C-1` to

\[
                         C-2d.                         \tag{0.3}
\]

Thus `C>=2d` is a necessary condition for an occurrence-preserving
upper-exact Hamilton extension.  In the OR-word regime it is harmless
asymptotically, but it is a real exact rank condition.

There is also a strategic simplification.  Protecting only the actual
double-crossrail bridge gives

\[
 p_{\rm br}=2d+3,\qquad r_{\rm up}(P_{1,\rm br})=4,
 \qquad p_{\rm br}-4=2d-1.                            \tag{0.4}
\]

So the twelve isolated upper-support edges do not reduce connector debt at
all.  If the global certificate is upper exact, their twelve upper values
are supplied somewhere automatically.  For support preservation, forcing
their literal occurrences only adds twelve tail/head/graphic contractions
and twelve unresolved clipped-residence interfaces.  The proof-efficient
global target is therefore the one bridge component plus global upper
exactness, not the full thirteen-component occurrence bank.

## 1. Correlated predecessor root shore

Let `P` be the incidence lift of the thirteen-component owner forest.  Every
Johnson transition contributes two incidence edges, so

\[
                         |E(P)|=2p=4d+30.               \tag{1.1}
\]

It is a disjoint union of alternating incidence paths and has maximum
degree two.  Orient every owner path.  At a transition

\[
                         V_i-L_i-V_{i+1},
\]

put the predecessor incidence `L_iV_i` in `P0` and the successor incidence
`L_iV_(i+1)` in `P1`.  Since all protected owners and lower colours are
distinct, `P0` is a matching of size `p`.

Every matching of size at most `m-1` in the middle-level incidence graph
extends to a perfect matching: after deleting its `t` endpoints on both
shores, the sharp middle-shadow surplus is at least `t`, so Hall survives.
Consequently, if

\[
                         p=2d+15\le m-1,               \tag{1.2}
\]

there is a perfect matching `M0` containing this prescribed predecessor
shore.  We then have

\[
                         P=P_0\mathbin{\dot\cup}P_1,
 \qquad P_0\subseteq M_0.                              \tag{1.3}
\]

Both classes contain one incidence from every projected Johnson
transition, so each has size `p`.  The value

\[
 \operatorname {up}_{M_0}(LV)=M_0(L)\cup V             \tag{1.4}
\]

is the corresponding projected adjacent-owner union, independently of the
chosen alternating phase.

Inside one protected path, the chosen phase gives `M0(L_i)=V_i`, and hence

\[
 \lambda_{M_0}(L_iV_{i+1})=L_i\longrightarrow L_{i+1}. \tag{1.5}
\]

The last protected owner is matched by `M0` to a lower vertex outside the
protected lower bank.  Perfect-matching injectivity makes those external
roots distinct between components.  Hence `lambda(P1)` is a forest of
thirteen vertex-disjoint directed paths.  Reversing a component phase only
reverses its path.

This prospective predecessor choice is stronger than taking an arbitrary
two-factor and colouring it afterward: it fixes the bridge direction and
avoids the generic fixed-`M0` protected-ticket obstruction.  It still
supplies no upper or residence conclusion outside `P`.  For the bridge-only
and right-continued one-component variants the corresponding exact phase
conditions are respectively

\[
                         2d+3\le m-1,
 \qquad                  3d+3\le m-1.                 \tag{1.6}
\]

## 2. Exact repeated-occurrence extension theorem

Fix a compatible `M0` and its protected shore `P1`.  Let

\[
 \mathsf M_L,\quad\mathsf M_O,\quad\mathsf M_G,
 \quad\mathsf M_U                                    \tag{2.1}
\]

be respectively the lower-tail partition matroid, owner-head partition
matroid, rooted-link graphic matroid, and upper-colour partition matroid on
incidences outside `M0`.

Choose a set `A0 subset P1` containing exactly one occurrence of every
upper value in (0.1), and put

\[
 |A_0|=16,\qquad A_1=P_1-A_0,qquad |A_1|=2d-1.       \tag{2.2}
\]

The upper matroid may contract `A0`, but it may not contract all of `P1`,
because `A1` repeats two upper values.  The other three matroids can and
must contract all of `P1`.

### Theorem 2.1 (protected repeated-upper Hamilton criterion)

There is an upper-exact spanning alternating Hamilton path containing every
incidence of `P` if and only if, for some allowed componentwise phase and
some representative choice `A0`, the following two objects exist.

1. A set `X`, disjoint from `P1`, of size `U-16`, common independent in

   \[
   \boxed{
   \mathsf M_L/P_1,\quad
   \mathsf M_O/P_1,\quad
   \mathsf M_G/P_1,\quad
   \mathsf M_U/A_0.}                                  \tag{2.3}
   \]

2. A directed Hamilton path of length `C-2d` in the physical free-port
   digraph of

   \[
                         F=P_1\cup X,                  \tag{2.4}
   \]

   after its `C-2d+1` rooted-link components are contracted.

#### Proof

Suppose first that `X` exists.  Put

\[
                         Q_0=A_0\cup X.                \tag{2.5}
\]

The upper contraction in (2.3) makes `up` injective on `Q0`; since
`|Q0|=U`, it is a bijection onto all upper colours.  The other three
contractions say exactly that

\[
                         F=Q_0\cup A_1=P_1\cup X       \tag{2.6}
\]

is a matching and its rooted links form a forest.  Its edge count is

\[
 |F|=U+(2d-1)=W-(C-2d+1),                             \tag{2.7}
\]

so it has exactly `C-2d+1` components.  A directed free-port Hamilton path
on those components uses `C-2d` additional incidences and produces one
spanning rooted-link path.  The resulting short shore has

\[
 U+(2d-1)+(C-2d)=U+C-1=W-1                           \tag{2.8}
\]

edges, contains all of `P1`, and is upper surjective.  Together with `M0`
it is the required alternating Hamilton path.

Conversely, let `Q` be such a protected Hamilton short shore.  Select one
edge of `Q` for every upper colour, choosing one protected occurrence for
each of the sixteen protected values.  Call the resulting upper-exact
forest `Q0`, and put `A0=P1 cap Q0`, `A1=P1-A0`, and
`X=Q0-A0`.  Since `Q` is a rooted-link path, `P1 union X` is matching and
graphic-independent, proving (2.3).  Contracting its components in the
remaining edges of `Q` gives the directed free-port Hamilton path in item 2.
The counts force its length to be `C-2d`.  \(\square\)

### Exact obstruction

If `C<2d`, then (2.7) asks a forest on `W` vertices to have more than
`W-1` edges.  Hence no upper-exact Hamilton path can retain every protected
occurrence of this forest.  No scalar or Hall repair can bypass this rank
obstruction.

For the asymptotic OR depth, `C` is exponentially larger than `d`, so this
is not expected to obstruct the intended application.  The substantive
open row is existence in all four contractions (2.3), followed by the
physical port path.

The same inequality is the complete raw rank ledger.  After contracting
`P1`, the tail and head partitions have at most `W-p` free slots, so beyond
the requested `U-16` elements they have scalar surplus

\[
             (W-p)-(U-16)=C-2d+1.                     \tag{2.9}
\]

The unrestricted graphic contraction has rank at most `W-1-p`, leaving

\[
             (W-1-p)-(U-16)=C-2d.                     \tag{2.10}
\]

The upper contraction has exactly the requested rank `U-16`.  Hence
`C>=2d` clears every individual cardinality/rank ceiling.  It does not imply
a common independent set: structural zeros can lower the rank on a common
restriction, and four separately extendible matroids need not extend
simultaneously.

## 3. Rooted-tail Hall survives all repeated protected occurrences

Although (2.3) remains a four-resource correlation, its upper/tail
projection is unconditional.

For `e=LV in P1`, write

\[
                         T(e)=M_0(L).                   \tag{3.1}
\]

The `p` rooted tails `T(e)` are distinct.  For `e in A0`, the protected pair

\[
              (\operatorname {up}(e),T(e))             \tag{3.2}
\]

has its tail contained in its upper colour.

### Theorem 3.1 (protected-and-forbidden rooted-tail extension)

Let `P1` be any protected matching of size `p<=m`, and let `A0 subset P1`
have distinct upper colours.  There is an injection

\[
 \psi:{[2m-1]\choose m+1}\longrightarrow
             {[2m-1]\choose m},\qquad \psi(R)\subset R,             \tag{3.3}
\]

which retains every pair (3.2) and satisfies

\[
 \psi(R)\notin T(P_1-A_0)qquad
       (R\notin\operatorname {up}(A_0)).                \tag{3.4}
\]

Equivalently, the upper-colour and rooted-tail partition rows of (2.3)
always have a common completion.

#### Proof

Delete the protected upper colours `up(A0)` and delete all `p` rooted tails
`T(P1)` from the central containment graph.  For any nonempty family
`mathcal X` of remaining upper colours, the central Kruskal--Katona surplus
gives

\[
 |N(\mathcal X)\setminus T(P_1)|
 \ge |N(\mathcal X)|-p
 \ge |\mathcal X|+m-p
 \ge |\mathcal X|.                                    \tag{3.5}
\]

Hall matches all remaining upper colours.  Adjoin the protected pairs in
`A0`.  This proves (3.3)--(3.4). \(\square\)

For the full double-crossrail forest, `p=2d+15`; hypothesis (1.2) is stronger
than `p<=m`.  Therefore no ordinary upper/tail Hall obstruction survives in
the asymptotic planting range, even though `2d-1` protected occurrences
repeat upper colours.

The theorem deliberately does not prove that the forced other owner heads
are distinct or that the rooted links remain acyclic after the completion.
Those are precisely the `M_O/P1` and `M_G/P1` rows in (2.3).

## 4. Why the twelve isolated occurrences should not be forced

Let `P_br` be only the incidence lift of the `2d+4`-owner double-crossrail
bridge.  Then

\[
 |P_{1,\rm br}|=2d+3,qquad
 |\operatorname {up}(P_{1,\rm br})|=4,qquad
 |P_{1,\rm br}|-4=2d-1.                               \tag{4.1}
\]

Thus deleting the twelve isolated protected transitions decreases both
`p` and its upper rank by twelve and leaves the exact connector debt
unchanged.  If the final short shore is upper exact, all twelve omitted
canonical values occur elsewhere automatically.

At occurrence level the two problems are different:

* retaining the full forest forces the twelve named physical incidences;
* retaining only the bridge preserves its four repeated-occurrence classes
  and asks only that the other twelve set values occur somewhere.

The second is sufficient for upper **support** and is strictly weaker in
the three contracted resource systems.  It also avoids the following
residence problem.  Each isolated two-owner edge is resident only because
both of its ends are component boundaries.  After placing it internally in
one Hamilton path, its common coordinates may form an internal run of
length two.  No owner-layer extension theorem repairs that automatically.

Therefore the exact 13-component theorem is useful as a local support
census, but the global proof should protect only the bridge occurrence bank
unless some downstream argument genuinely needs those twelve exact
occurrences.

## 5. A literal right continuation of the bridge source

There is one further local improvement which makes the bridge's source
interface explicit beyond its right endpoint.

Let `E` be the last bridge owner,

\[
                  E=K\cup\{z,a_3\}\cup F^\circ
                       \cup\{f_{d+1}\}.                \tag{5.1}
\]

Assume that at least `d` coordinates remain outside the bridge support
(in the odd middle-layer application it is enough that `d<=m-3`).  Choose
fresh coordinates `x_1,...,x_d` and append the owners

\[
 C_0=E,qquad
 C_t=E-\{f_1,\ldots,f_t\}+\{x_1,\ldots,x_t\}
              \quad(1\le t\le d).                     \tag{5.2}

This is a simple Johnson continuation.  Every new upper colour contains its
new label `x_t` and is therefore distinct from the bridge palette and from
the other new upper colours.  For `t>=2`, the new lower colour contains the
fresh prefix `x_1,...,x_(t-1)`, so these lower colours are mutually distinct.
The first lower colour is

\[
              E-\{f_1\}=K\cup\{z,a_3,f_{d+1}\}
                         \cup F[2,d],                  \tag{5.3a}
\]

which is separated from the bridge lower palette by its active/boundary
signature.  Thus all continuation lower colours are also new and distinct.

Take the maximal depth-`d` envelope of the extended owner path.  Make the
same two rail replacements as in the double-crossrail theorem, and replace
the old terminal maximal source letter at position `3d+3` by the singleton
letter

\[
                            \{f_{d+1}\}.                \tag{5.3}

### Theorem 5.1 (cap-compatible resident continuation)

The resulting nonempty source word dilates exactly to

\[
 G_1,\ldots,G_d,B,A,H_1,\ldots,H_d,D,E,C_1,\ldots,C_d. \tag{5.4}

Both cross banks remain unchanged.  Every internal positive run in (5.4)
has length at least `d+1`.

#### Proof

The left rail is unaffected.  A right-rail letter at position
`2d+2+s` is seen by the future owners `C_1,...,C_(s-1)`.  Each of those
owners contains its filler `f_s`; for the endpoint letter `s=d`, they also
contain `K,z,a_3`.  Thus every right-rail replacement remains below its new
global cap.  Letter (5.3) is seen by all `C_1,...,C_d`, which all contain
`f_(d+1)`.

The old bridge owners reconstruct as before, except that (5.3) now supplies
the one terminal filler needed by `E`.  For `C_t`, the suffix of the right
rail supplies

\[
 K\cup\{z,a_3\}\cup F[t+1,d],
\]

letter (5.3) supplies `f_(d+1)`, and the unchanged maximal-envelope anchor
at position `3d+3+t` supplies `x_1,...,x_t`.  Their union is exactly `C_t`.
All modified letters lie below their caps, so no owner overshoots.

For residence, the old right-clipped run of `f_s` gains exactly `s-1`
owners and reaches length

\[
                         (d-s+2)+(s-1)=d+1.            \tag{5.5}

The terminal `f_(d+1)` occurrence gains all `d` new owners and also reaches
length `d+1`.  Each `x_s` has a run ending at the new component boundary;
all earlier internal runs retain their old lower bound. \(\square\)

The continued protected owner path has

\[
 3d+4\text{ owners},\qquad 3d+3\text{ transitions},
 \qquad d+4\text{ upper-support values}.              \tag{5.6}

Its upper nullity is still

\[
                         (3d+3)-(d+4)=2d-1.            \tag{5.7}

Thus a q1-rainbow residence collar does not increase Catalan connector debt.
It exports the new nested `x_s` boundary state, however.  If this component
is placed internally in the global Hamilton path, those clipped runs still
need continuation.  Placing it at one global endpoint removes one side of
the residence debt but does not prove the final port-path or source/compiler
embedding.

## 6. Exact frontier

The full occurrence-preserving owner-layer problem is now exactly:

1. choose a compatible `M0` phase;
2. solve the common extension (2.3), of which Theorem 3.1 already closes the
   upper/tail projection;
3. find the `C-2d`-edge directed free-port Hamilton path;
4. preserve the literal source cap and clipped residence state under that
   global attachment.

For the native support problem, the twelve auxiliary occurrences can be
dropped and step 2 contracts only the bridge.  Neither form transports the
exterior lower compiler; that remains a separate common-cap/background
row.

The new result therefore does not prove a global extension.  It proves that
the double-crossrail bank has no hidden upper-count or rooted-tail Hall
obstruction, identifies the exact `2d-1` connector charge of its repeated
occurrences, and isolates the remaining central obstruction as

\[
 \boxed{
 \text{other-head + graphic common extension, followed by a protected
 free-port Hamilton path.}}
\]
