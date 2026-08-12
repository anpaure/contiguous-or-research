# K17 unrestricted signed packets, protected ejection, and square absorption

Date: 2026-07-31  
Lane: A, structural exact-equality theorem  
Status: exact unrestricted completion equivalence, signed-packet normal form,
and deterministic topology absorber.  No claim that
\(\nu(17)=B(17)=24313\) is made.

## 0. Verdict

The current K17 obstruction is not the 1,061 source colours left unrecycled
by one scaffold, nor the 926/892 residual matching ranks obtained after one
minimal frozen cut closure.  Those quantities change under provider
reselection, extra ejection, and fragment reversal.

There are exactly three logically separate gates.

1. A selected occurrence-labelled provider/witness bank must itself be
   independent in the tail, head, lower-colour, physical-edge, and graphic
   systems.  A repeated fixed colour, a fixed seam whose source-colour edge
   is protected, a degree excess, or a forced cycle is a monotone obstruction
   to every completion retaining that bank.
2. After those fixed resources pass, unrestricted residual completion is a
   physical tail--head--colour--graphic common-extension problem with eventual source
   ejections and graphic connectivity.  An owner--colour incidence flow is
   only its degree projection.
3. A connected upper-complete resident carrier still needs the exact K17-FRS
   staircase/common-cap certificate before it gives a word of length 24313.

The new positive statement is a deterministic signed repair theorem.  A
rainbow path forest with \(p\) components can be completed after deleting
\(d\) releasable edges exactly by a packet of \(p+d-1\) Johnson seams whose
colours are all but one colour in the disjoint deficit set consisting of the
\(d\) released colours and the \(p\) old missing colours, and whose contracted
chronology is one directed path.  Once an exact residual degree cover exists, a jointly protected bank
of colour-balanced \(2\times2\) switches absorbs its cycle components into
the distinguished path without changing any tail, head, or colour load.

## 1. Physical setup and fixed certificates

Put

\[
 V=\binom{[17]}9,\qquad
 {\cal C}=\binom{[17]}8,\qquad
 N=|V|=|{\cal C}|=24310.                             \tag{1.1}
\]

Let \(F\) be the authenticated physical lower-rainbow Johnson 2-factor.
For every \(c\in{\cal C}\), write \(f_c\) for the unique physical edge of
\(F\) having lower colour \(c\).  The two orientations of one physical edge
are distinct directed options but are parallel elements in the physical
graphic system.

A **complete certificate choice** \(\Gamma\) consists of:

* one occurrence-labelled consecutive directed witness block for every
  upper target required of the carrier;
* one complete state-labelled collar realization for every context-dependent
  seam selected by those witnesses; and
* every orientation, run-state, and protected-support literal used by those
  certificates.

Let the ground elements of \(G_\Gamma\) be permitted **state-labelled directed
arc options**.  Every option \(e\) has a directed physical-arc projection
\(a(e)=(u,v)\), an underlying unoriented physical edge \(\underline e\), and
a lower colour \(\chi(e)\).  All option copies with the same physical arc
have the same tail, head, and colour, and all copies of the same unoriented
physical edge are parallel in the graphic matroid below.  Compatible labels
forced on one physical directed arc are coalesced into one selected option;
incompatible labels make \(\Gamma\) inadmissible.

Let \(P(\Gamma)\) be the set of these coalesced state-labelled option
representatives forced by the certificates.  Repeated compatible reasons for
one option consume one resource, not several.  The optional part of
\(G_\Gamma\) contains every state-labelled factor orientation and literal
Johnson seam/collar option permitted together with \(\Gamma\).

Call \(\Gamma\) **admissible and extension-closed** when all of its non-arc
state literals are jointly consistent, \(P(\Gamma)\subseteq G_\Gamma\),
and every four-system-independent option set which contains \(P(\Gamma)\)
and projects to a degree-feasible path is jointly state-consistent and still
realizes the selected certificates.  For a consecutive witness block the
support-local part follows by saturating its internal owners.  For a boundary
collar or run state it is a separate hypothesis: the option/state language
must include enough context that an optional exterior arc cannot invalidate
the certificate.

