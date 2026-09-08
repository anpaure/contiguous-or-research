# Adversarial geometry and packing audit of the \(H\)-wide \(Q_8\) controller

Date: 2026-07-26

Method: pure mathematics only.

Audited source:

\[
\texttt{MATH\_THEOREM\_HWIDE\_COMPILER\_CONTROLLER\_FOR\_Q8\_CAROUSEL\_20260726.md}.
\]

This note audits the ambient coordinate budget, doubled-permutation
isometry, owner support, local-to-global compilation, and the relation to
CPM/EMSF.  It also proves the exact zero-collision statement available on
the uniquely registered fixed atlas.

## 0. Verdict

Four conclusions are exact.

1. **Each local macrocycle is valid.**  On disjoint split pairs,

   \[
                 \Pi\Pi,\qquad \Pi=B\Sigma A,
   \]

   is a doubled permutation of its \(D=r+8+8L\) active directions.  It is
   a literal isometric \(C_{2D}\) in the middle Johnson layer.

2. **The source omits four split pairs from its coordinate count.**  Its
   four frozen tag pairs require

   \[
                              D+4\le m.                       \tag{0.1}
   \]

   The displayed choice \(L=\lfloor(m-r-8)/8\rfloor\) gives only
   \(D\le m\).  The exact repair

   \[
              L=\left\lfloor {m-r-12\over8}\right\rfloor      \tag{0.2}
   \]

   gives

   \[
                         m-11\le D\le m-4.                    \tag{0.3}
   \]

   This preserves \(D\sim m\), makes all declared blocks disjoint, and
   enforces the strict EMSF condition \(D<m\).

3. **The uniquely tagged fixed-atlas family has no seam collisions at
   all.**  If at most one macro is used for each ordered pair
   \((C,Y)\), where \(C\) is a \(Q_8\) cycle and \(Y\) a controller
   cycle, then for every \(q\le H\) both signed trace maps are globally
   injective on this family.  Thus

   \[
                             E_q^-=E_q^+=0.                    \tag{0.4}
   \]

   This includes both antipodal occurrences, global turnarounds, mixed
   controller interfaces, and every homogeneous \(Q_8\) seam.

4. **That zero-collision family is exponentially too small.**  The
   controller factor on \(Q_r\) has \(2^r/(2r)\) cycles and the \(Q_8\)
   factor has sixteen.  Hence the proved registry has

   \[
            M\le {8\,2^r\over r},\qquad
            G=2DM\le {16D\over r}\,2^r.                       \tag{0.5}
   \]

   Since \(r=O(H)=o(m)\), this is \(G=2^{o(m)}\), while

   \[
                 W_m=\binom{2m}{m}=2^{2m-o(m)}.               \tag{0.6}
   \]

   A macroscopic completion must reuse registry pairs, add payload
   translates, or change split-pair atlases.  The tag/controller decoder
   then no longer identifies the macro.  No cross-copy collision theorem
   or near-spanning owner matching is proved in the source.

Therefore the corrected construction is an exact local strip theorem.  It
is not an unconditional CPM option, EMSF factor, or coefficient-one proof.

## 1. Exact coordinate ledger

In the support-revealing Johnson realization, every physical cube
direction is represented by a disjoint ground pair

\[
                           \{a_i,b_i\};                        \tag{1.1}
\]

an owner contains exactly one endpoint, and a cube move exchanges the two
endpoints.  The macro uses

\[
\begin{array}{c|c}
\text{block}&\text{number of split pairs}\\ \hline
\text{controller}&r\\
Q_8\text{ carousel}&8\\
\text{eight payload runs}&8L\\
\text{frozen cycle tags}&4.
\end{array}                                                  \tag{1.2}
\]

Thus \(D=r+8+8L\) pairs are active but \(D+4\) pairs are occupied.  The
four selected tag endpoints together with an exterior set of size
\(m-D-4\) form the fixed part of each middle owner.  This proves the
necessary condition (0.1).

