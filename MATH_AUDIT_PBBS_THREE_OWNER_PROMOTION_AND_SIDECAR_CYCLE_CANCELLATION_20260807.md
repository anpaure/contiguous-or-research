# Audit of the PBBS three-owner promotion hinge, one-spare split, and sidecar-cycle cancellation

**Date:** 2026-08-07  
**Audited notes:**

* `MATH_THEOREM_PBBS_THREE_OWNER_PROMOTION_HINGE_AND_SINGLE_Q1_SIDECAR_20260807.md`;
* `MATH_THEOREM_PBBS_PROMOTION_SIDECAR_CYCLE_CANCELLATION_20260807.md`.

## 1. Verdict

The original flat three-owner hinge passes its local suffix, rank, Johnson,
native-overlap, sidecar-sharpness, and clipped-residence checks.

The one-spare interval table in Theorem 6.1 also passes literally, but its
global conclusion needs an important correction.  Splitting (B^-) makes
the predecessor lower colour (I_-) literal, while forcing the predecessor
upper colour (J_-) to span (d+3) source positions.  In a word of length
(B(k)+1=W+d+1), every selected rank-((m+1)) witness has length at most
(d+2).  Hence the split packet trades one lower sidecar for one upper
sidecar; it does not by itself close the complete local (q_1) ticket.

The flagged-coatom arc identities and the multiset equality in the cycle
note are correct.  The inference that a cycle has zero global (q_1) cost
is false for an occurrence-labelled immediate palette.  A cycle of (h)
hinges uses each of its (h) coatom colours twice on two distinct owner
edges, and therefore consumes (h) units of lower-(q_1) duplicate slack.
That slack is only

\[
 inom{2m+1}{m}-inom{2m+1}{m-1}
 =\frac{2}{m+2}\binom{2m+1}{m}
 =\Theta(W/m).
\tag{1.1}
\]

Thus cycle cancellation can support only (O(W/m)) such hinges in a
one-copy lower palette, absent an additional physical fusion which deletes
one of the two edges carrying each repeated colour.  It cannot by itself
support a (Theta(W)) promotion bank.

The endpoint-hole lemma is correct at length (W+d), but it does not
obstruct the split construction at its stated length (W+d+1): there the
length-((d+2)) value (T_-) can itself be the selected middle witness at
the split endpoint.

## 2. Flat hinge: exact suffix and owner audit

The source positions are

\[
 \begin{array}{c|cccccc}
 	ext{position}&-d-1&-d&-d+1,ldots,-1&0&1\\ \hline
 	ext{letter}&B^-&\{u\}&K_1,ldots,K_{d-1}&B&\{v\}.
 \end{array}
\]

Since the (K_i)'s have union (M), direct endpoint arithmetic gives

\[
 \begin{array}{c|c|c}
 	ext{interval}&	ext{union}&	ext{length}\\ \hline
 [-d+1,-1]&M&d-1\\
 [-d,-1]&M\cup\{u\}=U&d\\
 [-d+1,0]&M\cup B=Y&d\\
 [-d,0]&M\cup\{u\}\cup B=T_0&d+1.
 \end{array}
\tag{2.1}
\]

The three owner windows are exactly

\[
 \begin{aligned}
 T_-&=[-d-1,-1]=M\cup\{u\}\cup B^-,\\
 T_0&=[-d,0]=M\cup\{u\}\cup B,\\
 T_+&=[-d+1,1]=M\cup B\cup\{v\}.
 \end{aligned}
\tag{2.2}
\]

All have length (d+1) and rank

\[
 (m-d-2)+1+(d+1)=m.
\]

The first edge exchanges the unique elements of (B^-\setminus B) and
(B\setminus B^-); the second exchanges (u) and (v).  The role
disjointness also gives (T_-\ne T_+), so this is a simple three-vertex
Johnson path, not merely two separately valid edges.

The positional overlaps of the two owner pairs are

\[
 [-d,-1]=U,
 \qquad
 [-d+1,0]=Y.
\tag{2.3}
\]

Their set-theoretic intersections are