On \(G_\Gamma\), use the following independence systems:

* \(M_{\rm out}\): capacity one at every directed tail;
* \(M_{\rm in}\): capacity one at every directed head;
* \(M_{\rm col}\): capacity one in every colour class;
* \(M_{\rm gr}\): the graphic matroid after projecting to underlying physical
  edges, with every state/orientation copy of one physical edge treated as a
  parallel element.

## 2. Exact unrestricted protected completion theorem

### Theorem 2.1 (protected-ejection four-matroid extension equivalence)

For a fixed admissible extension-closed complete certificate choice
\(\Gamma\), the following are
equivalent.

1. There is a connected coherently oriented Hamilton path on \(V\), using
   permitted options of \(G_\Gamma\), which retains every certificate in
   \(\Gamma\) and uses every lower colour except one exactly once.
2. \(P(\Gamma)\) is independent in all four systems and the contractions

   \[
    M_{\rm out}/P(\Gamma),\quad M_{\rm in}/P(\Gamma),\quad
    M_{\rm col}/P(\Gamma),\quad M_{\rm gr}/P(\Gamma)       \tag{2.1}
   \]

   have a common independent set of size

   \[
                         N-1-|P(\Gamma)|.                 \tag{2.2}
   \]

This is an exact physical equivalence.  It is not an ordinary Hall theorem
and not a conclusion from four separate rank inequalities.

#### Proof

A path in part 1 is independent in every listed system, so deleting its
forced subset gives the common independent set in (2.2).

Conversely, adjoin a common set of size (2.2) to \(P(\Gamma)\).  The result
has \(N-1\) physical arcs.  Graphic independence makes it a forest, hence a
spanning tree on the \(N\) owners.  Tail and head capacities imply undirected
degree at most two.  The tree is therefore one path.  At each internal owner
one arc enters and one leaves, so the orientation is coherent from the
unique initial owner to the unique terminal owner.  Colour independence
leaves exactly one of the \(N\) colours unused.

Every selected witness block is a directed path whose internal owners are
already saturated by its forced arcs.  It therefore occurs consecutively in
the final path.  Admissibility and extension-closedness then supply joint
state consistency and retain every fixed collar/run certificate.  Thus every
certificate in \(\Gamma\) survives literally. \(\square\)

### Corollary 2.2 (global disjunction over literal certificate banks)

Let \(\mathfrak G\) be an exhaustive refinement of the literal certificate
language: every acceptable final chronology induces at least one admissible
extension-closed \(\Gamma\in\mathfrak G\), recording one occurrence per
required target and its complete state context.  Then an unrestricted
protected completion exists if and only if condition 2 of Theorem 2.1 holds
for at least one \(\Gamma\in\mathfrak G\).

#### Proof

Apply Theorem 2.1 to the bank induced by a completion for necessity, and to
the successful bank for sufficiency. \(\square\)

### Corollary 2.3 (exact fixed-bank obstructions)

No completion retaining \(\Gamma\) exists if any of the following holds:

\[
 |P(\Gamma)\cap\chi^{-1}(c)|\ge2,\qquad
 |P(\Gamma)\cap\delta^+(v)|\ge2,\qquad
 |P(\Gamma)\cap\delta^-(v)|\ge2,\qquad
 \deg_{P(\Gamma)}(v)>2,                                \tag{2.3}
\]

if two opposite orientations of one physical edge are forced, or if the
underlying forced bank contains a cycle.  These obstructions are monotone
under adding residual arcs.

They are conditional on retaining \(\Gamma\).  If a provider or protected
witness is reselected, the forced bank changes; (2.3) is not a global K17
no-go.

## 3. Source ejection is exactly resource-neutral

Let \(Q\) be a spanning physical directed rainbow path forest with \(p\)
components.  Physical factor membership ignores orientation.  Define