For (0.2), put \(x=m-r-12\).  Since

\[
                         x-8<8\lfloor x/8\rfloor\le x,
\]

\[
\begin{aligned}
D&=r+8+8\lfloor(m-r-12)/8\rfloor\le m-4,\\
D&>r+8+(m-r-12)-8=m-12.
\end{aligned}                                                \tag{1.3}
\]

Integrality gives (0.3).  Also

\[
                         m\ge r+8H+12                         \tag{1.4}
\]

implies \(L\ge H\).  Because \(r<8(H+1)\) and \(H=o(m)\), (1.4) holds
for all sufficiently large \(m\).

The tags cause no rank or isometry problem: each tag pair contributes one
fixed endpoint to every owner and therefore to every lower and upper
target.  Sixteen tag orientations distinguish the sixteen \(Q_8\)
cycles.

## 2. Literal isometry

Write

\[
             \Pi=(\pi_0,\ldots,\pi_{D-1})=B\Sigma A.          \tag{2.1}
\]

The controller directions occur exactly once because \(BA=\kappa\).
The first half of the chosen \(Q_8\) cycle uses its eight directions once,
and the payload blocks contribute \(8L\) distinct directions.  Thus
\(\Pi\) is a permutation of all \(D\) active directions.

Every cyclic interval of at most \(D\) moves in \(\Pi\Pi\) uses distinct
directions.  Two cycle vertices at cyclic distance \(s\le D\) therefore
differ on exactly \(s\) split pairs.  Their Johnson distance is \(s\).
The cycle is simple and isometric.

More explicitly, let \(u_j\) be the endpoint removed by direction
\(\pi_j\) during the first half and \(v_j\) its mate.  Put

\[
 z_j=u_j,\qquad z_{D+j}=v_j\quad(0\le j<D).                    \tag{2.2}
\]

After cyclic reindexing the macro owners are

\[
               K\cup I_z(t,D),\qquad t\in\mathbb Z/(2D),      \tag{2.3}
\]

where \(K\) consists of the tag endpoints and the fixed exterior set.
This is literally a cyclic \(D\)-strip in the EMSF sense.

Pausing the controller during \(\Sigma\) does not affect factorhood.
Its nonstationary first-half projection is \(BA=\kappa\); the \(Q_8\)
projection follows the selected \(Q_8\) cycle.  The doubled-permutation
argument already proves the owner cycle without invoking a formal frame
identity.

## 3. Exact owner disjointness

Let \({\cal S}(C,Y)\) be the support of a macro based on a \(Q_8\) cycle
\(C\) and controller cycle \(Y\).  Every owner in this support projects
to a vertex of \(C\) and a vertex of \(Y\).  Since the child factors
partition their cubes,

\[
 {\cal S}(C,Y)\cap{\cal S}(C',Y')\ne\varnothing
 \quad\Longrightarrow\quad C=C'\text{ and }Y=Y'.              \tag{3.1}
\]

Consequently, a family with no repeated pair \((C,Y)\) is owner-disjoint.
The union of the cyclic successors on any such family is one exact
permutation of its declared owner union.  There is no further local
factor-consistency problem once whole cycles are owner-disjoint.

This argument does not prove that two payload translates with the same
\((C,Y)\) are disjoint, nor that macros built from different ground-pair
atlases are disjoint.  Those are the copies needed for macroscopic
coverage.

## 4. Fixed-atlas zero-collision lemma

### Lemma 4.1

Use one split-pair atlas, give the sixteen \(Q_8\) cycles distinct frozen
tags, and select at most one macro per pair \((C,Y)\).  If
\(1\le q\le H\le L\), then each map

\[
 X_t\longmapsto\bigcap_{j=0}^qX_{t+j},
 \qquad
 X_t\longmapsto\bigcup_{j=0}^qX_{t+j}                        \tag{4.1}
\]

is injective over every cyclic start of every selected macro.

### Proof

Suppose two targets of the same sign and depth are equal.  Their
restrictions to the frozen tag pairs agree, so their tags identify the
same \(Q_8\) cycle \(C\).