\[
 I_-=M\cup\{u\}\cup(B^-\cap B),
 \qquad
 I_+=Y.
\tag{2.4}
\]

Thus the successor lower colour is native, while the predecessor overlap
has rank (m-d-1), exactly (d) below the rank-((m-1)) intersection.
The sharpness calculation

\[
 |I_-\setminus U|=(m-1)-(m-d-1)=d
\tag{2.5}
\]

is correct.  Its scope is precise: it proves that the common length-(d)
overlap cannot itself be the predecessor colour.  It does not forbid a
separate occurrence of that named colour elsewhere.

For completeness, the flat hinge's two upper colours are already literal
on the spanning intervals

\[
 J_-=T_-\cup T_0=[-d-1,0],
 \qquad
 J_+=T_0\cup T_+=[-d,1],
\tag{2.6}
\]

both of length (d+2) and rank (m+1).

The construction needs (M\ne\varnothing) if all (K_i) are required to
be nonempty.  Thus an unconditional finite-parameter statement should
include (m\ge d+3).  The stronger assumption (|M|\ge d-1) in the flat
hinge is more than is needed when repetitions among the (K_i)'s are
allowed.  The cycle note omits even the nonemptiness hypothesis.

## 3. One-spare split: all endpoints and the displaced upper sidecar

Write

\[
 B^-=C\mathbin{\dot\cup}\{b^-\},
 \qquad
 B=C\mathbin{\dot\cup}\{b\},
 \qquad |C|=d,
\]

and replace the first source letter by

\[
 A_{-d-2}=\{b^-\},
 \qquad A_{-d-1}=C.
\]

Theorem 6.1's complete table checks as follows:

\[
\begin{array}{c|c|c|c}
\text{interval}&\text{length}&\text{value}&\text{rank}\\ \hline
[-d-2,-1]&d+2&T_-&m\\
[-d-1,-1]&d+1&I_-&m-1\\
[-d,-1]&d&U&m-d-1\\
[-d+1,-1]&d-1&M&m-d-2\\
[-d+1,0]&d&Y&m-1\\
[-d,0]&d+1&T_0&m\\
[-d+1,1]&d+1&T_+&m.
\end{array}
\tag{3.1}
\]

The owner values remain

\[
 \begin{aligned}
 T_-&=M\cup\{u\}\cup C\cup\{b^-\},\\
 T_0&=M\cup\{u\}\cup C\cup\{b\},\\
 T_+&=M\cup C\cup\{b,v\},
 \end{aligned}
\]

so the two Johnson exchanges and both lower intersections are correct.

The upper intervals, however, have unequal spare cost:

\[
 \begin{array}{c|c|c}
 J_-=T_-\cup T_0&[-d-2,0]&d+3\\
 J_+=T_0\cup T_+&[-d,1]&d+2.
 \end{array}
\tag{3.2}
\]

The (d+3) is unavoidable inside this source block.  The private label
(b^-) occurs only at (-d-2), and (b) first occurs at (0); every
interval whose union is (J_-) must contain both positions.

Consequently the sentence that every other displayed central or flag cell
has length at most (d+1) must not be read as including the upper colours.
More importantly, Corollary 6.2's statement that one spare removes the
sidecar “completely” is true only for the lower shore.  The exact full
ledger is

\[
 \boxed{
 \text{flat hinge at }B+1: 1\text{ lower sidecar, }0\text{ upper};
 \qquad
 \text{split hinge at }B+1: 0\text{ lower, }1\text{ upper}.}
\tag{3.3}
\]

Here “sidecar” means that the named colour needs another admissibly short
occurrence elsewhere in the global word.

## 4. General endpoint-antichain lemma and its correct application

The endpoint argument has the following parameter-free form.

### Lemma 4.1

Let a word of length (N=W+s) contain all (W) distinct members of one
rank layer, and select one witnessing interval for each.  Then:

1. the selected intervals have distinct left and right endpoints;
2. after ordering by left endpoint, their right endpoints have the same
   strict order;
3. every selected interval has length at most (s+1); and
4. exactly (s) word endpoints are unused by the selected witnesses.

#### Proof