\[
 C(Q)=\{c:f_c\notin E_{\rm phys}(Q)\},\qquad
 R(Q)=E_{\rm phys}(Q)\setminus E_{\rm phys}(F),        \tag{3.1}
\]

and let \({\cal M}(Q)\) be the missing lower-colour set of \(Q\).

### Lemma 3.1 (colour-by-colour ejection identity)

For every \(c\in{\cal C}\),

\[
 \boxed{
  {\mathbf 1}_{c\in C(Q)}
   =|R(Q)\cap\chi^{-1}(c)|+{\mathbf 1}_{c\in{\cal M}(Q)}.}
                                                               \tag{3.2}
\]

Consequently

\[
 |C(Q)|=|R(Q)|+p,\qquad |{\cal M}(Q)|=p.             \tag{3.3}
\]

#### Proof

If \(f_c\) is retained, colour rainbowness forbids every nonfactor edge of
colour \(c\), and \(c\) is not missing.  If \(f_c\) is absent, the forest
either uses one nonfactor edge of colour \(c\) or misses \(c\); these cases
are exclusive and exhaustive.  A spanning \(p\)-component forest has
\(N-p\) edges, all with distinct colours, so it misses exactly \(p\)
colours.  Summing (3.2) proves (3.3). \(\square\)

There is an equally exact endpoint ledger.  Put

\[
                         \pi_v=2-\deg_Q(v).                 \tag{3.4}
\]

Thus \(\pi_v\in\{0,1,2\}\), with value two only at an isolated owner, and
\(\sum_v\pi_v=2p\).  Then

\[
 \boxed{
  \deg_{R(Q)}(v)+\pi_v
       =\sum_{c:\,v\in f_c}{\mathbf 1}_{c\in C(Q)}.}       \tag{3.5}
\]

Indeed both sides equal
\(2-\deg_{E_{\rm phys}(F)\cap E_{\rm phys}(Q)}(v)\).  After orienting the
components, (3.4) is equivalently \(p\) free exits and \(p\) free entries.

Equations (3.2) and (3.5) prove the precise ejection law: deleting one
additional unprotected rainbow-forest edge creates one component, one free
exit, one free entry, one missing colour, and one additional required return
seam.  It creates geometric routing choice and no scalar slack.

### Corollary 3.2 (the two scaffold faces)

If \(F_c\) is the multiplicity of immutable nonfactor seams of colour \(c\)
and \(h_{f_c}=1\) means that the source edge \(f_c\) is protected, then the
exact immutable colour precheck is

\[
                         F_c+h_{f_c}\le1.                   \tag{3.6}
\]

Repeated fixed seams or a fixed seam sharing a colour with a protected
source edge are fatal colour obstructions.  A fixed seam sharing a colour
with a currently retained but unprotected source edge is not by itself a
colour obstruction: (3.2) permits that source edge to be ejected later.
Tail, head, graphic, state, or compiler constraints may still make the
instance infeasible.

Thus the stronger row

\[
       F_c\le\widehat c_c                                  \tag{3.7}
\]

is exact only when the current scaffold cut \(\widehat c\) is already the
final cut bank.

## 4. Exact signed absorption-packet normal form

Let \(Q\) be the \(p\)-component rainbow path forest of Section 3.  Delete
a set \(D\subseteq E_{\rm phys}(Q)\) of \(d\) releasable physical edges.
The underlying forest \(Q-D\) has \(p+d\) path fragments.  Choose an allowed
orientation \(\omega\) of every fragment, respecting all immutable directed
subblocks, and denote the resulting directed fragment forest by
\((Q-D)^\omega\).  Let \(A\) be a set of directed literal Johnson arcs, on
physical edges outside \(E_{\rm phys}(Q)\), from oriented fragment exits to
oriented fragment entries.  We use the normalized convention that a physical
edge common to the old and new forests is retained, not simultaneously listed
in both \(D\) and \(A\).

### Theorem 4.1 (signed packet equivalence)

Fix

