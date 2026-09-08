# Audit of the fixed-`z` two-bank collar: local PASS, private-closure and host-scope corrections

**Date:** 2026-08-02  
**Lane:** A, adversarial completed-ticket audit  
**Audited source:**
`MATH_THEOREM_A_FIXED_Z_TWO_BANK_DECODABLE_HISTORY_COLLAR_AND_BOUNDED_LOAD_SUBATLAS_20260802.md`  
**Verdict:** The local owner/facet construction, exact atlas count, forward
and reverse history tests, and bounded decoder are correct after one explicit
private-closure convention.  The stated cross-task greedy and provider rows
need the corrections in Sections 5--6.  No finite search is used.

## 1. Local path and count audit

The four banks satisfy

\[
 D^x\dot\cup D^y\subset X-\{a,b,c\},\qquad
 M^x\dot\cup M^y\subset[k]-X,                          \tag{1.1}
\]

and all seven active roles and `z` avoid the appropriate banks.  Hence every
central endpoint contains both deletion banks and avoids both marker banks.

For an endpoint `E` of type `epsilon in {x,y}`, the ray

\[
 E_j=(E-D^\epsilon_{[j]})\cup M^\epsilon_{[j]}          \tag{1.2}
\]

has facet

\[
 G_j=E-D^\epsilon_{[j]}+M^\epsilon_{[j-1]}.             \tag{1.3}
\]

Every step is a Johnson transition.  Marker prefixes distinguish type and
position for owners and for facets after the first step.  At the first step,
adjoining `d^x_1` or `d^y_1` gives the only two possible central endpoints.
Within one ticket, an `x` first facet avoids `z`, while a `y` first facet
contains it, so they cannot collide.  Packet facets contain both deletion
banks, while a first ray facet omits one bank element.  These observations
prove the claimed simplicity and 2-boundedness.

The terminal bank counts are also correct:

\[
 |V_O|=14+14d,qquad |V_F|=7+14d,qquad
 |E_+|=14+28d.                                         \tag{1.4}
\]

The exact role count is

\[
 (r-1-2d)_2(k-r-2d)_4(k-r-2d-4).                      \tag{1.5}
\]

It is `Theta(k^7)` uniformly when `r/k` remains in a compact subinterval of
`(0,1)` and `d=o(k)`.

There is one ledger distinction.  Equation (1.4) counts the **terminal
protected bank**.  A literal switch-collision ledger containing both old and
new moving incidences has

\[
                         |E_-\cup E_+|=21+28d,          \tag{1.6}
\]

because the seven retained incidences are common, while the seven old and
seven new moving incidences are distinct.  Use (1.4) for terminal protected
extension and (1.6) when old/new switch supports must both be reserved.

## 2. History orientation audit

Traverse a `y` ray from its far endpoint toward `y_i`.  Its last `d`
transitions delete

\[
                         m^y_d,\ldots,m^y_1
\]

and insert

\[
                         d^y_d,\ldots,d^y_1.
\]

Thus the newest-first past insertion and deletion histories at the seam are
exactly `D^y` and `M^y`.  Traversing the `x` ray outward from `x_j` first
deletes `D^x` and inserts `M^x`.  The history orientations in the source
note are therefore correct.

The seam `y_i -> x_j` deletes `z` and inserts the unique coordinate of
`x_j-f_i`.  Both labels avoid the four banks.  Consequently:

* `D^y`, the seam labels, and `D^x` are pairwise disjoint, proving every
  positive triangular cross-collar inequality;
* `M^y`, the seam labels, and `M^x` are pairwise disjoint, proving the
  negative inequalities; and
* within one ray no coordinate is both inserted and later deleted, or both
  deleted and later inserted.

Hence no internally completed short run is hidden in a ray.  Runs meeting a
far endpoint remain conditional on the exported history socket, exactly as
the source says.

## 3. Decoder audit

For an internal owner, the intersection with `M^x union M^y` gives the type
and prefix length, and replacing the marker prefix by the deletion prefix
recovers `E`.  The same holds for facets except at `j=1`, where there are at
most the two candidates

\[
                         E_x=G+d^x_1,qquad
                         E_y=G+d^y_1.                  \tag{3.1}
\]

The ray cap at step `j` is

\[
                         U_j=E-D^\epsilon_{[j-1]}
                                  +M^\epsilon_{[j]},    \tag{3.2}
\]

so its marker signature recovers `epsilon,j,E` uniquely.  A fully
occurrence-labelled incidence or history event retains the same owner/facet
and position data.  Thus every such nonprivate resource decodes to at most
two central endpoints.

This proof does **not** apply if a “history resource” is keyed only by the
bare label pair `(d_j,m_j)`: that pair is common to all seven rays and all
tickets.  The source explicitly uses occurrence-labelled transition/state
resources and treats bare coordinate names as non-capacity data.  Under that
definition the decoder is valid; any downstream implementation must preserve
the full occurrence key.

## 4. The exact private closure

The terminal new packet has `f_6=X-{a}` and contains the fixed moving
incidence

\[
                       \iota_*=(X,\ X-\{a\}).          \tag{4.1}
\]

This incidence occurs in **every** restricted central packet.  Its load is
the full number (1.5), namely `Theta(k^7)`.  The facet `X-{a}` is likewise
common.  The complete ray based at `x_0=X` contributes common owners,
facets, incidences, caps, and history events.

Therefore the load theorem is correct only with the following explicit
private closure:

\[
 \mathcal P_{X,a}=
   \{X,\ X-\{a\},\ \iota_*\}
   \cup\{\hbox{every owner, facet, incidence, cap and history occurrence
                   of the `X` ray}\}.                  \tag{4.2}
\]