Two intervals with equal left endpoint, equal right endpoint, or reversed
endpoint order are nested.  Their unions would then be comparable.  Two
distinct same-rank target values cannot be comparable, so none of these
cases occurs.  Write the ordered intervals as ([a_i,b_i]).  Then

\[
 a_i\ge i,
 \qquad
 b_i\le N-W+i=s+i,
\]

and hence (b_i-a_i+1\le s+1).  The (W) distinct right endpoints leave
exactly (N-W=s) unused positions.  \(\square\)

At (B(k)=W+d), this gives maximum selected length (d+1) and (d)
unused endpoints, exactly as claimed in the cycle note.  A full
length-((d+1)) suffix of rank below (m) marks an unused middle endpoint.

At (B(k)+1=W+d+1), however, the bounds are

\[
 \text{maximum selected length }d+2,
 \qquad
 d+1\text{ unused endpoints}.
\tag{4.1}
\]

The split packet's (T_-) is a rank-(m), length-((d+2)) witness ending
at the same endpoint where the length-((d+1)) suffix is (I_-).  Thus
that endpoint is not a middle-row hole in a (B+1) word.  The assertion
“at most (d) split hinges” is valid only at length (B), where their
required length-((d+2)) owner witnesses are forbidden in the first place.
It gives no density bound on split hinges in the (B+1) programme.

Apply the same lemma to the rank-((m+1)) layer at (B+1).  This layer also
has cardinality (W), so every selected upper witness has length at most
(d+2).  Formula (3.2) then proves that the local (J_-) occurrence cannot
be selected.  This is the rigorous upper-sidecar correction in (3.3).

Near the left boundary of a linear word, “the final (d+1) letters” should
be read as the whole available prefix ending there, or the hole statement
should be restricted to endpoints with a full predecessor window.  This is
only an endpoint convention and does not affect internal split packets.

## 5. Flagged-coatom graph and cycle algebra

For a flag

\[
 U_i=M_i\cup\{u_i\}\subset Q_i,
 \qquad |Q_i|=m-1,
\]

the complement (C_i=Q_i\setminus U_i) indeed has size (d).  For
distinct (i,j), the arc condition

\[
 Q_i\setminus\{u_i\}\subset Q_j
\]

is equivalent to

\[
 Q_j=(Q_i\setminus\{u_i\})\cup\{b_i(j)\}
\]

for one unique (b_i(j)\in Q_j\setminus Q_i).  All identities

\[
 M_i\cup(C_i+b_i(j))=Q_j,
 \qquad
 U_i\cup C_i=Q_i,
 \qquad
 T_i=Q_i\cup Q_j
\tag{5.1}
\]

are correct, as are the three flat owner values and their native overlaps.

The digraph definition must explicitly exclude (i=j).  As written,
(Q_i\setminus\{u_i\}\subset Q_i) would create a loop, while the claimed
entering label (b_i(i)\in Q_i\setminus Q_i) does not exist.  Cycle covers
must therefore have neither fixed points nor two-cycles if middle-owner
simplicity is required.

For a permutation (pi), the identity

\[
 \{Q_i:i\in J\}=\{Q_{\pi(i)}:i\in J\}
\tag{5.2}
\]

is tautologically correct.  It cancels the formal signed ledger

\[
 \sum_i({\bf e}_{Q_{\pi(i)}}-{f e}_{Q_i})=0.
\tag{5.3}
\]

It does not cancel the actual lower-colour multiset of the (2|J|) owner
edges.  That multiset is

\[
 \{Q_i:i\in J\}\mathbin{\dot\cup}
 \{Q_{\pi(i)}:i\in J\}
 =2\{Q_i:i\in J\}.
\tag{5.4}
\]

Thus every (Q_i) occurs twice, and the packet has duplicate excess

\[
 2|J|-|J|=|J|.
\tag{5.5}
\]

If a simple cyclic owner row has (W) edges and must cover all

\[
 L=\binom{2m+1}{m-1}=\frac{m}{m+2}W
\]

lower colours, its entire duplicate allowance is

\[
 W-L=\frac{2W}{m+2}.
\tag{5.6}
\]

Consequently a retained bank of cycle-cancelled flat hinges necessarily
satisfies