\[
 b\in {\cal M}(Q)\ \dot\cup\ \chi(D).                       \tag{4.0}
\]

The graph

\[
                         Q'=(Q-D)^\omega\cup A                \tag{4.1}
\]

is one coherently oriented Hamilton path using every lower colour except
\(b\) exactly once if and only if both conditions below hold.

1. After contracting the \(p+d\) oriented fragments, \(A\) is one directed
   Hamilton path.
2. As a literal multiplicity-one identity,

   \[
    \boxed{
      \chi(A)=
       \bigl(\chi(D)\ \dot\cup\ {\cal M}(Q)\bigr)
                  \setminus\{b\}.}                         \tag{4.2}
   \]

Necessarily

\[
                             |A|=p+d-1.                      \tag{4.3}
\]

#### Proof

Deleting \(d\) edges from a \(p\)-component forest gives \(p+d\) fragments.
Condition 1 joins them by \(p+d-1\) arcs and expands to a coherent Hamilton
path on all owners.

Before adding \(A\), the retained colour set is

\[
 {\cal C}\setminus\bigl({\cal M}(Q)\cup\chi(D)\bigr).
\]

The union is disjoint because \(D\subseteq Q\) and \(Q\) is rainbow.
Condition (4.2) restores every colour absent after deletion except \(b\), and
introduces no repetition.  This proves sufficiency.

Conversely, assume the fixed normalized data produce such a Hamilton path.
Because \(A\) uses no physical edge of \(Q\), normalization gives

