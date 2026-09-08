# The K16 two-shift trace and the 49-facet bridge

Date: 2026-07-31  
Status: exact finite theorem and conditional general cut/jump lemma; no
all-dimension RSB conclusion

## 1. Frozen inputs and conventions

Let `D` denote adjacent OR on a linear word and put

\[
 T=D^3(\texttt{answers/k15.word}),\qquad
 S=D^3(\texttt{answers/k16.word}).
\]

The authenticated hashes are

```text
answers/k15.word  f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
answers/k16.word  890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

Thus `T` has length 6435 and is the simple rank-eight parent deck.  Its
underlying exact factor has a large cycle

\[
 C_L=(T_0,\ldots,T_{6389})
\]

and a small cycle

\[
 C_s=(T_{6390},\ldots,T_{6434})
\]

of lengths (6390=15\cdot426) and (45=15\cdot3).

Write (z=2^{15}).  Delete (z) from the (6435) members of (S) which
contain it, preserving occurrence order, and call the result (M).  Call
the other (6435) members (U).

## 2. Exact componentwise formula

### Theorem 2.1

The unmarked subsequence is

\[
\begin{split}
 U={}&T[5112,6390)\,T[0,5112)\\
    &T[6426,6435)\,T[6390,6426).                 \tag{2.1}
\end{split}
\]

Equivalently its four chunk lengths are

\[
 1278,5112,9,36
 =3\cdot426,12\cdot426,3\cdot3,12\cdot3.        \tag{2.2}
\]

The rank-eight part of the marked projection is

\[
 M[0,6386)=T[5113,6390)\,T[0,5109).             \tag{2.3}
\]

Consequently it is the large cycle rotated one vertex past the common cut,
with the four consecutive vertices

\[
             T_{5109},T_{5110},T_{5111},T_{5112}                \tag{2.4}
\]

deleted.  Its remaining 49 entries have rank seven.

#### Proof

These are literal entrywise identities.  The arithmetic is structural:
both parent cycles are strict 15-sheet spirals with bases 426 and 3, and
both are cut after sheet 12.  Thus the complementary sheet counts are
(3+12), yielding (2.2).  In the voltage-(+4) presentation, sheet 12 is
also the clean-subgroup step because

\[
                        4\cdot12\equiv3\pmod {15}.              \tag{2.5}
\]

No formula for *choosing* this cut in a general dimension is asserted.
The audit cited in Section 6 checks every equality.  \(□\)

### Corollary 2.2 (why the two offsets differ by 45)

For (0\le j<1277),

\[
 M_j=T_{j+5113},
\]

while for (1277\le j<6386),

\[
 M_j=T_{(j+5158)\bmod6435}.
\]

The difference is

\[
                         5158-5113=45.             \tag{2.6}
\]

This is not a new dynamical period.  The first piece wraps at the end of a
component of length 6390, whereas the displayed subscripts are reduced
modulo the full concatenated deck of length (6435=6390+45).  Resetting
the index to zero after the large-cycle wrap therefore adds exactly the
skipped small-component length 45.

## 3. Exact 49-facet bridge

For a vertex (T_i) in one of the two closed Johnson cycles, let

\[
 e_i=T_{i^-}\cap T_i                                      \tag{3.1}
\]

be its incoming turn colour, where (i^-=i-1) inside a component and
(6390^-=6434) at the small-cycle closure.  Define

\[
 R=\{5109,5110,5111,5112\}\cup\{6390,\ldots,6434\}.       \tag{3.2}
\]

### Theorem 3.1

The last 49 entries of (M) are, in order,

\[
\begin{split}
 &(e_{5109},e_{5110},e_{5111},e_{5112}),\\
 &(e_{6426},\ldots,e_{6434},e_{6390},e_{6391},\ldots,e_{6425}). \tag{3.3}
\end{split}
\]

They are 49 distinct rank-seven sets.  The map

\[
                       e_i\longmapsto T_i\qquad(i\in R)        \tag{3.4}
\]

is a perfect containment matching because (e_i\subset T_i).  Thus the 49
missing marked rank-eight parent values are replaced by 49 distinct marked
facets with a canonical SDR.  The full containment graph has 128 edges,
but those extra incidences are not needed for existence.

The unique non-linear-parent facet is the small-cycle closure colour

\[
 e_{6390}=T_{6434}\cap T_{6390}
          =\mathtt{0x4671}
          \subset\mathtt{0x4679}=T_{6390}.                    \tag{3.5}
\]

All other facets in (3.3) equal the corresponding linear (D^2) value of
the K15 word.

#### Proof

Adjacent vertices in each parent component are Johnson adjacent, hence
their intersection has rank seven and is contained in the head vertex.
Direct replay gives (3.3), distinctness, and (3.5).  Therefore (3.4) is an
injective incidence matching.  \(□\)

### Corollary 3.2 (why 49 occurs)

Exactly four vertices are removed from the marked copy of the large cycle,
and all 45 vertices of the small component are represented on the facet
rail.  Hence

\[
                         49=45+4=45+(d+1),\qquad d=3.          \tag{3.6}
\]

The four large-cycle facets are also exactly the four (D^3)-windows
starting at 6386,6387,6388,6389 which contain the reserved singleton
letter `0x8000` at physical position 6389.  This explains the local
(d+1) width in this certificate.  It does not prove that every even lift
must use (d+1) facet rows.

## 4. Rank ledger and nonflatness

The trace (S) is simple, but it is not flat:

\[
 |\{s\in S:|s|=8\}|=6484=6435+49,
 \qquad
 |\{s\in S:|s|=9\}|=6386=6390-4.              \tag{4.1}
\]

All 12,870 values are distinct.  In particular, the facet bridge is an
actual two-rank chronology, not noise which may be discarded by a WLOG
flatness assumption.

## 5. Facet rays recover the whole upper tower

The bridge is stronger than a containment SDR.  It is a literal local
inverse to one adjacent-OR derivative.

### Lemma 5.1 (turn-colour ray identity)

Let

\[
  \cdots,v_{i-1},v_i,v_{i+1},\cdots
\]

be a directed Johnson path of rank-(r) vertices and put

\[
 e_i=v_{i-1}\cap v_i,qquad e_{i+1}=v_i\cap v_{i+1}.
\]

If (e_i\ne e_{i+1}), then

\[
                         e_i\cup e_{i+1}=v_i.                 \tag{5.1}
\]

Consequently, for a directed arc (v_a,\ldots,v_b),

\[
 D(e_a,e_{a+1},\ldots,e_b,v_b)=(v_a,v_{a+1},\ldots,v_b).    \tag{5.2}
\]

For a directed cycle, if (e_a) is the closure colour from the preceding
vertex (v_{a-1}), then

\[
 D(v_{a-1},e_a,e_{a+1},\ldots,e_{a-1})
   =(v_{a-1},v_a,\ldots,v_{a-2}).                            \tag{5.3}
\]

#### Proof

Both (e_i) and (e_{i+1}) are rank-((r-1)) subsets of (v_i).
Distinct such facets omit distinct elements, so their union is (v_i).
The displayed derivative identities apply this observation successively;
the endpoint socket is already a superset of its incident facet.  \(□\)

A globally lower-rainbow factor automatically has (e_i\ne e_{i+1}).

### Theorem 5.2 (exact K16 absorption)

In the K16 trace, the four large-cycle facet rows at starts 6386 through
6389, followed by the unmarked socket at start 6390, satisfy

\[
 D(S[6386,6391))
   =(z\cup T_{5109},z\cup T_{5110},z\cup T_{5111},z\cup T_{5112}). \tag{5.4}
\]

For the small component, the unmarked socket at start 12824 followed by all
45 terminal facet rows satisfies

\[
 D(S[12824,12870))
  =(z\cup T_{6425},z\cup T_{6426},\ldots,z\cup T_{6434},
    z\cup T_{6390},\ldots,z\cup T_{6424}).                   \tag{5.5}
\]

Thus every one of the 49 deleted marked upper lifts is restored one
derivative later.  There are 48 forward extensions of a facet window and
one left-seam/closure recovery; there is no uncovered terminal debt.

By associativity of adjacent OR,

\[
                    D^q(D E)=D^{q+1}E,                       \tag{5.6}
\]

so any deeper parent flag supported wholly inside one of the displayed
recovered strings is inherited automatically.  Only flags crossing an end
of (5.4) or (5.5) belong to the finite collar ledger.  This is the precise
all-depth content of the facet bridge; it does not assert that those collar
flags, residence, or the lower compiler are automatic.

## 6. Conditional general cut/jump/facet-bridge lemma

### Lemma 6.1

Let a rank-(r) Johnson 2-factor have components (C_0,C_1,\ldots,C_{c-1}).
Choose an oriented consecutive arc (A) of (h) vertices of (C_0), and
put

\[
 R=A\cup C_1\cup\cdots\cup C_{c-1}.                         \tag{6.1}
\]

Assume that the incoming turn colours

\[
                 e(v)=\operatorname{pred}(v)\cap v,qquad v\in R, \tag{6.2}
\]

are pairwise distinct.  Then replacing the marked upper lift (z\cup v)
by the marked facet (z\cup e(v)) for every (v\in R) has the following
exact properties:

1. it removes precisely (|R|) upper-lift states and introduces precisely
   (|R|) distinct facet states;
2. (e(v)\mapsto v) is a canonical containment SDR;
3. if the secondary component lengths are (L_1,\ldots,L_{c-1}), then
   writing a rotation of (C_0) in indices modulo the full concatenated
   deck creates an apparent offset jump of
   (L_1+\cdots+L_{c-1}), not a new phase invariant; and
4. if the parent components are strict (q)-sheet spirals and all are cut
   at one sheet (t), the two chunk lengths of component (j) are
   ((q-t)n_j) and (tn_j), where (L_j=qn_j).

#### Proof

Items 1 and 2 follow immediately from pairwise distinctness and
(e(v)\subset v).  Item 3 is the conversion from reduction modulo
(|C_0|) to reduction modulo the full deck.  Item 4 is the definition of
a strict spiral cut.  \(□\)

When the parent lower-turn palette is globally rainbow, the distinctness
hypothesis is automatic for every (R).  This is the useful recursive
content: the central incidence matching of a facet bridge costs no new Hall
argument.

### Physical-realization qualification

Lemma 6.1 is a trace-level lemma.  To obtain a literal child word one must
still solve the window equations which realize the proposed two-rank trace.
To obtain an RSB induction one must additionally prove, for the chosen
bridge:

* residence at every coordinate;
* preservation or replacement of every deep upper witness;
* an admissible lower compiler schedule;
* one simultaneous common-cap assignment, not merely the containment SDR;
* and compatible boundary/seam states.

None of these follows from (6.2).  For K16 they are supplied by the frozen
certificate and its direct common-cap model.  Thus the lemma identifies a
promising even-recursion interface—common-phase component rotations plus a
turn-colour facet bridge—but is not a proof of a uniform odd-to-even lift.

### Lemma 6.2 (exact literal window test)

There is nevertheless a simple necessary-and-sufficient test for the first
of those missing steps.  Let (S_0,\ldots,S_{N-1}) be any proposed subset
trace at depth (d).  For each coordinate (x), define the allowed source
positions

\[
 P_x=\{0,\ldots,N+d-1\}\setminus
       \bigcup_{i:x\notin S_i}\{i,i+1,\ldots,i+d\}.            \tag{6.3}
\]

Then there is a (not necessarily nonempty-letter) word
(A_0,\ldots,A_{N+d-1}) with (D^dA=S) if and only if

\[
        P_x\cap\{i,\ldots,i+d\}\ne\varnothing
        \quad\hbox{for every }i\hbox{ and every }x\in S_i.    \tag{6.4}
\]

Indeed, every zero trace window forbids (x) at all its source positions,
which proves necessity.  Conversely, put (x) at every position in (P_x).
Equation (6.4) makes every required window positive, while (6.3) makes every
forbidden window zero.  Coordinates are independent.  Requiring every
letter to be nonempty, imposing caps, and realizing the lower compiler all
remain coupled extra conditions.

For the K16 top coordinate, the zero trace interval is
`[6390,12825)`, which forces source zeros on `[6390,12828)`.  The literal
singleton `0x8000` at source position 6389 lies in exactly the four trace
windows starting at 6386 through 6389, and those are precisely the four
large-cycle facet rows in (3.3).  Thus the local (d+1) bridge is visible
both in the turn-colour factor and in the exact OR-window provenance.

## 7. Independent audit

The light standard-library replay

```text
scratch/audit_k16_two_shift_facet_bridge_20260731.py
```

hashes both words before use and checks all formulas above, the 49 canonical
incidences, the 128-edge full containment graph, and the child rank ledger.
It performs no search.