Let \(d\) be the number of controller moves in the corresponding
\(q\)-window.  On the controller block a lower target has exactly \(d\)
empty split pairs, while an upper target has exactly \(d\) full split
pairs.  Thus the restricted target determines \(d\).

Since \(q\le H\le L\), a window cannot cross the whole core
\(\Sigma\).  All its controller moves consequently form one consecutive
controller segment.  At a global turnaround this segment lies in \(AB\),
which is consecutive in \(\kappa\kappa=BABA\).

If \(d=0\), the controller restriction contains exactly one endpoint of
every controller pair and is therefore one complete controller vertex.
The controller factor partitions \(Q_r\), so this vertex belongs to a
unique controller cycle \(Y\).  The two core pauses on one macro have
complementary controller vertices, so the restriction also separates the
antipodal occurrences.

If \(d>0\), stationary repetitions during the core do not change an
intersection or union.  The restriction is exactly the literal signed
trace of a consecutive \(d\)-move segment of the controller factor.
Because \(d\le q\le H\), compiler injectivity recovers its start and,
in particular, its unique controller cycle \(Y\).  This also separates
the two antipodal copies.

The two equal targets have now recovered the same registry pair
\((C,Y)\), hence the same macrocycle.  On one cyclic \(D\)-strip, its
lower target is

\[
                         K\cup I_z(t+q,D-q),                   \tag{4.2}
\]

and its upper target is

\[
                         K\cup I_z(t,D+q).                    \tag{4.3}
\]

For \(0<q<D\), intervals of either displayed proper length in a cyclic
order of \(2D\) distinct labels have distinct underlying sets at distinct
starts.  Thus the starts agree. \(\square\)

Lemma 4.1 proves

\[
                             E_q^-=E_q^+=0                    \tag{4.4}
\]

on the certified fixed-atlas registry.  In particular, the homogeneous
\(Q_8\) seams do not contribute merely \(O(1)\) collision excess there;
they contribute zero.

## 5. Exact size of the certified registry

The \(Q_8\) factor has \(2^8/16=16\) cycles.  The controller factor on
\(Q_r\) has \(2^r/(2r)\) cycles.  Therefore the unique registry satisfies

\[
             M\le16{2^r\over2r}={8\,2^r\over r},\qquad
             G=2DM\le {16D\over r}\,2^r.                      \tag{5.1}
\]

With \(r<8(H+1)=o(m)\),

\[
                         \log_2G\le r+O(\log m)=o(m),          \tag{5.2}
\]

whereas

\[
                         \log_2W_m=2m-O(\log m).               \tag{5.3}
\]

Thus the exact zero-collision family has exponentially vanishing density.

Even allowing every active orientation, every tag orientation, and every
admissible exterior set in one fixed pair atlas gives at most

\[
  2^{D+4}\binom{2m-2D-8}{m-D-4}                              \tag{5.4}
\]

middle owners.  For \(m-11\le D\le m-4\), the binomial factor is bounded
by \(\binom{14}{7}\), so (5.4) is \(2^{m+O(1)}=o(W_m)\).
Therefore even a hypothetical payload completion inside one fixed pair
atlas cannot have positive middle-layer density.

The same capacity loss holds for targets.  At depth \(q\), one fixed
atlas supplies at most

\[
  2^4\binom Dq2^{D-q}
       \binom{2m-2D-8}{m-D-4}                                 \tag{5.5}
\]

lower targets, and the same upper bound for upper targets.  For
\(D=m-O(1)\) and \(q=o(m)\), this is \(2^{m+o(m)}\), while

\[
                         \binom{2m}{m\pm q}=2^{2m-o(m)}.       \tag{5.6}
\]

A global theorem must therefore mix many different pair atlases or use a
different realization.

There is also an elementary obstruction to naive full-packet completion.
A \(D\)-dimensional split-pair packet contains \(2^D\) owners.  A factor
entirely into \(C_{2D}\)'s requires