The four coordinate banks are private data as well, although bare labels are
not capacity-one resources.  With (4.2), a nonprivate collar resource cannot
decode to `X`: equality with an `X`-ray resource would make the resource a
member of (4.2).  The source phrase “belongs to the fixed rooted anchor
`(X,a)`” can be read as (4.2), but it should be stated literally.  If it is
read as only the owner `X`, the coordinate `a`, and the four label banks,
then (4.1) is the smallest counterexample to Theorem 4.1.

After this correction, the bound `2K_0k^6` follows from the decoder and the
central endpoint load theorem.

## 5. Cross-task privacy is not automatic

A resource can be private, hence have load `Theta(k^7)`, in one task atlas
and nonprivate in another.  The one-line greedy proof in Corollary 4.2 uses
the later atlas load of every resource in the already selected ticket.  It
therefore fails if that resource is private in the later atlas.

A proof-safe correction is to choose all private closures first, require
private--private capacity compatibility, and prefilter

\[
 \mathcal A_i'=
 \{T\in\mathcal A_i:
      T\cap\bigcup_{j\ne i}\mathcal P_j=\varnothing\}. \tag{5.1}
\]

Let `p_d=max_i|mathcal P_i|=O(d)`.  Every foreign private resource which is
nonprivate in atlas `i` deletes at most `2K_0k^6` tickets.  Therefore

\[
 |\mathcal A_i'|
 \ge N_d-2K_0(H-1)p_dk^6.                              \tag{5.2}
\]

Once (5.1) is imposed, ordinary greedy selection on the nonprivate supports
is valid.  A sufficient exact inequality is

\[
 N_d>2K_0(H-1)(p_d+S_d)k^6,                            \tag{5.3}
\]

where `S_d` bounds the nonprivate support of one ticket.  Fixed `H` and
`d=o(k)` still give the advertised asymptotic conclusion.

Thus “private banks chosen compatibly” must include (5.1), or an equivalent
cross-private avoidance theorem.  Pairwise disjointness of the private banks
alone is insufficient for the displayed greedy proof.

## 6. Provider and middle-level scope

The protected two-factor extension invoked in Section 5 is a theorem for
the middle-level inclusion graph on ground size

\[
                             k=2r-1.                    \tag{6.1}
\]

For general `k,r` the rank-`(r-1)` and rank-`r` shores need not even have the
same size, so the spanning two-factor conclusion does not follow.  Sections
1--4 are valid for general `k,r`; the provider/extension conclusion must add
(6.1), or invoke a different balanced host theorem.

For `H` selected tickets, provider postselection must be applied once to the
union bank, not separately to each ticket.  With pairwise-disjoint terminal
banks and `q_tot` total named backups, the direct bounds are

\[
\begin{aligned}
 v_O(P)&\le H(14+14d),\\
 v_F(P)&\le H(7+14d),\\
 L&=H(14+28d).
\end{aligned}                                           \tag{6.2}
\]

The sufficient provider inequalities are therefore

\[
 {r+1-H(14+14d)-2q_{tot}\choose2}
       >H(7+14d)+q_{tot},                              \tag{6.3}
\]

and

\[
                       H(14+28d)+2q_{tot}\le r-2.       \tag{6.4}
\]

The one-ticket equations in the source are correct for one ticket but are
not by themselves the postselection theorem used after the `H`-task
transversal.  For fixed `H`, `q_tot=O(Hd)`, and `d=o(r)`, (6.3) is eventually
automatic and (6.4) is the protected-edge budget.

Provider postselection removes provider-resource loads from the ticket
atlas only because (6.3)--(6.4) choose all providers jointly after all
tickets.  A canonical provider attached separately to every ticket would
reintroduce a common high-load resource.

## 7. Topology, phase and marginal scope

No topology overclaim was found in the local theorem.  The source correctly
retains as hypotheses that:

1. every `y` ray is traversed inward and every `x` ray outward;
2. the seven exterior continuations put the old cuts on one co-oriented
   quotient cycle in step-one order;
3. the step-two rethread is one quotient cycle;
4. the far sockets receive accepting exterior histories; and
5. a quotient development needs an equivariant in-place theorem rather than
   the literal `O(d)` protected-extension bound.

The zero seam-displacement statement is valid under those orientations.
Reversing a retained fragment or splitting the output requires the signed
per-fragment ledger, as the source explicitly notes.

The sentence that topology/exterior is “the only missing part of a fully
completed fixed-`z` ticket” should be read only inside the local
owner/q1/collar/cap layer.  Protected deeper upper witnesses,
source/compiler incidences, aperture return, and a child-native unit-voltage
seed remain additional rows, as Sections 6--7 of the source themselves say.

## 8. Final verdict

With the literal private closure (4.2), occurrence-labelled history keys,
the cross-private prefilter (5.1), and middle-level/provider scope
(6.1)--(6.4), the two-bank construction gives exactly what its local status
claims:

\[
 \Theta(k^7)\text{ central packets},\qquad
 O(d)\text{ local resources/ticket},\qquad
 O(k^6)\text{ nonprivate local load}.                  \tag{8.1}
\]

Without (4.2), the single incidence `iota_*` is a literal
`Theta(k^7)`-load counterexample.  No ray collision or sign error remains
after the stated corrections.  The construction still does not supply the
one-cycle exterior, arbitrary-width upper/source/compiler return, or an
equivariant protected host.

## 9. Provenance

The audited source had SHA-256

```text
303d80847434a62976c902acedf9a74dc9e8beecebd609aec1ee06cc71357872
  MATH_THEOREM_A_FIXED_Z_TWO_BANK_DECODABLE_HISTORY_COLLAR_AND_BOUNDED_LOAD_SUBATLAS_20260802.md
```
