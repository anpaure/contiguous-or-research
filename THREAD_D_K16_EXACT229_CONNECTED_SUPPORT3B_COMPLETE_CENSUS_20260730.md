# Exact229 connected support-three census

Date: 2026-07-30  
Status: **complete scoped no-pass**

## The class

Let `T[0],...,T[12872]` be the frozen exact229 chronology.  A connected
support-three move chooses

\[
0\le x<y<z<12873,\qquad 1\le y-x\le6,\quad1\le z-y\le6,
\]

and replaces `(T[x],T[y],T[z])` by one of its two directed nonidentity
3-cycles.  Thus the number of oriented descriptors is exactly

\[
2\sum_{a=1}^6\sum_{b=1}^6(12873-a-b)
=2(36\cdot12873-252)=926352.
\]

This is precisely class B of the frozen A/B normal form.  It is not the
quadratic one-close-edge/remote-third class A.

## Exact replay theorem

For every descriptor the census does all of the following literally.

1. It changes the three occurrence positions simultaneously.
2. It recomputes every affected adjacent equality.  Descriptors changing the
   total number of flat edges are rejected; otherwise the induced depth
   schedule is updated by the exact prefix flat charge.
3. Because the maximum compiler depth is three, all changed envelope and
   middle-row equations lie in `[x-3,z+3]`.  The engine checks that complete
   window and then performs a second all-row replay on every local survivor.
4. Every middle-exact survivor receives the unrestricted accumulated-union
   upper audit over all interval widths.
5. Every exact+upper survivor is handed to the generalized Hall program on
   all rank-below-eight targets and all proper-prefix cells.  The fixed
   `212/187` exact229 shore is diagnostic only.

The exact counts are

| ledger | count |
|---|---:|
| oriented descriptors | 926,352 |
| invalid total flat charge | 662 |
| flat-valid, two changed positions | 3 |
| flat-valid, three changed positions | 925,687 |
| local middle-exact | 1 |
| full all-row replays | 1 |
| local/full disagreements | 0 |
| middle-exact | 1 |
| arbitrary-upper audits | 1 |
| exact and arbitrary-upper-complete | **0** |
| generalized-Hall candidates | **0** |

The unique middle-exact descriptor is

\[
(x,y,z;\epsilon)=(12868,12870,12872;0).
\]

It rotates old values

```
8c67, cc63, ce61
```

to

```
cc63, ce61, 8c67.
```

Its flat schedule is relocated, its reconstructed middle chronology is
exact, and its chronology SHA-256 is
`9edae717631119643a126fc551aa7b13b0236a6f7954ec40846498b87f245563`.
The independent arbitrary-width replay finds exactly the three upper holes

```
8ce7, bcef, cc67.
```

Consequently no Hall call is mathematically required in this class.  The
fail-closed Hall orchestrator confirms expected candidates `0`, completed
candidates `0`, and status `NO_EXACT_UPPER_PATCHES`; its return code 2 is the
documented deficient/no-candidate status, not a resource failure.

## Shifted-eight gate

On the unique exact hit, cells 13964 and 13966 are both present and retain
all their old candidates:

```
13964: {6809,6829}
13966: {4809,4829}
```

Neither acquires the required shifted target (`6a29` and `4a29`,
respectively), and neither exact pass-0 shifted profile is realized.  Hence
this complete connected class does not physically realize the conditional
two-path `0200` repair.

## Scope and surviving branch

The theorem closes only one directed 3-cycle on three positions whose two
successive gaps are at most six, on the frozen exact229 chronology.  It says
nothing about class A, multiple interacting cycles, or applying the same
local class after a nonlocal braid.

The immediate surviving branch is therefore the requested composition with
the four authenticated nested forward-swap Hall-24 chronologies.  Those four
parents must be treated as new literal bases: dynamic exactness, unrestricted
upper coverage, and the full generalized matching must all be recomputed.
Conditional halo incidences are not physical edges and may not be credited.

## Reproducibility

The successful run used one H100 CPU under a 2 GiB address-space cap.

- Native census: 0.65 s wall, 6,196 KiB maximum RSS, exit 0.
- Zero-candidate Hall audit: 0.63 s wall, 58,880 KiB maximum RSS, documented
  exit 2.

The first launch attempt stopped before compilation because its generated
checksum file contained literal `n` separators.  It produced no mathematical
output.  The successful `_r1` run used an uploaded frozen checksum manifest.

Frozen principal hashes:

```
engine source   8d2a884c7546771f3cd8e1a8447f1d04a31df649661293bdd2a69beeb6069a01
launcher        b435196c34373a5b09c0d315f4ea89b88a5a6a90aae73256803a4f934bcc6df1
checksum file   0c126aadee4952d14ed6a7e12de543bba38baff33e4f4d2e8803d1f96a974946
native result   a73bd7aff96bb1c3e1f2d8b97b05b2a5dd8ba27e4bcf634503940f226e01b3b1
exact ledger    036d62a6ff24119aea2114ea34ebcca61c6ed1fda9f9f531a72c5e908254acc8
patch ledger    dd3e4d0d672b0e1f41b50075fda62ff00ace3165ef2b360478ddf0f398ec36da
Hall summary    16229172c2ffa4351d7c290c2f7e1514e51e6776f0995d8b8308ae79e3def99d
```

The complete synchronized artifact directory is
`scratch/threadD_k16_exact229_support3B_connected_20260730/`; its
`output_sha256.txt` replays without error.
