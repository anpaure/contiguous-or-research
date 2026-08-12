# The successor motif-820 core has exactly two minimal full-q1 C4 escapes

Date: 2026-07-29  
Status: proved by a bounded exact Johnson/provider census.  This note proves
minimal literal certificate escape, not residence completion or feasibility of
the rebuilt overlay.

## 1. Frozen input and scope

Let \(Q_2\) be the twice-preconditioned physical factor

```text
scratch/k16_failedlit0_mixed_hall_escape_u27742_plus_l57614_20260729.json
SHA-256 b935ee4a4ce3c494e7f2daf2756b3c6aeba2751b39f996082edf16e298642b49
```

and let the deletion-minimal successor core be

```text
scratch/k16_mixed_hall_escape_both_guarded_core_20260729.json
SHA-256 285063a11c1894f3420fe442a7c3d2f6cb16138ab8ff8fbd1b5980569ddad6a6
```

The core has ten lower and eight upper source-unique q1 rows and the
coordinate-5, length-2 motif with closure

\[
 {\cal M}_{820}=\{(64036,64040),(64036,65028),(64040,64264)\}.       \tag{1.1}
\]

The factor \(Q_2\) has 12,870 edges, degree two at every middle vertex,
both complete physical q1 palettes, two components of lengths 13 and 12,857,
and 2,224 residence violations.

## 2. Exhaustive radius-two reduction

For a rank-seven colour \(L\), its physical providers are

\[
 \{(L\cup\{a\},L\cup\{b\}):a,b\notin L, a\ne b\},                 \tag{2.1}
\]

and there are \(\binom92=36\).  Dually, a rank-nine colour \(U\) has the 36
providers

\[
 \{(U\setminus\{a\},U\setminus\{b\}):a,b\in U, a\ne b\}.         \tag{2.2}
\]

Suppose a two-edge switch creates a second occurrence of one of the 18
source-unique guarded colours.  One inserted edge is therefore among the
\(18\binom92=648\) providers in (2.1)--(2.2).  If that edge is \(uv\), a
degree-balanced two-edge switch must delete one of the two old factor edges
at \(u\), one of the two old factor edges at \(v\), and insert the edge joining
their other endpoints.  Thus there are at most four completions per provider.
This proves that the audit below is exhaustive for every radius-two guarded-
redundancy escape.

Likewise, a radius-two direct repair of (1.1) must delete one of its three
closure edges.  Each such deletion removes at least one source-unique guarded
provider; complete q1 coverage forces an inserted replacement provider.
Consequently it is included in the same census.

There are two further abstract ways a carrier edit could invalidate the
signed Farkas row without either operation: delete a common (Q_2\cap R)
edge of positive gain, or insert a new Q-only blue edge of negative gain.
The full-overlay audit finds no common positive-gain edge.  It also checks
all 342 Q-absent negative-gain seams (340 outside (Q_2\cup R)): their 97
degree-balanced C4 completions include no full-q1 completion.  Therefore
every radius-two break of this fixed certificate changes an active source
provider or hits the motif closure, and the provider census is exhaustive.

The exact audit deduplicates these completions, checks both inserted edges are
Johnson edges absent from the current factor, and replays all
\(\binom{16}{7}=\binom{16}{9}=11{,}440\) physical q1 rows.  It finds 173
distinct degree-balanced candidates and exactly two complete-q1 survivors.

## 3. The unique guarded-redundancy escape

The first survivor is

\[
\begin{array}{ll}
\text{delete}&(43789,47629),\ (44557,44809),\\
\text{insert}&(43789,44809),\ (44557,47629).                \tag{3.1}
\end{array}
\]

Its complete nonzero q1 load ledger is

\[
\begin{array}{c|cc}
L_{43785}&1&2\\
L_{44553}&2&1\\
U_{47885}&3&2\\
U_{48653}&1&2.
\end{array}                                                \tag{3.2}
\]

Thus it creates a second provider of the guarded source-unique colour
\(L_{43785}\) and creates no q1 hole.  The old source-unique inequality
\(b_{9423}\le0\) is therefore replaced after rebuilding by a two-provider
capacity row; its zero-anchor force disappears.
Both deleted edges are \(Q_2\setminus R\), and both inserted edges are outside
\(Q_2\cup R\), against the frozen canonical physical endpoint reconstruction.
It does not touch (1.1).  It removes one old short motif and creates four,
so the residence count increases from 2,224 to 2,227; the component lengths
remain 13 and 12,857.  This is a certificate escape, not progress on
residence.