\[
 D=E_{\rm phys}(Q)\setminus E_{\rm phys}(Q'),
 \qquad
 A=\{a\in E(Q'):\underline a\notin E_{\rm phys}(Q)\}.       \tag{4.4}
\]

Every
component of the common physical forest \(Q-D\) occurs as one contiguous
fragment in \(Q'\): each internal owner is already saturated by its two common
physical edges.  Its traversal in \(Q'\) supplies \(\omega\), possibly the
reverse of its traversal in \(Q\).  Contraction therefore gives condition 1.
Comparing the two literal rainbow colour sets forces (4.2), and the edge count
gives (4.3). \(\square\)

### Corollary 4.2 (exact upper-protection test)

For each required upper target \(T\), let \({\cal W}_T\) be its complete
occurrence-labelled consecutive witness family.  The packet of Theorem 4.1
is all-target protected if and only if every \(T\) has either

* an old occurrence whose physical block lies in one fragment of
  \((Q-D)^\omega\) and whose traversal under \(\omega\) is still an allowed
  occurrence in \({\cal W}_T\), or
* a new literal witness in the final fragment order.

For immediate upper colours this reduces to the corresponding occurrence
count after deleting and adding edges.  For deeper targets, scalar counts are
not sufficient: the whole consecutive block is required.

Only coordinate runs meeting a deleted or added boundary can change their
lengths.  Reversal preserves internal run lengths, swaps prefix with suffix,
and sends an internal interval \([s,s+\ell)\) in a fragment of length \(L\)
to \([L-s-\ell,L-s)\).  Residence is therefore
decidable by literal final replay.  A compressed boundary-state composition
is exact only when its state contains the fragment length, endpoint bits,
clipped prefix/suffix run lengths, constant and internal-failure flags, and
every relative offset needed by the deadline staircase.  Separate locally
safe seams do not imply global residence when two collars interact through a
short fragment.

## 5. Graver moves are the complete algebraic repair language

Fix \(\Gamma\), the path endpoints, and the omitted colour \(\beta\).  Give every arc
variable bounds \(0\le x_a\le1\), encode the exact path tail, head, and colour
equations, and turn each physical-edge
opposite-orientation inequality into an equality with a bounded slack
variable.  Fix every arc in \(P(\Gamma)\) to one.  Any further guard is in the
scope below only when it is represented exactly by bounded integer auxiliary
variables and linear equations.  Let

\[
 {\cal F}_\Gamma(\beta)=
   \{x\in\mathbb Z^g:A_\Gamma x=r_{\Gamma,\beta},\
                         \ell\le x\le u\}                  \tag{5.1}
\]

be this bounded exact guarded fibre, where \(A_\Gamma\) is integral (clear
denominators first if necessary) and \(r_{\Gamma,\beta}\) is its integer
right-hand side.  Its arc coordinates are
binary because they are integral and lie in \([0,1]\).  The exact endpoint
equations make every point one directed endpoint-to-endpoint path plus zero
or more vertex-disjoint directed cycles; graphic connectedness is the
remaining property.

For integer vectors \(g,z\), write \(g\sqsubseteq z\) when they have the same
coordinatewise signs and \(|g_i|\le|z_i|\) for every \(i\).  A nonzero
kernel vector is **primitive** if it is minimal under \(\sqsubseteq\).

### Theorem 5.1 (Graver connectivity of the exact guarded fibre)

Any two points \(x,y\in{\cal F}_\Gamma(\beta)\) are joined by a finite sequence
of primitive conformal kernel moves (Graver moves).  Every intermediate point remains in
\({\cal F}_\Gamma(\beta)\) and retains every fixed protected arc.

#### Proof

If \(x=y\), there is nothing to prove.  Otherwise the difference \(z=y-x\)
lies in the integer kernel of \(A_\Gamma\).  If it is primitive, use it.
Otherwise choose a nonzero primitive
\(g_1\sqsubseteq z\), subtract it, and continue by induction on
\(\|z\|_1\).  This gives a conformal decomposition

\[
                             z=g_1+\cdots+g_s.               \tag{5.2}
\]

For every \(j\), the point
\(x+\sum_{i\le j}g_i\) lies coordinatewise between \(x\) and \(y\), hence
obeys the same bounds.  Each move is in the kernel, so all equations remain exact.
Coordinates fixed by \(\ell_i=u_i\) cannot move. \(\square\)

This theorem has two consequences which matter for the finite search.

* Failure of every \(2\times2\) switch is only a no-go for that move family.
  It is not a global completion obstruction; a larger Graver move may be
  necessary.
* If the exact guarded fibre contains a connected point, then every degree
  cover in that fibre has a finite Graver-move route to a connected point.
  The route need not improve component count monotonically, and nonlinear
  residence/compiler conditions must either be included in the finite guard
  state or checked on the final chronology.

Thus an abstract incidence flow does not suffice: its columns need not lift
to the physical directed-arc fibre (5.1).

## 6. Deterministic colour-balanced square absorber

Let \(Q_0\in{\cal F}_\Gamma(\beta)\) consist of one directed path and directed
cycles.  Choose an edge

\[
 e=x\longrightarrow x'
\]

of the current root path and an edge

\[
 f=y\longrightarrow y'
\]

of a different directed cycle.  Suppose the cross-arcs

\[
 a=x\longrightarrow y',\qquad a'=y\longrightarrow x'       \tag{6.1}
\]

are literal permitted Johnson arcs and

\[
                  \{\chi(a),\chi(a')\}
                     =\{\chi(e),\chi(f)\}                  \tag{6.2}
\]

as multisets.  Assume also that no physical-edge antisymmetry row is
violated and that the four-edge replacement, together with its state
variables, is a feasible kernel move of the exact guarded fibre
\({\cal F}_\Gamma(\beta)\).

### Lemma 6.1 (one protected square absorbs one cycle)

The switch

\[
 Q_1=(Q_0\setminus\{e,f\})\cup\{a,a'\}                    \tag{6.3}
\]

preserves every tail load, head load, lower-colour load, global endpoint,
and omitted colour \(\beta\), and merges that cycle into the root path.

If \(e,f\notin P(\Gamma)\), every selected witness block avoids the deleted
edges, and the two new seams have the full collar states asserted in the
guarded-fibre move, then the switch also retains the entire protected upper
tower.  A switch which instead changes a selected witness belongs to a new
certificate choice \(\Gamma'\); it is not a move in the fixed
\({\cal F}_\Gamma(\beta)\) fibre until that new bank is rebuilt and rechecked.

#### Proof

The old and new tail multisets are both \(\{x,y\}\), and the old and new
head multisets are both \(\{x',y'\}\).  Equation (6.2) preserves the colour
multiset.  In chronology order, the replacement is

\[
 \cdots\to x\to y'\rightsquigarrow y\to x'\to\cdots,
\]

where \(y'\rightsquigarrow y\) traverses the old cycle with \(f\) removed.
It is therefore one path and has one fewer component.  The protection claim
follows because every selected witness avoids the deleted edges and the exact
guarded-fibre move retains its state/collar equations. \(\square\)

### Theorem 6.2 (protected square-ear bank)

Suppose \(Q_0\) has cycles \(C_1,\ldots,C_s\).  If there is a sequential
bank of \(s\) switches satisfying Lemma 6.1 in the state produced by all
earlier switches, then their composition is one Hamilton path in the same
exact guarded fibre and retains the protected upper tower.

It is sufficient in particular to have a rooted tree on the initial path and
cycle components, a root-to-leaf linear order \(e_1,\ldots,e_s\) of its
edges, and an extended square-move vector

\[
                    g_{e_i}\in\ker_{\mathbb Z}A_\Gamma      \tag{6.4}
\]

for every tree edge.  Require: every square is colour-balanced and physically
permitted; its deleted old edges avoid \(P(\Gamma)\) and every selected
witness block; all old supports are pairwise disjoint; new arcs avoid all
reserved old supports and are globally physical-compatible; and, from the
initial full variable vector \(x_0\),

\[
 x_0+\sum_{i\le j}g_{e_i}\in{\cal F}_\Gamma(\beta)
                    \qquad(1\le j\le s).                    \tag{6.5}
\]

Process the tree edges in this order.  At each step the
parent side is the current root path and the child is an unabsorbed directed
cycle.  Without that tree edge the two sides of its tree cut cannot already
have merged; disjoint old supports ensure that its two deleted edges are still
present.  Lemma 6.1 therefore applies at every step.  After \(s\) switches
only the root path remains. \(\square\)

The square-ear bank is a positive, checkable topology certificate.  Its
absence is only a square-architecture obstruction.  The complete signed
repair language inside an exactly encoded fixed fibre is the Graver system of
Theorem 5.1.

## 7. Exact implication to a length-24313 word

For completeness, spell out the terminal compiler condition.  A chronology
\(T=(T_0,\ldots,T_{N-1})\) has **K17-FRS** if there are nonempty sets
\(Q_0,\ldots,Q_{N+2}\subseteq[17]\) such that

\[
 Q_i\cup Q_{i+1}\cup Q_{i+2}=T_i
                  \quad(0\le i<7401),                       \tag{7.1}
\]

\[
 Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3}=T_i
                  \quad(7401\le i<N),                       \tag{7.2}
\]

and the following multiset union is disjoint and equals the complete lower
Boolean ideal:

\[
 \{Q_i:0\le i\le N+2\}\ \dot\cup\
 \{Q_i\cup Q_{i+1}:0\le i\le N+1\}\ \dot\cup\
 \{Q_i\cup Q_{i+1}\cup Q_{i+2}:7401\le i\le N\}
 =\{S\subseteq[17]:1\le|S|\le8\}.                         \tag{7.3}
\]

### Corollary 7.1 (K17 signed-absorption GO criterion)

Suppose a complete certificate choice \(\Gamma\) and either Theorem 4.1 or
Theorem 6.2 produce one directed Hamilton owner chronology \(T\).  If

1. every upper target has a final consecutive witness in \(T\); and
2. \(T\) has K17-FRS in the sense of (7.1)--(7.3),

then there is a universal nonempty word of length

\[
                             N+3=24313.                    \tag{7.4}
\]

Together with the proved lower bound, this gives

\[
                             \nu(17)=B(17)=24313.          \tag{7.5}
\]

#### Proof

The absorption theorem supplies one exact owner chronology, while clause 1
transfers the complete upper tower.  Equations (7.1)--(7.2) are exact middle
replay, and (7.3) is the complete lower-cell atlas.  The audited exact K17-FRS
normal form therefore materializes a universal word of length 24313.  The
known lower bound gives equality. \(\square\)

K17-FRS is not implied by residence, upper completeness, marginal Hall, or
colour balance.  Residence/deadline corridors, boundary top ports, and an
integral common-cap assignment are one proved route to K17-FRS; they remain
additional simultaneous requirements on the same chronology.  The absorption
theorem closes carrier topology and colour balance, not the compiler.

## 8. Authenticated current obstructions

### 8.1 The smallest current fixed-bank circuit

The exact-active 2,649-target candidate contains the following two forced
physical edges:

\[
 0x84fb\longrightarrow0x0cfb,qquad
 0x44fb\longrightarrow0x05fb.                            \tag{8.1}
\]

The first is the chosen seam provider for target `0x8cff`.  The second is a
source edge protected by the chosen provider

\[
                 0x64f9\longrightarrow0x44fb
\]

for target `0x1e4fb`.  Both edges in (8.1) have lower colour `0x04fb`.
Let \(y_{T;u,v}\) denote selection of the particular occurrence-labelled
provider \(u\to v\) for target \(T\).  The two certificate literals obey the
deletion-minimal no-good

\[
 y_{0x8cff;0x84fb,0x0cfb}
 +y_{0x1e4fb;0x64f9,0x44fb}\le1.                         \tag{8.2}
\]

No extra ejection, residual b-flow, fragment reversal, or topology splice can
retain both: the final path has colour capacity one.  This is the smallest
possible nonloop circuit.  It is not a global K17 obstruction, because either
provider/witness certificate may be reselected.

The full exact-active candidate has 2,908 pairwise colour-distinct seams, but
1,142 seam/protected-source colour circuits and one forced directed cycle of
length nine.  It therefore fails before residual flow.  Its frozen lineage
is

```text
scratch/threadD_k17_alltarget_residual_completion_20260731/
    exactactive2649_round0.candidate.json
SHA-256 fd7594bc0cd6bd050e21997d4444e7be795bd0db0a92c079e44afd51b7f345b4

scratch/threadD_k17_alltarget_residual_completion_20260731/
    exactactive2649_round0.lower_gate.audit.json
SHA-256 18b5d274ec4a6867767ad969fbaacb64a08347f2ec3d73dfccf9e8f69816eab9
payload  8e963fe465dd6b04508590f518cd53e056c2205e3598f10ca1b81d6d7b14b292

scratch/threadD_k17_alltarget_residual_completion_20260731/
    exactactive2649_round0.lower.audit.json
SHA-256 c927d6a0bb90e24cd4c22154155eeff713ba6f3ae7e4037d9615411bbc5e6714
payload  a5c08b96c21fcd1e96b4517bd4175f40aa0eddaf615c1452df0cd8d103b026b9
```

### 8.2 Fixed seams versus releasable old edges

The hard323 bank has 1,564 fixed seams on 1,527 colours.  Its repeat excess
37 consists of 37 doubleton colour classes, so at least one seam from every
class must be released.  One explicit circuit is

\[
 0x326f\longrightarrow0x1322f,qquad
 0xb22f\longrightarrow0x332f,                            \tag{8.3}
\]

both of colour `0x322f`.  This excludes completion retaining that fixed seam
bank.

Of its 1,061 seam colours whose source edge remains in the current scaffold,
312 meet the exported protected source bank and are fixed-bank conflicts.
Among the other 749, exactly 741 have one fixed seam and are pure ejection
obligations; the remaining eight have two fixed seams and already belong to
the 37 fatal duplicate-colour classes above.  The current two cycles of
lengths 3 and 13 are likewise not forced-bank cycles; ejectable old edges may
break them.

The hard323 candidate and its exact lower-gate audit have SHA-256 values
`2c29f2f804ab5f08d3059fe3a3455fd9c174a30e35c18f450a9132422d22f15d`
and `7519ee3bb62cd8faf82fe83a0409216b25dbde28b7ed3ebbce6667c4a213a084`,
respectively.

### 8.3 No-gos which do not survive unrestricted completion

There is one new quantitative theorem inside the frozen provider/orientation
face.  Its scope is useful precisely because it must not be globalized.

### Lemma 8.1 (605 extra-ejection floor in the frozen face)

For the authenticated 1,838-provider selection, retain all chosen providers
and their protected source edges, keep the source successor orientation and
minimal 3,336-cut closure fixed, and permit only additional canonical
source-edge ejections.  Any such completion requires at least 605 additional
cuts.

#### Proof

The minimal face has 1,498 residual tails, heads, and cut colours, and needs
1,497 returns.  Its full-Johnson tail--colour and colour--head projection
ranks are respectively

\[
                              926,\qquad 892.              \tag{8.4}
\]

In the authenticated projections,

\[
 (t,c_i)\in E_{TC}\iff c_i=i\cap s(i)\subset t,
 \qquad
 (c_i,h)\in E_{CH}\iff c_i\subset s(h).                  \tag{8.5}
\]

Thus adding \(d\) canonical cuts adds exactly \(d\) vertices to each shore
of either projection and leaves its induced old--old graph unchanged.  Delete
from any enlarged matching every edge incident with a new vertex.  At most
\(2d\) matching edges disappear, so

\[
 \nu_{TC}(d)\le926+2d,qquad
 \nu_{CH}(d)\le892+2d.                                  \tag{8.6}
\]

The enlarged completion requires \(1,497+d\) matched pairs.  Hence

\[
 d\ge1497-926=571,qquad d\ge1497-892=605.              \tag{8.7}
\]

The second inequality proves the claim. \(\square\)

Provider reselection, fragment reversal, or release of the frozen provider
bank changes the old--old projection, so Lemma 8.1 is not a global K17 lower
bound.

The following authenticated failures have only the stated restricted scope.

* The fixed-minimal-cut protected-provider face has required residual size
  1,497 and tail--colour/colour--head ranks 926/892.  Extra ejection,
  fragment reversal, or provider reselection changes that residual graph.
* A row using the present scaffold cut in place of the eventual cut excludes
  legal ejections and is not an unrestricted row.
* Positive upper-hole counts and rotating casualty banks are incumbent
  diagnostics, not global obstructions.
* Failure of a square bank, a fixed-orientation completion, or one incidence
  b-flow does not exclude a larger Graver move or another
  certificate choice.

No audited artifact proves unrestricted K17 impossibility.

## 9. Sharp remaining gate and handoff to computation

The exact structural target for the computational lane is now:

1. choose one complete occurrence-labelled certificate bank \(\Gamma\) for
   all upper targets;
2. reject immediately every tail, head, colour, physical-edge, and graphic
   circuit in \(P(\Gamma)\), including rows such as (8.2);
3. solve the unrestricted eventual-ejection degree fibre, with every source
   ejection paying both endpoint incidences through (3.5);
4. either enforce graphic independence in that common-extension solve, or export
   one degree cover and a jointly protected square-ear/Graver-move bank;
5. replay the final upper tower and residence state; and
6. solve the exact K17-FRS/common-cap compiler on that same chronology.

The smallest unproved carrier-side positive hypothesis is not marginal Hall.
It is the existence of one certificate choice \(\Gamma\) whose fixed bank is
four-system independent and whose physical contracted port hypergraph has a
target-size tail--head--colour--graphic common independent extension.  If
computation first finds only a degree cover, Theorems 5.1 and 6.2 specify the
complete algebraic repair system and the smallest practical topology
absorber.  Exact equality additionally requires K17-FRS on that same final
chronology; the common extension alone does not imply it.

This theorem package does not rerun or supersede D's solver.  It supplies the
proof interface and the exact scope of every certificate or no-good that D
may export.
