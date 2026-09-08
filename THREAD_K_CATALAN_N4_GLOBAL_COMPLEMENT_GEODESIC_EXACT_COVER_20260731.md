# Thread K: global `n=4` complement-geodesic exact cover

Date: 2026-07-31  
Status: **SAT, independently replayed**  
Scope: one finite global base case for the antipodal-geodesic filler problem; no
all-parameter recursion is asserted.

## 1. The exact hypergraph

Let `V=binom([8],4)`.  An unoriented complement geodesic is a Johnson path

\[
 P=(T_0,T_1,T_2,T_3,T_4),\qquad T_4=[8]\setminus T_0,
\]

in which every coordinate changes exactly once.  Associate to `P` its thirteen
resources

\[
 \{T_0,\ldots,T_4\}\ \sqcup\
 \{T_{i-1}\cap T_i:1\le i\le4\}\ \sqcup\
 \{T_{i-1}\cup T_i:1\le i\le4\}.                 \tag{1.1}
\]

The resource parts have sizes `70`, `56`, and `56`.  The desired object is an
exact cover of all 182 resources by fourteen rows of (1.1).

### Proposition 1.1 (complete catalogue and regularity)

There are exactly

\[
 {1\over2}\binom84(4!)^2=20,160                 \tag{1.2}
\]

unoriented complement geodesics.  Every row contains thirteen distinct
resources, and every resource in each of the three parts has degree exactly

\[
 20,160\,{5\over70}=20,160\,{4\over56}=1,440.  \tag{1.3}
\]

#### Proof

Choose one endpoint from each complementary pair.  Independently order its
four deleted and four inserted coordinates; pairing the two orders gives a
unique oriented geodesic.  Reversal supplies the other endpoint orientation,
so (1.2) follows.  On a geodesic all five vertices are distinct, as are the
four deleted-coordinate intersections and four inserted-coordinate unions.
The three ranks keep these resources mutually disjoint.  The coordinate group
is transitive on each resource part, and double counting incidences gives
(1.3).  The independent enumerator additionally checks all `262,080`
incidences and obtains the degree histogram `1440^182`.  ∎

### Proposition 1.2 (one-path symmetry fixing is lossless)

The action of `S_8` is transitive on the set of unoriented complement
geodesics.  Hence an exact cover exists if and only if one exists containing
the fixed path

\[
 (15,30,60,120,240).                              \tag{1.4}
\]

#### Proof

Write a directed geodesic as ordered lists
`(r_1,r_2,r_3,r_4)` and `(a_1,a_2,a_3,a_4)` of its removed and added
coordinates.  A coordinate permutation carrying these two ordered lists to
those of another directed geodesic carries the whole path to the other path.
Reversal passes to the unoriented action.  Finally, any exact cover is nonempty,
so one of its rows may be carried to (1.4).  ∎

## 2. Exact-cover result

### Theorem 2.1 (global antipodal-geodesic filler at `n=4`)

The hypergraph in Section 1 has an exact cover.  One certificate is the
following fourteen paths:

```text
 15  30  60 120 240
 29  89  90 114 226
 92  86  54  51 163
 58  27 147 135 197
 23  71  78 204 232
 53  45 108 106 202
102 101  85 149 153
 77 141 142 170 178
 39 166 150 154 216
 99 195 210 212 156
116 180 184 169 139
 46  43  75 201 209
 57 105 225 228 198
 83 113 177 165 172
```

They partition all seventy middle vertices.  Their fifty-six consecutive
intersections are every rank-three set exactly once, and their fifty-six
consecutive unions are every rank-five set exactly once.  Each terminal pair
is complementary and every coordinate flips once along each path.

#### Proof and proof-safety boundary

The search uses Algorithm X/DLX on the complete 20,160-row catalogue after
selecting (1.4).  For the positive conclusion, correctness of the DLX search
algorithm is not trusted: the emitted witness is replayed independently from
the masks.  The independent audit also reconstructs the full catalogue rather
than importing the searcher's rows.  It verifies:

1. exactly `20,160` canonical unoriented geodesics;
2. exactly thirteen distinct resources in every row;
3. degree `1,440` for every one of the 182 resources;
4. membership of every selected path in the reconstructed catalogue;
5. exact multiplicity one on every middle, lower, and upper resource;
6. antipodal endpoints and one flip of every coordinate on every selected
   path.

These literal checks prove the theorem independently of solver semantics. ∎

### Corollary 2.2 (universal internal residence)

Every coordinate trace on every selected path is monotone, since it flips
exactly once.  Thus no selected component has an internal positive or zero run.
The certificate is consequently safe for every internal guard width in the
independent-filler sense.  This does **not** say that arbitrary later joins of
the fourteen components are residence-safe; seam obligations remain external.

## 3. Computational provenance

The one authorized heavy run used one H100 host CPU only:

```text
host/directory: h100 (arboghast)
                /home/amodo/or15/work/laneK_n4_global_geodesic_exactcover_20260731
limits:         nice 15; address space 2 GiB; wall cap 900 s
verdict:        SAT
DLX nodes:      1,297,785
CPU/wall:       24.60 s / 24.61 s
maximum RSS:    12,204 KiB
```

Frozen artifacts:

```text
scratch/search_catalan_antipodal_geodesic_filler_n4_dlx_20260731.cpp
  5ddcb07c49406182ff15b45795ad73c91ae70f2baab5c509b7fddba2c676a201

scratch/catalan_antipodal_geodesic_filler_n4_20260731.witness.txt
  4cb494aaffc4887b261745c8d68ffc1faedf5b9a6264c8a0738a6e752846018d

scratch/catalan_antipodal_geodesic_filler_n4_20260731.h100.run.log
  17600e06343f5665b0d6d8bf6dff47125231a782908850ec31c5b5fa6240fbf7

scratch/catalan_antipodal_geodesic_filler_n4_20260731.h100.compile_hashes.txt
  862bba3a0f4239fe114693bab565935dd4a8e3b680ce056b161094469c724b3b

scratch/audit_k_catalan_n4_global_complement_geodesic_exact_cover_20260731.py
  038ddebbf2843c96e50e4504853473e70d9aef8dbebaa539b46e9b20fd249d1f

scratch/k_catalan_n4_global_complement_geodesic_exact_cover_20260731.audit.json
  b56999544df0dc1f78d7e353eec338d5ecb3b452527d15d6f8a921c128665e19
  canonical payload 9c56cbad2a7c4e45442e86e62b348bf7712cbbc972be3f3477863d1c0e568c17
```

## 4. Exact implication scope

This result establishes the global `n=4` base and separates the complete
geodesic bank from the already closed same-frame two-parent bank: the former is
SAT even though the latter contains no qualifying filler.  It does not prove a
uniform all-`n` matching theorem, direct edgewise recursion, or preservation of
deep-shadow/compiler data.  Those remain the DERF recursion gates.