\[
 \boxed{|J|\le\frac{2W}{m+2},}
\tag{5.7}
\]

before accounting for any other forced repeated lower colours.  For an
open owner path the right side changes by only an endpoint constant.  The
claim that no external *target occurrence* is required can still be used
as a support statement, but the stronger claims “zero net named-(q_1)
defect” and “the sidecars have disappeared exactly” are invalid unless the
global model explicitly permits the same named occurrence to service two
edge-colour demands and charges the resulting duplicate multiplicity
elsewhere.

## 6. Triangle specialization

The explicit triangle calculation is correct.  With

\[
 |R|=m-2,
 \qquad Q_x=R\cup\{x\},\quad
 Q_y=R\cup\{y\},\quad Q_z=R\cup\{z\},
\]

and (d)-sets (C_s\subset R), the flags

\[
 M_s=R\setminus C_s,
 \qquad U_s=M_s\cup\{s\}
\]

have the required ranks, (C_s=Q_s\setminus U_s), and distinguished
deletion label (s).  The three middle owners are

\[
 R+\{x,y\},
 \qquad R+\{y,z\},
 \qquad R+\{z,x\},
\]

and are distinct.  This is the bottom-type Johnson triangle.  A top-type
Johnson triangle has one common rank-(m) union on all three edges and
would duplicate the middle owner; the distinct-union hypothesis correctly
excludes it.

Distinct (C_s)'s give distinct (M_s)'s, and the distinct external labels
give distinct (U_s)'s.  If (A\) is disjoint from all three (C_s), then

\[
 K_s=R\setminus(A\cup C_s),
 \qquad G=R\setminus A
\]

indeed satisfy

\[
 M_s=K_s\mathbin{\dot\cup}A,
 \qquad G=K_s\mathbin{\dot\cup}C_s.
\]

This proves only a common-core algebraic interface.  It does not construct
a residence collar or show that the triangle can be embedded in one
positive-resident chronology.

The triangle's lower palette has six edge incidences on the three values
(Q_x,Q_y,Q_z), so it consumes exactly three units of duplicate slack.
The phrase “three distinct literal (q_1) colours” is correct as a support
statement, but must not be read as a six-edge injective palette.  Packing
(H/3) such triangles for (H=\Theta(W)) flags still consumes (H)
duplicate units and violates (5.7).

## 7. Residence interface

For either flat or split source, the three owner *values* are the same.
Their coordinate membership words are:

* (M\) and (B^-\cap B): (111);
* (u): (110);
* (B^-\setminus B): (100);
* (B\setminus B^-): (011);
* (v): (001).

Hence no positive run starts and ends strictly inside the three-owner
path.  Every run shorter than (d+1) touches a displayed boundary.  This
local interface claim is correct, including at (d=2).

It does not prove extendability.  Each boundary run must be continued for
the required number of owner positions without causing an owner repeat,
palette collision, or incompatible source-age state.  Likewise the common
set (G) in the triangle specialization is only a candidate permanent
core.  No literal (O(d))-owner collar or positive-residence theorem is
present in either audited note.

## 8. Corrected frontier

The locally valid choices at physical length (B(k)+1) are therefore:

1. **flat hinge:** all three owners and both upper colours have admissible
   local lengths, but the predecessor lower colour is a named sidecar;
2. **split hinge:** all three owners and both lower colours have admissible
   local lengths, but the predecessor upper colour is a named sidecar;
3. **cycle of flat hinges:** predecessor lower target values cancel in a
   signed support ledger, but every hinge consumes one unit of lower-palette
   duplicate slack, limiting this route to (O(W/m)) retained hinges.

Thus none of the two notes yet supplies a (Theta(W)) promotion bank with
zero or (O(1)) total (q_1) sidecars.  The exact missing local-to-global
operation must either:

* fuse away one of the two same-colour owner edges per flat hinge cycle;
* couple split hinges so that their length-((d+3)) predecessor upper
  colours receive admissibly short occurrences without linear duplication;
  or
* use a different promotion packet whose complete lower and upper palette
  ledger fits the (B+1) endpoint bounds simultaneously.