## 4. The unique direct motif-820 escape

The second survivor is

\[
\begin{array}{ll}
\text{delete}&(56088,64024),\ (64040,64264),\\
\text{insert}&(56088,64264),\ (64024,64040).                \tag{4.1}
\end{array}
\]

Its complete nonzero q1 ledger is

\[
\begin{array}{c|cc}
L_{55832}&2&1\\
L_{56072}&1&2\\
U_{64056}&1&2\\
U_{64296}&2&1.
\end{array}                                                \tag{4.2}
\]

The guarded colour \(L_{64008}\) is preserved exactly: its old provider
\((64040,64264)\) is replaced by \((64024,64040)\).  The switch deletes a
closure edge of (1.1), so motif 820 itself disappears.  However, it creates
the new coordinate-5, length-2 motif

\[
 \{(64024,64040),(64036,64040),(64036,65028)\}.             \tag{4.3}
\]

Hence it merely slides the bad collar by one edge.  The total residence count
stays exactly 2,224, while the physical components change from lengths
\((13,12857)\) to \((13,2270,10587)\).
Again, both deleted edges are \(Q_2\setminus R\), and both inserted edges are
outside \(Q_2\cup R\).  Thus the \(L_{64008}\) source-unique blue variable is
transported to a new blue edge rather than made common with the resident shore.

## 5. Exact minimality and boundary

**Theorem.**  The minimum radius of a nontrivial literal degree-balanced,
complete-q1 edit which invalidates the frozen 19-row motif-820 certificate is
two.  Within radius two, (3.1) is the unique escape by guarded-colour
redundancy and (4.1) is the unique escape by direct deletion of the motif-820
closure.

**Proof.**  If one edge of a simple two-factor is deleted and one is inserted
while all degrees are preserved, the deleted and inserted edges have the same
endpoint multiset.  As undirected non-loop edges they are equal, so the edit
is trivial.  Thus every nontrivial edit has radius at least two.  Both (3.1)
and (4.1) have the same four endpoint incidences on their deleted and inserted
shores, hence preserve degree, and the exact full-q1 replay proves their
claimed properties.  Section 2 proves completeness of the finite radius-two
census for either mode of escaping this guarded certificate.  Therefore the
lower bound is attained and the two survivors are unique in their respective
modes. \(\square\)

The census does not list every socket-neutral radius-two change of the
overlay; it proves that all unlisted changes leave the signed certificate
intact.  It also does not prove that
the successor overlay after either switch is feasible.  In particular,
(3.1) worsens residence and (4.1) transports rather than eliminates the
short-run defect.  Deeper shadows, topology, voltage, and literal compiler
properties have not been audited here.

## 6. Support turnover from the preceding core

The preceding detector-zero core had eight lower and thirteen upper guarded
rows.  Direct set comparison with the present ten lower and eight upper rows
gives exactly one common palette row:

\[
             C_{\rm old}\cap C_{\rm new}=\{U_{65060}\}.       \tag{6.1}
\]

Its unique source provider is \((64036,65028)\).  In the old proof this was a
peripheral zero anchor; in the successor it is one of the three motif-820
closure edges.  The motif-390 and motif-820 closure vertex sets themselves
are disjoint.  Neither (3.1) nor (4.1) uses any edge of the two prior q1-safe
preconditioning C4s.  Thus the iterative dual has genuinely migrated: (3.1)
attacks the new-only row \(L_{43785}\), while (4.1) transports the new-only
\(L_{64008}\) provider and the collar around the sole inherited row.

## 7. Permanent replay

```text
scratch/audit_k16_motif820_active_colour_c4_20260729.py
SHA-256 d8ab47dc02d17539d5bd7c04e9306a6f7ecc72ace9cb6f509e0885491b8c3ce3

scratch/k16_motif820_active_colour_c4_20260729.audit.json
SHA-256 527e9fb32b833a5d254817b67a2f07bcf5617b27d7da4771dad42ca5e49fea2b

scratch/k16_motif820_sparse_hall_20260729.audit.json
SHA-256 404c2d492983b16e908843ef6d263c8e2e9cdd6176847eea94940d51c29e7949

scratch/k16_resident_resume1_q1_canonical_physical_endpoints_20260729.json
SHA-256 fbd182aff3117581c7cf5216e33a30db3309da23c8d570275114e5a6165985e9
```

The verifier uses only the Python standard library and the already frozen
literal audit helpers.  It performs no SAT/CP solve, records 648 abstract
provider slots, and checks up to four local reconnections for each absent
provider.