\[
                                2D\mid2^D,                    \tag{5.7}
\]

equivalently, \(D\) is a power of two.  The source's generic value
\(D=r+8+8L\) need not be a power of two.

## 6. Why the \(64HM\) statement does not solve the outer problem

On the family for which macro identity is certified by the tag and
controller restrictions, Lemma 4.1 gives zero, stronger than
\(64HM\).  To obtain \(G=W-o(W)\), however, one must add macros outside
that registry.  Two such copies can share the same tag \(C\) and the same
controller trace \(Y\), or can use incomparable coordinate atlases.
Then equality of restricted targets no longer identifies a macro.

The local calculation at one same-oriented seam only compares starts
whose macro is already known.  It does not bound target collisions between
two new copies.  Therefore it does not prove

\[
 \sum_{q\le H}(E_q^-+E_q^+)\le64HM                             \tag{6.1}
\]

for an unspecified macroscopic completion.  Such a bound would require an
additional cross-copy separator or a colored owner/target matching theorem.

The precise dichotomy is

\[
\begin{array}{c|c|c}
\text{family}&\text{proved collision ledger}&\text{owner mass}\\ \hline
\text{fixed atlas, unique }(C,Y)&0&2^{o(m)}\\
\text{macroscopic completion}&\text{not proved}&\text{potentially }W-o(W).
\end{array}                                                  \tag{6.2}
\]

## 7. CPM/EMSF boundary

With the corrected root-scale choice,

\[
                             D\in[m-11,m-4].                  \tag{7.1}
\]

Thus one macro is geometrically a valid EMSF strip: \(D<m\), and
\(H/D\to0\).  If an independent theorem packed such macros on
\(W-o(W)\) owners and proved aggregate cross-macro target coverage, their
union would be legitimate EMSF input.  Neither assertion is supplied.

The root-scale value \(D=\Theta(m)\) is not the standard CPM packet radius,
which must be \(o(m)\).  The local construction could instead choose

\[
                             H\ll D=o(m),                      \tag{7.2}
\]

and would then be scale-compatible with CPM.  It would still not be a
completed \(2^D\)-owner packet option: packet completion, owner-disjoint
colored selection, and cross-packet target control remain open.

An owner-disjoint collection of already constructed whole macros is
globally compilable in the modest graph-theoretic sense: unite their
successor permutations.  CPM/EMSF require the much stronger near-spanning
owner partition and aggregate literal target-hole bound.

## 8. Corrected geometric theorem

### Theorem 8.1

Let \(H=o(m)\).  Let \(n=4\cdot2^t\) be least with
\(n\ge2(H+1)\), put \(r=2n\), and assume \(m\ge r+8H+12\).
Define \(L,D\) by

\[
 L=\left\lfloor {m-r-12\over8}\right\rfloor,\qquad
 D=r+8+8L.                                                  \tag{8.1}
\]

Then the \(H\)-wide construction, including all four tag pairs, embeds
on mutually disjoint ground-pair blocks in \(\binom{[2m]}m\).  It has
\(L\ge H\), \(m-11\le D\le m-4\), and every macro is a literal isometric
cyclic \(D\)-strip.

Any family with no repeated \((Q_8\text{-cycle},\text{controller-cycle})\)
pair is an exact owner-disjoint factor of its declared union and has
globally injective lower and upper traces through depth \(H\).  Its owner
mass is at most

\[
                              {16D\over r}\,2^r=2^{o(m)}.       \tag{8.2}
\]

No near-spanning completion or cross-copy collision bound follows.

### Proof

The coordinate ledger is Section 1, isometry is Section 2, owner
disjointness is Section 3, trace injectivity is Lemma 4.1, and the mass
bound is Section 5. \(\square\)

The first exact local error in the source is the omitted four-tag-pair
budget.  After repairing it, the first substantive failure is global:
the certified zero-collision registry is negligible, while the copies
needed to make it macroscopic have no proved disjoint packing or
cross-target decoder.
